import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk, ellipe

# 常量定义
mu0 = 4 * np.pi * 1e-7  # 真空磁导率 (T·m/A)
R = 1.0  # 电流环半径 (m)
I = 0.001  # 电流 (A)


def calculate_Bx_Bz(R, I, x, z):
    """
    计算 xz 平面上某点 (x, z) 的磁场分量 Bx 和 Bz
    """
    D = R ** 2 + x ** 2 + z ** 2
    numerator = 4 * R * np.abs(x)  # 绝对值避免负k^2
    denominator = D + 2 * R * x
    k_sq = numerator / denominator if denominator != 0 else 0

    # 处理特殊情况：x=0（轴线上）
    if x == 0:
        Bx = 0.0
        Bz = (mu0 * I * R ** 2) / (2 * (R ** 2 + z ** 2) ** (3 / 2))
        return Bx, Bz

    # 处理 k^2 超出椭圆积分定义域的情况
    if k_sq >= 1 or k_sq <= 0:
        return 0.0, 0.0

    alpha = np.sqrt(D - 2 * R * x)
    K = ellipk(k_sq)
    E = ellipe(k_sq)

    # 计算 Bx 和 Bz
    Bx = (mu0 * I * z) / (4 * np.pi * R * x * alpha) * ((D + R * x) * E - (D - R * x) * K)
    Bz = (mu0 * I) / (4 * np.pi * alpha ** 3) * ((D + R ** 2 - x ** 2) * E - (D - R ** 2 - x ** 2) * K)

    return Bx, Bz


# 生成网格点
x = np.linspace(-5 * R, 5 * R, 30)
z = np.linspace(-5 * R, 5 * R, 30)
X, Z = np.meshgrid(x, z)

# 计算磁场分量
Bx = np.zeros_like(X)
Bz = np.zeros_like(Z)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Bx[i, j], Bz[i, j] = calculate_Bx_Bz(R, I, X[i, j], Z[i, j])

# 绘制矢量场
plt.figure(figsize=(10, 8))
plt.quiver(X, Z, Bx, Bz, color='blue', scale=1e5, width=0.003)
plt.streamplot(X, Z, Bx, Bz, color='red', linewidth=1, density=2)

# 标记电流环位置
theta = np.linspace(0, 2 * np.pi, 100)
plt.plot(R * np.cos(theta), R * np.sin(theta), 'k-', linewidth=2)

# 图像标注
plt.xlabel('x (m)', fontsize=12);
plt.ylabel('z (m)', fontsize=12);
plt.title('Magnetic Field of a Circular Current Loop in xz-plane', fontsize=14);
plt.grid(True);
plt.axis('equal');
plt.show()