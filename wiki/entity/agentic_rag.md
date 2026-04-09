# Agentic RAG

## Overview
에이전트형 RAG(Agentic RAG)는 단순한 질의응답을 넘어, LLM이 자율적인 에이전트로서 추론하고 도구를 사용하며 문제를 해결하는 방식입니다.

## Key Features
- **Proactive Inference**: 수동적인 검색 대신, 어떤 단계가 필요한지 스스로 계획을 세웁니다.
- **Tool Use**: 필요에 따라 검색 엔진, 데이터베이스, API 등을 선택적으로 호출합니다.
- **Incremental Logic**: 중간 결과를 검증하고, 부족한 정보가 있다면 추가 검색을 수행하는 반복 루프를 가집니다.

## Why it's a trend
기존 RAG는 단일 검색 결과에 의존하여 복합적인 질문에 취약했지만, 에이전트형은 다단계 추론(Multi-step reasoning)을 통해 높은 신뢰도의 답변을 생성하기 때문입니다.
