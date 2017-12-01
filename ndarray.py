#coding:utf-8
import numpy as np

a = np.array([[-3,-2,-1,0,]])
b = np.array([[1,2,3,4,], [5,6,7,8,]])
#print np.array([-3,-2,-1,0,]).shape
print type(a), '\n', a, a.shape
print type(b), '\n', b, b.shape
print '\n'

#select1 
#print b[:, 0]
#print b[:, 0].reshape(len(b[:, 0]), 1)
#print '\n'
#select2
#print b>6
#print b[b>6]

#3 modified
#b[b>5]=0
#print b

#4 vstack, hstack
#print np.vstack([a, b])
#print np.concatenate([a, b], axis=0)

#5 generate
#print np.arange(10)
#print np.arange(2, 8).reshape(2, 3)
#print np.arange(1, 100, 2).reshape(5,10)

#6 生成指定范围和个数的等差数列
#print np.linspace(0, 1, 4)
#10^1 ~ 10^3间, 含3个数的等比数列
#print np.logspace(1, 3, 3)

#7
#print np.ones((2,4))
#print np.zeros((3,4))
#print np.eye(4)
#print np.empty((4,5))

#8 一参数指定字符串, 获取其ASCII码, 二参数指定字符位数
#print np.fromstring('limingzhi', np.int8)

#9 一参数根据行列号生成矩阵元素, 二参数指定矩阵大小
#print np.fromfunction(lambda i,j: i+j, (4,5))

#10 
#print np.sin(a)
#print np.cos(a)
#print np.tan(a)
#print np.arcsin(a)
#print np.arccos(a)
#print np.arctan(a)
#print np.exp(a)
#print np.sqrt(a)

#11 *点乘, 数跟矩阵, 或两个矩阵的列相同或者其中一个列元素数为1
#print b*-2
#print type(a[:, 1:2])
#print a[:, 1:2] * b
#print '\n'
#12 矩阵的乘法
#print a[:, 1:3]
#print b
#print a[:, 1:3].dot(b)
#print '\n'
#print a[:, 1:3][0]
#print b
#print a[:, 1:3][0].dot(b)

#13 transpose 矩阵的转置
#print b
#print b.transpose()
#print b.T

#14 linalg 矩阵的逆
#c = np.concatenate(([[-7, -6, -5, -4]], np.vstack((a, b))), axis=0)
#print c
#print np.linalg.inv(c)
#print np.eye(4)
#print np.linalg.inv(np.eye(4))

#15
# 整个矩阵范围内的最大最小值
#print b.max()
#print b.min()
# 在行或列上的最大最小值
#print b.max(axis=0)
#print b.max(axis=1)
# 最大最小值在各组内的位置(序号从0开始)
#print b.argmax(axis=0)
#print b.argmax(axis=1)
# mean
#print b.mean()
#print np.mean(b)
#print b.mean(axis=0)
#print np.mean(b, axis=0)
#print b.mean(axis=1)
#print np.mean(b, axis=1)
# var
#print b.var()
#print np.var(b)
#print np.mean((b-b.mean())**2)
#print b.var(axis=0)
#print np.var(b, axis=0)
#print b.var(axis=1)
#print np.var(b, axis=1)
# std
#print b.std()
#print np.sqrt(np.mean(((b - b.mean()))**2))
#print b.std(axis=0)
#print b.std(axis=1)
# median
#print np.median(b)
#print np.median(b, axis=0)
#print np.median(b, axis=1)
# sum
#print b.sum()
#print b.sum(axis=0)
#print b.sum(axis=1)
# cumsum
#print b.cumsum()
#print b.cumsum(axis=0)
#print b.cumsum(axis=1)

d = np.arange(20).reshape(4, 5)
print d
print d.shape
print d.ndim
print d.size
print d.dtype
print d.itemsize
print d.data









