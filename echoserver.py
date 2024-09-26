def calculate_bmi(weight, height):
    """
    計算 BMI 的函數
    :param weight: 體重（公斤）
    :param height: 身高（公尺）
    :return: BMI 值
    """
    if height <= 0:
        raise ValueError("身高必須大於 0")
    return weight / (height ** 2)

def main():
    try:
        weight = float(input("請輸入體重（公斤）："))
        height = float(input("請輸入身高（公尺）："))
        bmi = calculate_bmi(weight, height)
        print(f"你的 BMI 值為：{bmi:.2f}")
        
        if bmi < 18.5:
            print("體重過輕")
        elif 18.5 <= bmi < 24.9:
            print("體重正常")
        elif 25 <= bmi < 29.9:
            print("體重過重")
        else:
            print("肥胖")
    except ValueError as e:
        print(f"輸入錯誤：{e}")

if __name__ == "__main__":
    main()