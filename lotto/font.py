import matplotlib.pyplot as plt

# 기본 설정으로 재설정
plt.rcParams.update(plt.rcParamsDefault)

# 폰트 설정
plt.rcParams['font.family'] =  'Noto Sans CJK JP'
plt.rcParams['font.sans-serif'] = ['Noto Serif CJK JP']

# 임의의 데이터 생성
data = range(50)

plt.plot(range(50), data, 'r')
plt.title('가격변동 추이')
plt.ylabel('가격')
plt.show()
