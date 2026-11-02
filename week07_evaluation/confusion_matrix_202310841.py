# 인공지능개론 7주차(성능평가) 27페이지 과제
# 이진 분류 성능평가 프로그램
# TP = True Positive: 실제 양성, 예측 양성
# FP = False Positive: 실제 음성, 예측 양성
# FN = False Negative: 실제 양성, 예측 음성
# TN = True Negative: 실제 음성, 예측 음성


def read_count(name):
    """혼동행렬의 개수를 0 이상의 정수로 입력받는다."""
    while True:
        try:
            value = int(input(f"{name} 값을 입력하세요 (0 이상의 정수): "))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("0 이상의 정수를 입력해주세요.")


def divide(numerator, denominator):
    """분모가 0인 지표는 정의되지 않으므로 None을 반환한다."""
    if denominator == 0:
        return None
    return numerator / denominator


def percent(value):
    if value is None:
        return "정의되지 않음 (분모 0)"
    return f"{value:.2%}"


def main():
    # 혼동행렬 값: 고정된 숫자 대신 사용자 입력을 사용한다.
    while True:
        TP = read_count("TP")
        FP = read_count("FP")
        FN = read_count("FN")
        TN = read_count("TN")

        # 전체 데이터 수
        N = TP + FP + FN + TN
        if N > 0:
            break
        print("전체 데이터 수가 0입니다. 네 값을 다시 입력해주세요.\n")

    # 1. 정확도 Accuracy: 전체 중 올바르게 예측한 비율
    accuracy = (TP + TN) / N

    # 2. 민감도 Sensitivity / Recall: 실제 양성 중 양성으로 예측한 비율
    sensitivity = divide(TP, TP + FN)

    # 3. 특이도 Specificity: 실제 음성 중 음성으로 예측한 비율
    specificity = divide(TN, TN + FP)

    # 4. 정밀도 Precision / PPV: 양성 예측 중 실제 양성인 비율
    precision = divide(TP, TP + FP)

    # 5. 음성예측도 NPV: 음성 예측 중 실제 음성인 비율
    npv = divide(TN, TN + FN)

    # 6. F1-score
    # 강의식: 2 * precision * sensitivity / (precision + sensitivity)
    # 이를 TP, FP, FN으로 정리한 동치식을 사용해 0으로 나누는 경우를 구분한다.
    f1_score = divide(2 * TP, 2 * TP + FP + FN)

    # 7. 오분류율 Error Rate: 전체 중 잘못 예측한 비율
    error_rate = (FP + FN) / N

    print("\n========== 혼동행렬 ==========")
    print("              실제 +   실제 -")
    print(f"예측 +       {TP:8d} {FP:8d}")
    print(f"예측 -       {FN:8d} {TN:8d}")
    print(f"전체 데이터 수 N: {N}")

    print("\n========== 성능 평가 ==========")
    print(f"정확도 Accuracy       : {percent(accuracy)}")
    print(f"민감도 Sensitivity    : {percent(sensitivity)}")
    print(f"특이도 Specificity    : {percent(specificity)}")
    print(f"정밀도 Precision      : {percent(precision)}")
    print(f"음성예측도 NPV        : {percent(npv)}")
    print(f"F1-score              : {percent(f1_score)}")
    print(f"오분류율 Error Rate   : {percent(error_rate)}")

    print("\n========== 오류 해석 ==========")
    print(f"FP(False Positive) = {FP}")
    print("→ 실제 음성을 양성으로 잘못 판단")
    print("→ 질병 검사에서는 불필요한 검사나 처치 등의 비용 발생 가능")
    print()
    print(f"FN(False Negative) = {FN}")
    print("→ 실제 양성을 음성으로 잘못 판단")
    print("→ 질병 검사에서는 질병이나 이상을 놓치는 위험 발생 가능")


if __name__ == "__main__":
    main()
