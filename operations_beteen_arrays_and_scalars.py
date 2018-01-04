# -*- coding:utf-8 -*-

import numpy as np
# 数组之间的乘法 / 减法，对应元素的相乘 / 相减。需要两个数组的维度相同
arr1 = np.array([[1.0,2.0,3.0],[4,5,6]])
arr2 = np.array([[10,14,15],[9,8,12]])
arr3 = np.array([[2,7,5],[3,4,2]])
arr4 = np.array([[1,2,3.1],[2,3,4]])
arr5 = np.array([[1,2,3],[2,3,4],[3,4,5]])
arr6 = np.array([[1,2,3,4],[5,6,7,8]])

print('arr1 * arr2 = ',arr1*arr2)
print('arr1 - arr2 = ',arr1-arr2)
print('arr2 + arr3 = ',arr2 + arr3)
print('arr2 + arr4 = ',arr2 + arr4)
#虽然 arr2 和 arr3 中想对应的元素都能够整除，所得的结果任然是浮点数
print('arr2 / arr3 = ',arr2 / arr3)
print('arr2 / arr3 所得数组中元素的数据类型：',(arr2 / arr3).dtype)
print(arr3 / arr4)
print('arr3 / arr4 所得数组中元素的数据类型：',(arr3 / arr4).dtype)
#arr4 和 arr5 维度相同才能相加
#print(arr4 / arr5)

#arr4 arr6  两者维度不相同，会报错。行和列都相同才能计算
#print(arr4 + arr6)

#标量操作作用于数组中的每一个元素
arr7 = np.array([[1,2,3,4],[5,6,7,8]])
arr8 = np.array([[1.0,2.,3,4.2],[5.,6.2,7.3,8]])

print('2 / arr8 is: ',2/arr8)
print('40320 / arr7 is: ',40320/arr7)

# 输出
'''
arr1 * arr2 =  [[ 10.  28.  45.]
 [ 36.  40.  72.]]
arr1 - arr2 =  [[ -9. -12. -12.]
 [ -5.  -3.  -6.]]
arr2 + arr3 =  [[12 21 20]
 [12 12 14]]
arr2 + arr4 =  [[ 11.   16.   18.1]
 [ 11.   11.   16. ]]
arr2 / arr3 =  [[ 5.  2.  3.]
 [ 3.  2.  6.]]
arr2 / arr3 所得数组中元素的数据类型： float64
[[ 2.          3.5         1.61290323]
 [ 1.5         1.33333333  0.5       ]]
arr3 / arr4 所得数组中元素的数据类型： float64
s / arr8 is:  [[ 2.          1.          0.66666667  0.47619048]
 [ 0.4         0.32258065  0.2739726   0.25      ]]
s / arr7 is:  [[ 40320.  20160.  13440.  10080.]
 [  8064.   6720.   5760.   5040.]]
'''