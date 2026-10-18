"""
한글 폰트 설정 및 시각화 테스트 모듈
------------------------------------
Matplotlib 차트 출력 시 한글 깨짐 및 마이너스(-) 부호 깨짐 현상을 해결하기 위한 유틸리티 모듈입니다.
운영체제(Windows, macOS, Linux)를 자동으로 감지하여 적절한 한글 폰트를 설정합니다.

사용 예시:
    from font import set_korean_font
    set_korean_font()
"""

import platform
import matplotlib.pyplot as plt


def set_korean_font(font_family: str | None = None) -> str:
    """
    Matplotlib 전역 설정(rcParams)에 한글 폰트와 마이너스 부호 옵션을 적용합니다.

    Args:
        font_family (str, optional): 사용할 폰트 이름.
                                     None일 경우 실행 중인 운영체제에 맞춰 기본 한글 폰트를 자동 지정합니다.

    Returns:
        str: 최종 적용된 폰트 이름
    """
    # 1. 이전 설정의 간섭을 없애기 위해 Matplotlib 설정을 기본값으로 초기화
    plt.rcParams.update(plt.rcParamsDefault)

    # 2. 한글 폰트 적용 시 마이너스(-) 부호가 깨져 네모(□)로 표시되는 문제 방지
    plt.rcParams['axes.unicode_minus'] = False

    # 3. 폰트명이 전달되지 않은 경우 운영체제(OS) 환경에 알맞은 기본 한글 폰트 자동 선택
    if font_family is None:
        os_name = platform.system()
        if os_name == 'Darwin':
            # macOS 기본 한글 폰트
            font_family = 'AppleGothic'
        elif os_name == 'Windows':
            # Windows 기본 한글 폰트
            font_family = 'Malgun Gothic'
        else:
            # Linux 및 기타 환경 (구글 Noto Sans 한글 폰트)
            font_family = 'Noto Sans CJK KR'

    # 4. 선택된 폰트를 기본 폰트 패밀리로 지정
    plt.rcParams['font.family'] = font_family

    # 5. sans-serif 계열의 대체 폰트(fallback) 목록 구성 (지정 폰트 부재 시 대비)
    plt.rcParams['font.sans-serif'] = [font_family, 'DejaVu Sans', 'sans-serif']

    return font_family


def test_plot() -> None:
    """
    한글 제목, 축 레이블, 범례 및 음수 부호가 정상적으로 출력되는지 확인하는 테스트 차트를 생성합니다.
    """
    # X축: 0부터 49까지의 정수 (50개)
    x = list(range(50))
    # Y축: -25부터 24까지의 정수 (마이너스 부호 정상 출력 여부 검증용)
    y = [val - 25 for val in x]

    # 그래프 캔버스 크기 설정 (가로 8인치, 세로 4인치)
    plt.figure(figsize=(8, 4))

    # 빨간색 실선으로 데이터 플롯 및 범례 라벨 지정
    plt.plot(x, y, color='red', label='변동폭')

    # 차트 요소별 한글 텍스트 지정
    plt.title('가격변동 추이 (한글 폰트 테스트)')
    plt.xlabel('시간 (일)')
    plt.ylabel('가격 변동량')

    # 가독성을 높이기 위한 그리드(격자) 표시
    plt.grid(True, linestyle='--', alpha=0.5)

    # 범례 표시
    plt.legend()

    # 여백 자동 조정
    plt.tight_layout()

    # 그래프 창 화면 출력
    plt.show()


# 본 스크립트가 모듈로 import되지 않고 단독 실행될 때만 아래 테스트 코드 수행
if __name__ == '__main__':
    # 한글 폰트 설정 실행
    selected_font = set_korean_font()
    print(f"적용된 한글 폰트: {selected_font}")

    # 한글 및 마이너스 렌더링 테스트 차트 표시
    test_plot()


