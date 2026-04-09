import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

# 환경 변수 로드
load_dotenv()

AOAI_API_KEY = os.getenv("AOAI_API_KEY")
AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_DEPLOY_GPT4O_MINI = os.getenv("AOAI_DEPLOY_GPT4O_MINI")

class WikiRAG:
    def __init__(self, wiki_root="wiki"):
        self.wiki_root = Path(wiki_root)
        self.llm = AzureChatOpenAI(
            openai_api_version="2024-02-01",
            azure_deployment=AOAI_DEPLOY_GPT4O_MINI,
            temperature=0.0,
            api_key=AOAI_API_KEY,
            azure_endpoint=AOAI_ENDPOINT
        )

    def _read_file(self, file_path: Path) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def query(self, question: str):
        print(f"질문: {question}")
        
        # 1. Index 읽기
        index_content = self._read_file(self.wiki_root / "index.md")
        
        # 2. 관련 문서 식별
        selection_prompt = PromptTemplate.from_template(
            """당신은 위키 관리자입니다. 주어진 위키 인덱스를 보고 사용자의 질문에 답변하기 위해 읽어야 할 파일 목록을 골라주세요.
            파일 경로는 'entity/filename.md' 형식이어야 합니다. 관련이 없다면 빈 목록을 반환하세요.
            응답은 오직 파일 경로 목록만 쉼표로 구분해서 작성하세요. (예: entity/doc1.md, entity/doc2.md)

            #Wiki Index:
            {index}

            #User Question:
            {question}

            #Selected Files:"""
        )
        
        file_selector = selection_prompt | self.llm | StrOutputParser()
        selected_files_str = file_selector.invoke({"index": index_content, "question": question})
        selected_files = [f.strip() for f in selected_files_str.split(",") if f.strip().endswith(".md")]
        
        print(f"선택된 문서: {selected_files}")
        
        # 3. 문서 내용 결합
        context = ""
        for file_path in selected_files:
            full_path = self.wiki_root / file_path
            if full_path.exists():
                context += f"\n--- {file_path} ---\n"
                context += self._read_file(full_path)
        
        # 4. 최종 답변 생성
        qa_prompt = PromptTemplate.from_template(
            """당신은 RAG 트렌드 전문가입니다. 제공된 위키 문서 내용을 바탕으로 사용자의 질문에 친절하게 답변해 주세요.
            문서에 없는 내용이라면 모른다고 답변하세요. 한국어로 답변하세요.

            #Context:
            {context}

            #Question:
            {question}

            #Answer:"""
        )
        
        qa_chain = qa_prompt | self.llm | StrOutputParser()
        response = qa_chain.invoke({"context": context, "question": question})
        return response

if __name__ == "__main__":
    rag = WikiRAG()
    
    # 테스트 질문
    test_question = "에이전트형 RAG와 GraphRAG의 주요 차이점과 특징을 설명해줘."
    answer = rag.query(test_question)
    
    print("\n[답변]")
    print(answer)