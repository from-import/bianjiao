import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'SimHei', 'size': 12}
plt.rc('font', **font)
plt.rcParams['axes.unicode_minus'] = False  # 禁用Unicode负号

mr = 0.5  # s
a = 1  # 1
b = 1e-6  # 1e-6
p = 206265  # 206265

S = np.linspace(0, 1800, 100)  # 假设距离范围为0到1800m

mu = (mr * S * 1000) / p
mL = np.sqrt(a**2 + (1000 * b * S)**2)

plt.figure(figsize=(8, 6))
plt.plot(S, mu, label='mu')
plt.plot(S, mL, label='mL')
plt.plot(S, 0.001*S, linestyle='--', label='y=x')



plt.title('边角精度匹配分析(0.5*,1mm+1ppm*s)')
plt.xlabel('距离(m)')
plt.ylabel('横向/纵向误差(mm)')
plt.legend()
plt.grid(True)
plt.show()
