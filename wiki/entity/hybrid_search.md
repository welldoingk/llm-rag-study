# Hybrid Search

## Overview
하이브리드 검색(Hybrid Search)은 시맨틱 검색(Dense Retrieval)과 키워드 검색(Sparse Retrieval)의 장점을 결합하여 검색 정확도를 극대화하는 기법입니다.

## Key Components
- **Dense Retrieval (Vector)**: 질문의 의미적 맥락(Embeddings)을 파악하여 관련 문서를 찾습니다.
- **Sparse Retrieval (Keyword/BM25)**: 특정 고유명사나 코드명, 기술 용어 등을 정확하게 일치시킵니다.
- **Re-ranking**: 두 방식에서 검색된 결과들을 가중치 혹은 LLM을 통해 다시 순위화(Rank)합니다.

## Why it's a trend
벡터 검색 단독으로는 정확한 명칭 검색에 한계가 있고, 키워드 검색은 의미 파악이 안 된다는 점을 보완하기 위해 기업용 RAG의 표준이 되고 있습니다.
