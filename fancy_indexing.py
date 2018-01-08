# -*- coding:utf-8 -*-

import numpy as np

# 生成一个9*9 二维数组，空数组，每个元素使用随机数填充
arr = np.empty((9,9))
# print('arr: ','\n',arr)
item = 0
for i in range(9):
    # 数组中每一行都设置为同一个值
    for j in range(9):
        arr[i,j] = item
        item += 1
print('arr: ','\n',arr)
'''
输出：
arr:  
 [[  2.49260831e-306   1.10894291e-296   4.22979968e-307   1.62598065e-260
    2.99484325e+262   6.11246463e+228   1.17233372e+214   9.11806837e+179
    3.58254543e+246]
 [  2.66064803e-260   2.99484325e+262  -3.46556953e-311   2.66360040e+233
    7.36099711e+223   3.62479380e+228   6.19180686e+223   1.02188594e-152
    7.04101559e+199]
 [  1.99613101e+161   6.01334637e-154   1.27734658e-152   9.27777354e+242
    8.89746444e+247   4.77092211e+180   6.91286294e+212   2.60988669e+180
    1.87673448e-152]
 [  1.53190189e-094   2.46415835e-154   4.83245960e+276   1.27734658e-152
    4.64334692e+199   1.33856863e-152   1.02584479e+200   5.16442567e+058
    1.27966302e-152]
 [  1.06097754e-153   1.32655307e-258   1.38760003e+219   2.44046062e-152
    3.16451810e+180   4.77295198e+180   6.01346953e-154   5.28964691e+180
    2.47379808e-091]
 [  4.47593816e-091   6.11208869e+228   2.59345432e+161   2.46089539e-154
    4.56335201e-072   4.83245960e+276   7.33956123e+223   1.27734658e-152
    7.04101559e+199]
 [  1.90327826e+185   2.53064200e-258   4.88483536e+252   6.01334668e-154
    4.47593816e-091   1.03417828e-028   4.83245961e+276   6.01347002e-154
    1.96086552e+243]
 [  2.87247029e+161   1.46922109e+195   5.35815010e+199   1.94858306e+227
    1.71963040e+238   6.96410738e+252   1.08988615e+243   6.01347002e-154
    7.48551512e+247]
 [  2.62785629e+092   2.04553260e-258   4.47593804e-091   6.01334512e-154
    2.11673047e+214   2.17371178e+068   6.01334668e-154   2.44041296e-154
    1.32882751e+179]]
arr:  
 [[  0.   1.   2.   3.   4.   5.   6.   7.   8.]
 [  9.  10.  11.  12.  13.  14.  15.  16.  17.]
 [ 18.  19.  20.  21.  22.  23.  24.  25.  26.]
 [ 27.  28.  29.  30.  31.  32.  33.  34.  35.]
 [ 36.  37.  38.  39.  40.  41.  42.  43.  44.]
 [ 45.  46.  47.  48.  49.  50.  51.  52.  53.]
 [ 54.  55.  56.  57.  58.  59.  60.  61.  62.]
 [ 63.  64.  65.  66.  67.  68.  69.  70.  71.]
 [ 72.  73.  74.  75.  76.  77.  78.  79.  80.]]
'''


# 1
print(arr[4],arr[3],arr[0],arr[2])
print(type(arr[4]))
print()
# 2
print(arr[4],'\n',arr[3],'\n',arr[0],'\n',arr[2])
print(type(arr[4]))
print()
# 3
print(arr[[4,3,0,2]])
print(type(arr[[4,3,0,2]]))
'''
3 种输出的区别：
1：每一行之间以空格隔开，每一行都是一个一维数组(numpy.ndarray)，输出的结果是多个一维数组(numpy.ndarray)
2：每一行之间以换行符隔开，每一行都是一个一维数组(numpy.ndarray)，输出的结果是多个一维数组(numpy.ndarray)
3：每一行之间以换行符隔开，每一行都是一个一维数组(numpy.ndarray)，输出的结果是一个二维列表(numpy.ndarray)
输出：
[ 36.  37.  38.  39.  40.  41.  42.  43.  44.] [ 27.  28.  29.  30.  31.  32.  33.  34.  35.] [ 0.  1.  2.  3.  4.  5.  6.  7.  8.] [ 18.  19.  20.  21.  22.  23.  24.  25.  26.]

 [ 36.  37.  38.  39.  40.  41.  42.  43.  44.] 
 [ 27.  28.  29.  30.  31.  32.  33.  34.  35.] 
 [ 0.  1.  2.  3.  4.  5.  6.  7.  8.] 
 [ 18.  19.  20.  21.  22.  23.  24.  25.  26.]

[[ 36.  37.  38.  39.  40.  41.  42.  43.  44.]
 [ 27.  28.  29.  30.  31.  32.  33.  34.  35.]
 [  0.   1.   2.   3.   4.   5.   6.   7.   8.]
 [ 18.  19.  20.  21.  22.  23.  24.  25.  26.]]
'''
# 正数索引从0开始
print(arr[[3,5,7]])
print()
# 倒数第3行，第5行，第7行,负数索引从-1开始
print(arr[[-3,-5,-7]])
print()

#1
print(arr[[1,5,7,2],[0,3,1,2]])
a = arr[[1,5,7,2],[0,3,1,2]]
print('a: ',a)
print(type(a))
print()
# 2
print(arr[(1,0)],arr[(5,3)],arr[(7,1)],arr[(2,2)])
b = arr[(1,0)],arr[(5,3)],arr[(7,1)],arr[(2,2)]
print('b: ',b)
print(type(b))
print()

# 3
print(arr[1,0],arr[5,3],arr[7,1],arr[2,2])
c =arr[1,0],arr[5,3],arr[7,1],arr[2,2]
print('c: ',c)
print(type(c))
print()

'''
输出：
[  9.  48.  64.  20.]
a:  [  9.  48.  64.  20.]
<class 'numpy.ndarray'>

9.0 48.0 64.0 20.0
b:  (9.0, 48.0, 64.0, 20.0)
<class 'tuple'>

9.0 48.0 64.0 20.0
c:  (9.0, 48.0, 64.0, 20.0)
<class 'tuple'>
'''

# 打印第1行的0,3,1,2 这些列，行/列都是从0开始
# 打印第5行的0,3,1,2 这些列，行/列都是从0开始
# 1
print(arr[[1,5,7,2]][:,[0,3,1,2]])
print()
aa = arr[[1,5,7,2]][:,[0,3,1,2]]
print('aa:','\n',aa)
print(type(aa))
# 2
print(arr[np.ix_([1,5,7,2],[0,3,1,2])])
bb = arr[[1,5,7,2]][:,[0,3,1,2]]
print('bb:','\n',bb)
print(type(bb))
print()

'''
1 和 2 输出的结果完全一样，只是2的可读性要好些
[[  9.  12.  10.  11.]
 [ 45.  48.  46.  47.]
 [ 63.  66.  64.  65.]
 [ 18.  21.  19.  20.]]

aa: 
 [[  9.  12.  10.  11.]
 [ 45.  48.  46.  47.]
 [ 63.  66.  64.  65.]
 [ 18.  21.  19.  20.]]
<class 'numpy.ndarray'>
[[  9.  12.  10.  11.]
 [ 45.  48.  46.  47.]
 [ 63.  66.  64.  65.]
 [ 18.  21.  19.  20.]]
bb: 
 [[  9.  12.  10.  11.]
 [ 45.  48.  46.  47.]
 [ 63.  66.  64.  65.]
 [ 18.  21.  19.  20.]]
<class 'numpy.ndarray'>
'''