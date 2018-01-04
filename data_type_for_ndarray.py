# -*- coding:utf-8 -*-

import numpy as np

print("生成数组时指定数据类型")
arr = np.array([1,2,3],dtype=np.float64)
print(arr.dtype)
arr1 = np.array([1,2,3],dtype=np.int32)
print(arr1.dtype)

# chararray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
# dtype:str or dtype
print("使用astype 复制数组并转换数据类型")
int_arr = np.array([1,2,3,4,5])
float_arr = int_arr.astype(np.float)
print(int_arr.dtype)
print(float_arr.dtype)

print('使用astype 将float类型转换成int时小数部分被舍弃')
float_arr1 = np.array([3.7,4.8,5.9,2.1,-1.2,12.9])
int_arr1 = float_arr1.astype(dtype=np.int)
print(int_arr1)
print(int_arr1.dtype)

print('使用astype 把字符串转换成数字，如果失败抛异常')
str_arr = np.array(['1.25','-9.6','0.3','123','10.1'],dtype=np.string_)
str_arr2 = np.array(['abc','-9.6','0.3','123','10.1'],dtype=np.string_)
float_arr2 = str_arr.astype(dtype=np.float)
# float_arr3 = str_arr2.astype(dtype=np.float) # 这句代码会报错
print(float_arr2)
# print(float_arr3)

print('astype 使用其他数组的数据类型作为参数')
int_arr2 = np.arange(20)
print(int_arr2)
float_arr4 = np.array([.23,0.270,.357,0.44,0.5],dtype=np.float64)
print(int_arr2.astype(float_arr4.dtype))
print(int_arr2)
print(int_arr2[0],int_arr2[1])

'''
NumPy ndarray  数据类型
int8,uint8 -i1,u1               有/无符号的8位整型
int16,uint16 -i2,u2             有/无符号的16位整型
int32,uint32 -i4,u4             有/无符号的32位整型
int64,uint64 -i8,u8             有/无符号的64位整型
float16 - f2                    半精度浮点数
float32 - f4 or f               标准的单精度浮点数，与C的float兼容
float64 - f8 or d               标准的双精度浮点数，与C的double，python的float兼容
float128 - f16 or g             扩展精度浮点数
complex64/128/256 - c8/16/32    分别用64/128/256位的浮点数表示的复数
bool - ?                        存储Ture/False 值的布尔类型
object - O                      Python 对象类型
string_ - S                     固定长度的字符串类型。S 10 表示长度为10的字符串
unicode_ - U                    固定长度的unicode类型


输出：
生成数组时指定数据类型
float64
int32
使用astype 复制数组并转换数据类型
int32
float64
使用astype 将float类型转换成int时小数部分被舍弃
[ 3  4  5  2 -1 12]
int32
使用astype 把字符串转换成数字，如果失败抛异常
[   1.25   -9.6     0.3   123.     10.1 ]
astype 使用其他数组的数据类型作为参数
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.
  15.  16.  17.  18.  19.]
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
0 1
'''