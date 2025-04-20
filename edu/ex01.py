# 구구단 출력 프로그램

def print_gugudan():
    """구구단 출력 함수"""
    for dan in range(1, 10):
        print(f"--- {dan}단 ---")  # 단 제목 출력
        for num in range(1, 10):
            print(f"{dan} x {num} = {dan * num}")
        print()  # 각 단 끝에 빈 줄 추가

if __name__ == "__main__":
    print_gugudan()
