import numpy as np
# aa = np.arange(0,12).reshape((3,4))
# print(aa)

# 最大最小值
# 以下的函数都支持  aixs参数  等于1 对行进行  等于 0 就是 对列进行运算
# print(np.argmin(aa,aixs=0))
#
# print(np.argmax(aa))
# 平均数的两种写法

# print(np.mean(aa))
# print(np.average(aa))
# #中间数
# print(np.median(aa))
# # 累加
# print(np.cumsum(aa))
# # 累差
# print(np.diff(aa))
#非0数
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
0
11
如果值不是0则输出行列索引 一一对应  是0 就不输出
(array([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
"""
# print(np.nonzero(aa))
# 排序

aa = np.arange(12,0,-1).reshape((3,4))
print(aa)

# 排序 是 每行 单独 按升序排列
# print(np.sort(aa))
# help(np.nonzero)
# 反向转换  行变成列了
# print(np.transpose(aa))
# print((aa.T).dot(aa))
# 数列中 所有大于9的数 都变成9 小于5 的数 变成5 中间值不变
# print(np.clip(aa,5,9))
# print(np.clip(aa,5,9))