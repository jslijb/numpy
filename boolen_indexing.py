# -*- coding:utf-8 -*-

import numpy as np
import numpy.random as np_random
name_arr = np.array(['Bob','Joe','Will','Bob','Joe','Bill','Joe'])
ndr_arr = np_random.rand(7,4)
print('name_arr is: ',name_arr)
'''
输出：name_arr is:  ['Bob' 'Joe' 'Will' 'Bob' 'Joe' 'Bill' 'Joe']

'''
print('ndr_arr: ','\n',ndr_arr)
'''
输出 7行4列二维数组。每个元素都是一个随机值
ndr_arr:  
 [[ 0.26236941  0.99325476  0.73899847  0.28867581]
 [ 0.02813794  0.66985577  0.47357807  0.78385717]
 [ 0.90752759  0.34890763  0.34638289  0.33341022]
 [ 0.27209486  0.06409603  0.15717144  0.6987891 ]
 [ 0.34705623  0.82653803  0.25818207  0.61585622]
 [ 0.04089236  0.88197284  0.61451966  0.76919174]
 [ 0.70830169  0.07373122  0.94111699  0.13982623]]

'''
# name_arr 中元素等于 'Bob' 返回True，否则False。输出的是布尔数组，所有的元素的值:True/False 就只有这两个值
print('boolen arrar: ',name_arr == 'Bob')
# 获取上一个数组中为True的元素对应的索引，这个数组中只打印这些索引的行
# 上一个数组：[True False False  True False False False]
# 这样只打印ndr_arr 这个数组的第1行和第4行，其他的行不打印，过滤掉
# 使用布尔数组可以选择所需要的行
'''
输出：
boolen arrar:  [ True False False  True False False False]
'''
# ndr_arr的行数 和 布尔数组的列数 相等
print('ndr_arr index boolen: ','\n',ndr_arr[name_arr == 'Bob'])
'''
输出：
 ndr_arr index boolen:  
 [[ 0.26236941  0.99325476  0.73899847  0.28867581]
 [ 0.27209486  0.06409603  0.15717144  0.6987891 ]]
'''
# 在布尔数组的基础上还可以分片，过滤列
print('ndr_arr index boolen and split: ','\n',ndr_arr[name_arr == 'Bob',:2])
'''
输出：
 ndr_arr index boolen and split:  
 [[ 0.26236941  0.99325476]
 [ 0.27209486  0.06409603]]
'''
# 取反 ~(pattern) == expression 或者 pattern != expression
#  ndr_arr[~(name_arr == 'Bob')] = ndr_addr[name_arr != 'Bob'
print('ndr_arr index boolen and take back: ','\n',ndr_arr[~(name_arr == 'Bob')])
print('ndr_arr index boolen and logic not: ','\n',ndr_arr[name_arr != 'Bob'])
# 做逻辑或操作
mask_arr = (name_arr =='Bob') | (name_arr == 'Joe')
print('mask_arr: ','\n',mask_arr)
print('ndr_arr[mask_arr]: ','\n',ndr_arr[mask_arr])
# 这种赋值方式是赋值的引用，而不是值，ndr_arr 和 ndr_arr1 指向同一个内存地址
ndr_arr1 = ndr_arr
print('id(ndr_arr): ',id(ndr_arr))
print('id(ndr_arr1): ',id(ndr_arr1))
print('ndr_arr1: ',ndr_arr1)
# 这里改变的值，而不是引用，ndr_arr 和 ndr_arr1 引用没有发生变化，所以ndr_arr 和 ndr_arr1 值都发生了变化
ndr_arr[name_arr == 'Joe'] = 7
print('ndr_arr is: ',ndr_arr)
print('ndr_arr1 is: ',ndr_arr1)
print('id(ndr_arr): ',id(ndr_arr))
print('id(ndr_arr1): ',id(ndr_arr1))

# copy 的方式新生成一个数组，把旧数组的值复制到新数组中，而且两个数组在内存中第地址不一样
# 两个数组的值一样，但是引用不一样
ndr_arr2 = ndr_arr.copy()
print("id(ndr_arr): ",id(ndr_arr))
print("id(ndr_arr2): ",id(ndr_arr2))
print('ndr_arr: ',ndr_arr)
print('ndr_arr2: ',ndr_arr2)
ndr_arr[name_arr == 'Joe'] = [1,2,3,4]
# 此时ndr_arr ndr_arr2 这两个数组的值不一样，ndr_arr 的值发生变化，而ndr_addr2 的值没有发生变化
print('ndr_arr: ',ndr_arr)
print('ndr_arr2: ',ndr_arr2)
ndr_arr1[name_arr == 'Joe'] = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
# 无论是修改ndr_arr 还是修改ndr_arr1 这两个数组的值始终保持一致，因为两者的内存地址始终保持一致
print("ndr_arr1: ","\n",ndr_arr1)
print("ndr_arr: ","\n",ndr_arr)