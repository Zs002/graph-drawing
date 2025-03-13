import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')  # 使用 TkAgg 后端

# 设置坐标轴和文字的样式
plt.style.use('default')  # 使用默认样式
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从 Excel 文件中读取数据
# 假设 Excel 文件中有三组数据，分别存储在三个工作表中
file_path = "G:\\xkj.xlsx"

# 读取每组数据
df1 = pd.read_excel(file_path, sheet_name='Sheet1')  # 第一组数据
df2 = pd.read_excel(file_path, sheet_name='Sheet2')  # 第二组数据
df3 = pd.read_excel(file_path, sheet_name='Sheet3')  # 第三组数据

# 假设 Excel 表格中，H 和 B 分别存储在 'H' 和 'B' 列
H1 = df1['H']  # 第一组 H 数据
B1 = df1['B']  # 第一组 B 数据

H2 = df2['H']  # 第二组 H 数据
B2 = df2['B']  # 第二组 B 数据

H3 = df3['H']  # 第三组 H 数据
B3 = df3['B']  # 第三组 B 数据

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制三组磁滞回线
plt.plot(H1, B1, label='Cr12', color='blue', linestyle='-', linewidth=1)
plt.plot(H2, B2, label='45#钢', color='red', linestyle='--', linewidth=1)
plt.plot(H3, B3, label='纯铁', color='green', linestyle='-.', linewidth=1)

# 添加标题和标签
plt.title('磁滞回线')
plt.xlabel('磁场强度 H (mA/m)')
plt.ylabel('磁感应强度 B (mT)')

# 添加网格
plt.grid(True)

# 显示图例
plt.legend()

# 显示图形
plt.show()

plt.clf()  # 清除之前的图形
# 嘿嘿
#不玩了下班

