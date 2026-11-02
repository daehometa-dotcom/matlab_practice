# 3주차 · 유사성 기반 인공지능: KNN

기존 데이터의 특징과 정답 품종을 알고 있는 상태에서, 새로운 데이터의 가까운 이웃을 찾아 품종을 예측합니다.

## 권장 실행 순서

| 순서 | 파일 | 내용 |
| --- | --- | --- |
| 1 | [ex1_dataload_visualization.m](ex1_dataload_visualization.m) | Iris 로딩, 품종별 시각화, 학습·평가 데이터 구분 |
| 2 | [ex2_knn_using_matlab.m](ex2_knn_using_matlab.m) | 내장 함수 `fitcknn`과 `predict`로 두 품종 분류, k=3 |
| 3 | [ex3_knn_my_style.m](ex3_knn_my_style.m) | 거리 계산·정렬·다수결을 직접 구현하고 내장 함수와 비교 |
| 4 | [ex4_knn_generalization.m](ex4_knn_generalization.m) | 특징 4개와 품종 3개로 확장, k=5 |
| 5 | [ex5_knn_space.m](ex5_knn_space.m) | 두 특징의 격자 공간에서 KNN 분류 영역 시각화, k=50 |

각 스크립트는 필요한 데이터를 직접 불러오므로 독립 실행할 수 있습니다.
마지막 공간 시각화는 많은 격자점과 학습 데이터의 거리를 반복 계산하므로 앞선 예제보다 오래 걸릴 수 있습니다.

## 핵심 개념

1. 새 데이터와 기존 학습 데이터 사이의 거리를 구합니다.
2. 가장 가까운 k개 이웃을 선택합니다.
3. 이웃의 정답 품종 중 최빈값으로 분류합니다.

KNN의 k는 참고할 이웃 수입니다. K-means의 K는 만들 군집 수이므로 구분합니다.
특징이 연속형이어도 예측할 정답이 품종이면 분류입니다.

## 데이터 열

| 열 | 특징 |
| --- | --- |
| 1 | Sepal length · 꽃받침 길이 |
| 2 | Sepal width · 꽃받침 너비 |
| 3 | Petal length · 꽃잎 길이 |
| 4 | Petal width · 꽃잎 너비 |

MATLAB과 Statistics and Machine Learning Toolbox에서 실행합니다.
