import numpy as np

aa = np.arange(3,15).reshape(3,4)

print(aa)
# 多维索引 只有 一个索引的   就代表 每个内部单元的索引值
# 两个索引  第一个 维的所以  第二个 代表 是该单元的元素内部单元索引 以此类推
# print(aa[2][1])
# # print(aa[2,1])
# # print(aa[2,:])
# # print(aa[:,2])
# # print(aa[1,0:2])
# 循环每个行的元素
# for ro in aa:
#     print(ro)
# 把行变成列 进行迭代
# for ro in aa.T:
# #     print(ro)

# 把多维数组转换为一维的列表  返回 数组
# print(aa.flatten())
# 迭代每个 已转换的一维列表 flat 是一个迭代器
# for item in aa.flat:
#     print(item)