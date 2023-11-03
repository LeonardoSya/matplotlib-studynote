import matplotlib.pyplot as plt

# plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.title("my title")
plt.show()

# *整个图像为一个Figure对象，Figure对象中可以包含多个Axes对象，每个ax对象都是一个拥有自己坐标系统的绘图区域
plt.figure(figsize=(6, 3))
plt.plot(6, 3)
plt.plot(3, 3 * 2)
plt.show()
