"""
Author: LeonardoSya 2246866774@qq.com
Date: 2023-11-03 20:11:38
LastEditors: LeonardoSya 2246866774@qq.com
LastEditTime: 2023-11-03 20:32:20
FilePath: \matplotlib\02_标记和线.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""
"""
    给坐标自定义标记 plot()方法的 marker参数 marker支持定义大量的符号(参考文档)    
    
    fmt = '[marker][line][color]'  例如 o:r 实心圆虚线红色
    
    自定义标记的大小与颜色： 
        markersize(ms) 
        markerfacecolor(mfc)标记内部颜色
        markeredgecolor(mec)标记边框颜色
    
    linewidth(lw)
"""

import numpy as np

import matplotlib.pyplot as plt

ydata = np.array([1, 3, 4, 5, 8, 9, 6, 1, 3, 4, 5, 2, 4])

plt.plot(ydata, marker="o", ms=5, mfc="#da3729", mec="black", lw=2)
plt.plot(ydata**0.5)
plt.show()
