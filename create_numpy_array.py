import numpy as np

data1 = [1,2,3,4]
data2 = [1,2.3,4.5,2]
data3 = [3.2,3.6,2.9,1.02]
data4 = [1,2,'a','b',3]
data5 = [1,2,3.4,2.3,'a','e']


data6 = [[1,2,3],[3,4,5],[3,5,7]]
data7 = [[1,2,3,4],[5,6,7,8]]
data8 = [[1,2,3],[9,7,20,10,2,3,1]]
data9 = [[1,2],[1,2,3],[3,4,5,6]]
data10 = [[1,2,'e',2.3,'c',5.6],['a',9.8,'b',1,3,2.5]]
data11 = [[1,2,3],['a','b'],[9.3,2.4]]
data12 = [[1,2.3,'a'],[12,34,2.5,'a',3.2,'abc']]
data13 = [['a','b','c'],['e','f','g']]
data14 = [['abc','cde'],['efg','fgh']]
data15 = [['ab','cde'],['efgh','ijkmn']]


arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)
arr4 = np.array(data4)
arr5 = np.array(data5)
arr6 = np.array(data6)
arr7 = np.array(data7)
arr8 = np.array(data8)
arr9 = np.array(data9)
arr10 = np.array(data10)
arr11= np.array(data11)
arr12= np.array(data12)
arr13= np.array(data13)
arr14= np.array(data14)
arr15= np.array(data15)


#dtype 表示数组中元素的数据类型
print('arr1 is: ', arr1)
print('arr1 dtype is: ',arr1.dtype)

print('arr2 is: ', arr2)
print('arr2 dtype is: ',arr2.dtype)

print('arr3 is: ', arr3)
print('arr3 dtype is: ',arr3.dtype)

print('arr4 is: ', arr4)
print('arr4 dtype is: ',arr4.dtype)

print('arr5 is: ', arr5)
print('arr5 dtype is: ',arr5.dtype)


print('arr6 is: ', arr6)
print('arr6 dtype is: ',arr6.dtype)
#数组维度---表示矩阵的行和列
print('arr6 shape: ',arr6.shape)

print('arr7 is: ', arr7)
print('arr7 dtype is: ',arr7.dtype)
print('arr7 shape: ',arr7.shape)

print('arr8 is: ', arr8)
print('arr8 dtype is: ',arr8.dtype)
print('arr8 shape: ',arr8.shape)

print('arr9 is: ', arr9)
print('arr9 dtype is: ',arr9.dtype)
print('arr9 shape: ',arr9.shape)

print('arr10 is: ', arr10)
print('arr10 dtype is: ',arr10.dtype)
print('arr10 shape: ',arr10.shape)

print('arr11 is: ', arr11)
print('arr11 dtype is: ',arr11.dtype)
print('arr11 shape: ',arr11.shape)

print('arr12 is: ', arr12)
print('arr12 dtype is: ',arr12.dtype)
print('arr12 shape: ',arr12.shape)


