# from numpystudy import *
# ano=eye(4)

# ano=array([[1., 0., 0., 0.],
# #        [0., 1., 0., 0.],
# #        [0., 0., 1., 0.],
# #        [0., 0., 0., 1.]])
# print(ano)

import numpy as np
# a = np.array([1,  2,  3], dtype = complex)
# a = np.array([1,  2,  3,4,5], ndmin =  2)
a = np.array([[1,2],[3,4]])
b = np.arange(4).reshape(2,2)
aa = np.array([1,  23,  4],dtype=np.float)
dd = np.zeros((3,4))
dd1 = np.ones((3,4),dtype=int)
dd3 = np.arange(10,20,2)
dd4 = np.arange(12).reshape((3,4))
dd5 = np.linspace(1,10,6).reshape((2,3))
# dd0 = np.empty()
# print (aa.dtype)
# print (a)
# print (dd)
# print (dd3)

dd6=np.array([10,20,30,40])
dd7=np.arange(4)
# print(dd6,dd7)
dd8=dd6-dd7
dd9=dd6+dd7
dd10=dd6*dd7
# print(dd8)
# print(dd9)
# print(dd10)
# print(dd7**2)
# print (dd5)

c = 10*np.sin(5)
# print(c)

# print(dd6<25)
# print(dd6==20)
#
# print(a)
# # print(b)
# # # print(a*b)
# numpystudy.dot() 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
# 对于二维数组，计算的是两个数组的矩阵乘积；对于多维数组，它的通用计算公式如下，即结果数组中的每个元素都是：
# 数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和： dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])。
# # yy =np.dot(a,b)
# # print(yy)

mm = np.random.random((2,4))
print(mm)

print(np.sum(mm,axis=0))
print(np.min(mm))
print(np.max(mm))