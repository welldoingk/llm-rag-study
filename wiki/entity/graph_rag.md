# GraphRAG

## Overview
GraphRAG는 비정형 데이터를 지식 그래프(Knowledge Graph) 형태로 구조화하여 RAG 시스템에 결합한 아키텍처입니다.

## Key Features
- **Relational Mapping**: 개체(Entity)와 관계(Relationship)를 명시적으로 연결하여 전체적인 맥락을 파악합니다.
- **Global Query Optimization**: "이 모든 보고서의 공통적인 테마는 무엇인가?"와 같은 요약 질문에 강점을 보입니다.
- **Explainability**: 노드 간의 경로를 통해 왜 그런 답변이 생성되었는지 추적하기 용이합니다.

## Architecture
1. **Entity/Relation Extraction**: 문서에서 개체와 관계를 추출.
2. **Graph Construction**: 추출된 개체들로 그래프 형성 및 커뮤니티(계층) 분석.
3. **Traversed Retrieval**: 질문과 관련된 노드를 시작점으로 주변 정보를 탐색하며 답변 생성.
