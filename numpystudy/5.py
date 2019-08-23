import numpy as np


aa = np.arange(12).reshape(3,4)

print(aa)
# 分割  第一个参数 是 分割对象  第二个参数 是分成 几部分 必须是 对等的  第三个参数 是 对列 进行分割
# print(np.split(aa,3,axis=1))

# 分割  第一个参数 是 分割对象  第二个参数 是分成 几部分 可以是  不 对等的  第三个参数 是 对列 进行分割
# print(np.array_split(aa,3,axis=1))

# 横向分割  纵向分割
print(np.vsplit(aa,3))
print(np.hsplit(aa,2))