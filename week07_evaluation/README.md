# 7주차 · 성능평가 과제

인공지능개론 7주차 강의자료 27페이지의 이진 분류 성능평가 프로그램을 완성했습니다.

## 제출 코드

[confusion_matrix_202310841.py](confusion_matrix_202310841.py)

- TP, FP, FN, TN을 사용자 입력으로 받습니다.
- 빈칸인 정확도, 민감도, 특이도, 정밀도, 음성예측도의 공식을 완성했습니다.
- F1-score와 오분류율을 함께 출력합니다.
- 외부 라이브러리 없이 Python 3에서 실행합니다.

## 실행

```bash
python confusion_matrix_202310841.py
```

TP, FP, FN, TN 순서로 0 이상의 정수를 입력합니다.
숫자가 아닌 값이나 음수는 다시 입력받습니다. 전체 데이터가 0개이면 네 값을 다시 입력받습니다.

## 혼동행렬 배치

| | 실제 양성 (+) | 실제 음성 (-) |
| --- | --- | --- |
| 예측 양성 (+) | TP | FP |
| 예측 음성 (-) | FN | TN |

## 지표 공식

N = TP + FP + FN + TN

| 지표 | 공식 |
| --- | --- |
| 정확도 Accuracy | (TP + TN) / N |
| 민감도 Sensitivity / Recall | TP / (TP + FN) |
| 특이도 Specificity | TN / (TN + FP) |
| 정밀도 Precision / PPV | TP / (TP + FP) |
| 음성예측도 NPV | TN / (TN + FN) |
| F1-score | 2 × Precision × Recall / (Precision + Recall) |
| 오분류율 Error Rate | (FP + FN) / N |

코드에서는 F1을 동치식 2TP / (2TP + FP + FN)으로 계산합니다.
각 지표의 분모가 0이면 '정의되지 않음 (분모 0)'으로 표시합니다.
예를 들어 TP=0, FP=0, FN>0이면 정밀도는 정의되지 않지만 F1의 개수 기반 분모는 양수이므로 F1은 0입니다.

## 강의 예시 실행 결과

입력: TP=450, FP=50, FN=50, TN=450

| 지표 | 결과 |
| --- | --- |
| 정확도 | 90.00% |
| 민감도 | 90.00% |
| 특이도 | 90.00% |
| 정밀도 | 90.00% |
| 음성예측도 | 90.00% |
| F1-score | 90.00% |
| 오분류율 | 10.00% |

이 예시와 비대칭 입력, 분모 0, 잘못된 입력 및 전체 0의 재입력을 실제 Python 실행으로 확인했습니다.

## 제출 방법

과제 코드의 GitHub 링크를 메모장에 복사해 .txt 파일로 저장하고, 해당 파일을 과제 제출란에 업로드합니다.

https://github.com/daehometa-dotcom/matlab_practice/blob/main/week07_evaluation/confusion_matrix_202310841.py
