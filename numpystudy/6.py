import numpy as np


aa = np.arange(4)

print(aa)

b= aa

c= aa

d =aa

aa[0]=11

print(aa)
print(c)

print(aa is d)
# 深拷贝 e的  值 改变 不会 影响到aa的值
e = aa.copy()