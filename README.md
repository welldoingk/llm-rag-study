# RAG Trends Wiki (LLM Wiki Pattern)

이 프로젝트는 Andrej Karpathy의 "LLM Wiki" 컨셉을 바탕으로, 벡터 데이터베이스 없이 마크다운 파일과 인덱스만을 활용하여 구축된 RAG 시스템입니다. 최신 RAG 트렌드(2024-2025)를 주제로 합니다.

## 주요 특징

- **Vector-less RAG**: 벡터 DB(FAISS 등)를 사용하지 않고, LLM이 `index.md`를 먼저 읽어 관련 문서를 식별한 뒤 해당 파일들을 읽어 답변을 생성합니다. (Moderate Scale 추천 방식)
- **Persistent Wiki Structure**: 지식이 `wiki/` 디렉토리 내에 체계적으로 저장되며, `index.md`와 `log.md`를 통해 관리됩니다.
- **RAG Trends Research**: Agentic RAG, GraphRAG, Hybrid Search 등 최신 기술 트렌드 정보가 내장되어 있습니다.

## 기술 스택

- **LLM**: Azure OpenAI (GPT-4o-mini)
- **Framework**: LangChain
- **Knowledge Base**: Markdown indexed Wiki
- **Package Manager**: uv

## 위키 구조 (`wiki/`)

- `index.md`: 모든 페이지의 카탈로그 및 요약.
- `log.md`: 위키 수정 및 주입 내역 기록.
- `entity/`: 개별 기술 개념 페이지 (e.g., `agentic_rag.md`, `graph_rag.md`).
- `raw/`: 초기 리서치 원본 데이터.

## 실행 방법

### 1. 설정
`.env` 파일에 Azure OpenAI API 키와 엔드포인트를 설정하세요.

### 2. 실행
```bash
uv sync
python main.py
```

`main.py`를 실행하면 위키의 `index.md`를 조회하여 "Agentic RAG와 GraphRAG의 차이점"에 대해 답변합니다.
