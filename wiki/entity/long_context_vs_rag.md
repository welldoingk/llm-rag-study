# Long-Context vs RAG

## Overview
최근 LLM의 컨텍스트 윈도우(Context Window)가 1M 토큰 이상으로 확장되면서 RAG의 필요성에 대한 논의가 있었으나, 현재는 상호 보완적인 관계로 정의되고 있습니다.

## Comparison
| Feature | Long-Context | RAG |
| :--- | :--- | :--- |
| **Data Size** | 수십만 토큰 내외 | 거의 무제한 (테라바이트 급) |
| **Updates** | 프롬프트 재입력 필요 | 데이터 소스 업데이트만으로 즉시 반영 |
| **Cost** | 컨텍스트가 길수록 비용 증가 | 필요한 조각만 사용하므로 저렴 |
| **Use Case** | 단일 긴 문서/코드 전체 분석 | 방대한 지식 베이스 검색 및 질의 |

## Integration Trend
가장 효율적인 전략은 RAG로 관련 후보군을 추출한 뒤, Long-Context LLM에 전달하여 깊이 있는 고차원 추론을 수행하는 하이브리드 방식입니다.
