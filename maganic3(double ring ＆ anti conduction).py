import numpy as np
import matplotlib.pyplot as plt

# 常量定义
mu0 = 4 * np.pi * 1e-7  # 真空磁导率 (T·m/A)
R = 1.0                  # 线圈半径 (m)
I = 1.0                  # 电流强度 (A)
a = R                    # 线圈间距 (a = R 时为标准亥姆霍兹线圈)

def single_coil_Bz(z, coil_z):
    """计算单个线圈在位置 z 处的 Bz 分量"""
    return (mu0 * I * R**2) / (2 * (R**2 + (z - coil_z)**2)**(1.5))

def total_Bz(z):
    """计算两个反向电流线圈在 z 轴上的总 Bz"""
    Bz_upper = single_coil_Bz(z, coil_z=+a)  # 上侧线圈 (电流 +I)
    Bz_lower = -single_coil_Bz(z, coil_z=-a) # 下侧线圈 (电流 -I, 反向)
    return Bz_upper + Bz_lower

# 生成 z 轴上的点
z = np.linspace(-3*R, 3*R, 500)
Bz = np.array([total_Bz(zi) for zi in z])

# 绘制 Bz 随 z 的变化
plt.figure(figsize=(10, 6))
plt.plot(z, Bz, 'b-', linewidth=2, label='$B_z(z)$')
plt.axvline(x=+a, color='r', linestyle='--', label='Coil at $z=+a$')
plt.axvline(x=-a, color='r', linestyle='--', label='Coil at $z=-a$')
plt.axhline(y=0, color='k', linestyle=':')

# 标注
plt.xlabel('$z$ (m)', fontsize=12)
plt.ylabel('$B_z$ (T)', fontsize=12)
plt.title('Magnetic Field $B_z$ on the Axis of Anti-Helmholtz Coils', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()