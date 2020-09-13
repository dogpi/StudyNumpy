import numpy as np
# 创建一个二维数组
# 第一维度中每个元素都是一维数组
# 第二维度每个元素都是int32类型
x = np.array([[1,2,3],[4,5,6]],np.int32)
print(type(x))      # <class 'numpy.ndarray'>



print(x[1,2])       # 6

y = x[:,1]          # 第一维度所有项的第二维度的第一项
print(y)            # [2 5]

y[0] = 9
print(x)            # [[1 9 3]
                    #  [4 5 6]]

print(x.shape)      # 数组维度元组(2, 3)

print(x.dtype)      # 数组元素类型int32

print(x.flags)      # 数组内存布局信息

print(x.strides)    # 遍历数组时每个维度中的字节元组（12,4）

print(x.ndim)       # 数组维度2

print(x.data)       # python缓冲区对象指向数组的数据的开头

print(x.size)       # 数组中的元素数6

print(x.itemsize)   # 一个数组元素的长度，以字节为单位4

print(x.nbytes)     # 数组元素消耗的总字节数24

print(x.base)       # 如果内存来自其他对象，则为基类对象None

print(x.T)          # 转置数组[[1 4]
                    #         [9 5]
                    #         [3 6]]

print(x.real)       # 数组的真实部分

print(x.imag)       # 数组的虚部

print(x.flat)       # 数组上的一维迭代器

print(x.ctypes)     # 一个简化数组与ctypes模块交互的对象