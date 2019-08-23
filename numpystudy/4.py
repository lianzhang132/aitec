import numpy as np

aa = np.array([1,1,1])
aa1 = np.array([1,1,1])[:,np.newaxis]
bb = np.array([2,2,2])
bb1 = np.array([2,2,2])[:,np.newaxis]
# 合并数列  为多维的  上下

cc = np.vstack((aa,bb))
# 左右合并
dd = np.hstack((aa,bb))


# print(aa.shape,cc.shape)

# print(dd,dd.shape)

# print(aa.T)
# 在行 上加个维度
print(aa[np.newaxis,: ])
# 在列上加维度
print(aa[:,np.newaxis])

ee = np.concatenate((aa1,bb1,aa1),axis=1)
# print(ee)