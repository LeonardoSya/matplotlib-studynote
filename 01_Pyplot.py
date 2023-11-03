"""
Pyplot是Matplotlib的子库, 提供与matlab类似的绘图api

import matplotlib.pyplot as plt

plot()：用于绘制线图和散点图
scatter()：用于绘制散点图
bar()：用于绘制垂直条形图和水平条形图
hist()：用于绘制直方图
pie()：用于绘制饼图
imshow()：用于绘制图像
subplots()：用于创建子图
"""

import numpy as np
import matplotlib.pyplot as plt

"""
plot()  绘制点和线
    单条线: plot([x], y, [fmt], *, data=None, **kwargs)
    多条线: plot([x], y, [fmt], [x2], [y2], [fmt2], ..., **kwargs)

x, y: 数据为列表或数组  x可选,当不设置x时会根据y的值设置为 0,1,2,...N-1
fmt(可选): 定义基本格式(颜色、标记、线条样式...)
**kwargs(可选): 用于在二维平面图上设置指定的属性 如标签、线的宽度等
"""

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

"""
fmt:
    颜色字符: 'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，
            '#008000' RGB 颜色符串
            多条曲线不指定颜色时，会自动选择不同颜色
    线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线
    标记字符：'.' 点标记，',' 像素标记(极小点) 'o' 实心圈标记 'v' 倒三角标记，'^' 三角标记，'>' 右三角标记 '<' 左三角标记
"""

xStep = np.arange(0, 10 * np.pi, 0.01)  # (start, stop, step)
ySin = np.sin(xStep)
yCos = np.cos(xStep)

plt.plot(xStep, ySin, "g", xStep, yCos, "r")
plt.show()
