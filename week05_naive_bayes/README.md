# 5주차 · 확률 기반 인공지능: Naive Bayes

꽃받침 길이 하나로 Setosa와 Versicolor를 분류합니다.

## 파일

[ex_naive_bayes_202310841.m](ex_naive_bayes_202310841.m)

Current Folder를 이 폴더로 설정하고 스크립트 전체를 실행합니다.

```matlab
ex_naive_bayes_202310841
```

MATLAB과 Statistics and Machine Learning Toolbox가 필요합니다.

## 코드 흐름

1. Iris 중 Setosa·Versicolor 100개를 선택합니다.
2. 실제 품종을 0(Setosa), 1(Versicolor)로 표현합니다.
3. `fitcnb`와 `predict`로 내장 모델의 결과를 구합니다.
4. 품종별 사전확률, 꽃받침 길이의 평균·표준편차를 구합니다.
5. 관측한 길이를 품종별 정규분포 확률밀도함수에 대입합니다.
6. 각 품종의 '우도 × 사전확률'을 비교해 `my_result`를 구합니다.
7. `Training_label`과 `my_result`를 비교해 정확도를 계산합니다.

## 정확도 과제

```matlab
correct_idx = find(Training_label == my_result);
num_correct = length(correct_idx);
num_total = length(Training_label);
accuracy = num_correct / num_total;
```

이전 MATLAB 실행에서 확인한 결과:

| 항목 | 값 |
| --- | --- |
| 맞힌 개수 | 89개 |
| 전체 개수 | 100개 |
| 정확도 | 89.00% |

이는 학습에 사용한 데이터를 다시 평가한 정확도이며, 별도 테스트 데이터에 대한 정확도는 아닙니다.
이번 저장소 정리 과정에서 MATLAB 실행으로 재측정한 결과는 아닙니다.

## 개념 구분

- 사전확률: 길이를 보기 전 각 품종의 비율.
- 우도: 해당 품종이라고 가정했을 때 관측 길이의 확률밀도.
- 사후확률: 길이를 확인한 뒤 각 품종일 확률.
- 분류할 때는 공통 분모를 생략하고 '우도 × 사전확률'만 비교할 수 있습니다.

코드와 주석은 업로드한 과제 형태를 유지했습니다.
