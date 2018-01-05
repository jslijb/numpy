# -*- coding:utf-8 -*-
import numpy as np

arr = np.array([1,2,3,8,0,2])
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,22,33],[44,55,66],[77,88,99]],[[111,222,333],[444,555,666],[777,888,999]]])
arr3 = np.array([[[1,2],[3,4],[6,7],[21,31]],[[11,22],[147,258],[10,20],[34,35]],[[9,0],[123,456],[101,202],[20,42]]])


print('arr: ',arr)
# 输出arr 一维数组 第1个元素和第二个元素
print('arr[0]: ',arr[0],'\t','arr[1]: ',arr[1])
# 输出arr1 二维数组 3行3列
print('arr1: ','\n',arr1)
# 输出arr1 第3行的所有元素，是个一维数组
print('arr1[2]','\n',arr1[2])
print('arr1[2] type: ',type(arr1[2]))
# 输出arr1 第一行和第二行 所有的元素，结果是二维数组，维度：2*3
print('arr1[:2]: ','\n',arr1[:2])
# 输出arr1 第1行到第二行，第1列到第2列
print('arr1[1:,:2]: ','\n',arr1[1:,:2])
# 输出arr1 第1列到第2列所有的元素
print('arr1[:,:2]: ','\n',arr1[:,:2])
# 输出arr1 第二行第3列的元素
print('arr1[1,2]: ','\n',arr1[1,2])
# arr1[1,2] type ---> numpy int32
print(type(arr1[1,2]))

print('arr2: ',arr2)
print('arr2 shape: ','\n',arr2.shape)
print('arr2[1:,:2]: ','\n',arr2[1:,:2])
print('arr2[1,2,1]: ','\n',arr2[1,2,1])
print('arr2[0]: ','\n',arr2[0])
print('arr2[0] type: ',type(arr2[0]))
# 复制 arr2[1] 的值
old_values = arr2[1].copy()
print('old_values: ','\n',old_values)
print('old_values type is: ',type(old_values))
# 给arr2[1] 中所有元素赋值42
arr2[1] = 42
print('new arr2 value: ','\n',arr2)
# 还原 arr2[1] 的值
arr2[1] = old_values
print('newest arr2 value: ','\n',arr2)
old_values_0 = arr2[0].copy()
print('old_values_0 :','\n',old_values_0)
arr2[0] = [10,20,30]
print('update arr2[0]: ','\n',arr2)
# arr2[2] = [[123,234,345],[80,90,100]]  # 这个会报错
arr2[2] = [[123,234,345]]
print('update arr2[2]: ','\n',arr2)
arr2[2] = [[198,203,190],[203,301,201],[901,801,701]]
print('update arr[2] 1*3: ','\n',arr2)
print('arr3: ','\n',arr3)
print('arr3 shape is: ',arr3.shape)
print('arr3[0]: ','\n',arr3[0])
print('arr3[0,1]: ','\n',arr3[0,1])
print('arr3[:,3,:]: ','\n',arr3[:,3,:])
print('arr3[:2,3:,1:]: ','\n',arr3[:2,2:,1:])
print('arr3[2,2,1]: ',arr3[2,2,1])
print(type(arr3[2,2,1]))

'''
输出
arr:  [1 2 3 8 0 2]
arr[0]:  1 	 arr[1]:  2
arr1:  
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
arr1[2] 
 [7 8 9]
arr1[2] type:  <class 'numpy.ndarray'>
arr1[:2]:  
 [[1 2 3]
 [4 5 6]]
arr1[1:,:2]:  
 [[4 5]
 [7 8]]
arr1[:,:2]:  
 [[1 2]
 [4 5]
 [7 8]]
arr1[1,2]:  
 6
<class 'numpy.int32'>
arr2:  [[[  1   2   3]
  [  4   5   6]
  [  7   8   9]]

 [[ 11  22  33]
  [ 44  55  66]
  [ 77  88  99]]

 [[111 222 333]
  [444 555 666]
  [777 888 999]]]
arr2 shape:  
 (3, 3, 3)
arr2[1:,:2]:  
 [[[ 11  22  33]
  [ 44  55  66]]

 [[111 222 333]
  [444 555 666]]]
arr2[1,2,1]:  
 88
arr2[0]:  
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
arr2[0] type:  <class 'numpy.ndarray'>
old_values:  
 [[11 22 33]
 [44 55 66]
 [77 88 99]]
old_values type is:  <class 'numpy.ndarray'>
new arr2 value:  
 [[[  1   2   3]
  [  4   5   6]
  [  7   8   9]]

 [[ 42  42  42]
  [ 42  42  42]
  [ 42  42  42]]

 [[111 222 333]
  [444 555 666]
  [777 888 999]]]
newest arr2 value:  
 [[[  1   2   3]
  [  4   5   6]
  [  7   8   9]]

 [[ 11  22  33]
  [ 44  55  66]
  [ 77  88  99]]

 [[111 222 333]
  [444 555 666]
  [777 888 999]]]
old_values_0 : 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
update arr2[0]:  
 [[[ 10  20  30]
  [ 10  20  30]
  [ 10  20  30]]

 [[ 11  22  33]
  [ 44  55  66]
  [ 77  88  99]]

 [[111 222 333]
  [444 555 666]
  [777 888 999]]]
update arr2[2]:  
 [[[ 10  20  30]
  [ 10  20  30]
  [ 10  20  30]]

 [[ 11  22  33]
  [ 44  55  66]
  [ 77  88  99]]

 [[123 234 345]
  [123 234 345]
  [123 234 345]]]
update arr[2] 1*3:  
 [[[ 10  20  30]
  [ 10  20  30]
  [ 10  20  30]]

 [[ 11  22  33]
  [ 44  55  66]
  [ 77  88  99]]

 [[198 203 190]
  [203 301 201]
  [901 801 701]]]
arr3:  
 [[[  1   2]
  [  3   4]
  [  6   7]
  [ 21  31]]

 [[ 11  22]
  [147 258]
  [ 10  20]
  [ 34  35]]

 [[  9   0]
  [123 456]
  [101 202]
  [ 20  42]]]
arr3 shape is:  (3, 4, 2)
arr3[0]:  
 [[ 1  2]
 [ 3  4]
 [ 6  7]
 [21 31]]
arr3[0,1]:  
 [3 4]
arr3[:,3,:]:  
 [[21 31]
 [34 35]
 [20 42]]
arr3[:2,3:,1:]:  
 [[[ 7]
  [31]]

 [[20]
  [35]]]
arr3[2,2,1]:  202
<class 'numpy.int32'>
'''
