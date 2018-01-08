# -*- coding:utf-8 -*-

import numpy as np
import numpy.random as np_random

print('转置矩阵')
arr = np.arange(15)
# 将arr 转换成一个3行5列的二维矩阵。行*列=原矩阵元素的总和。否则会报错
arr1 = arr.reshape((3,5))
print('arr: ','\n',arr)
print('arr1: ','\n',arr1)
'''
输出：
arr:  
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
arr1:  
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

print('原矩阵和转置矩阵做点积')
arr2 = np_random.randn(6,3)
print('arr2: ','\n',arr2)
print('arr2.T: ','\n',arr2.T)
print('arr2 * arr2.T: ','\n',np.dot(arr2,arr2.T))

'''
原矩阵和转置矩阵做点积,计算方法：
	     A				  A.T	
						[[a,e,i,m],
	[[a,b,c,d,r,u],		[b,f,j,n],
	[e,f,g,h,q,v],		[c,g,k,o],
	[i,j,k,l,s,w],		[d,h,l,p],
	[m,n,o,p,t,x]]		[r,q,s,t],
						[u,v,w,x]]
numpy.dot(A,A.T)
a*a + b*b + c*c + d*d + r*r + u*u = aaa*e + b*f + c*g + d*h + r*q + u*v = bb
a*i + b*j + c*k + d*l + r*s + u*w = cc
a*m + b*n + c+o + d*p + r*t + u*x = dd

e*e + f*f + g*g + h*h + q*q + v*v = ee

i*i + j*j + k*k + l*l + s*s + w*w = ff

m*m + n*n + o*o + p*p + t*t + x*x = gg

e*i + f*j + g*k + h*l + q*s + v*w = hh

e*m + f*n + g*o + h*p + q*t + v*x = ii

m*i + n*j + o*k + p*l + t*s + x*w = jj

numpy.dot(A,A.T):
[ aa bb cc dd ]
[ bb ee hh ii ]
[ cc hh ff jj ]
[ dd ii jj gg ]
'''

print('高维矩阵转换')
arr3 = np.arange(24)
arr4 = arr3.reshape((2,3,4))
print("arr3:",arr3)
print("arr4:",'\n',arr4)
'''
输出：
2 * 3 * 4 = 24
arr3: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
arr4: 
 [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''
print('arr4.transpose((1,0,2))','\n',arr4.transpose((1,0,2)))
print()
print('arr4.swapaxes(1,2)','\n',arr4.swapaxes(1,2))
print()
'''
输出：
transpose() 参数为坐标抽，正常顺序(0,1,2,..,n-1)
现传入(1,0,2) 表示将第0个坐标和第1个坐标互换
更换之前 2*3*4
arr4[0][0] = arr4_t[0][0] = [0,1,2,3]
arr4[0][1] = arr4_t[1][0] = [4,5,6,7]
arr4[0][2] = arr4_t[2][0] = [8,9,10,11]
arr4[1][0] = arr4_t[0][1] = [12,13,14,15]
arr4[1][1] = arr4_t[1][1] = [16,17,18,19]
arr4[1][2] = arr4_t[2][1] = [20,21,22,23]

更换之后 3*2*4
arr4.transpose((1,0,2)) 
 [[[ 0  1  2  3]
  [12 13 14 15]]

 [[ 4  5  6  7]
  [16 17 18 19]]

 [[ 8  9 10 11]
  [20 21 22 23]]]

arr4.swapaxes(1,2) 
 [[[ 0  4  8]
  [ 1  5  9]
  [ 2  6 10]
  [ 3  7 11]]

 [[12 16 20]
  [13 17 21]
  [14 18 22]
  [15 19 23]]]
  
  swapaxes() 2个参数，都是坐标抽参数，作用：将两个坐标抽的内容兑换
  swapaxes(1,2) 表示将1,2这两个坐标互换，行和列互换
  arr4.swapaxes(1,2) 
 [[[ 0  4  8]
  [ 1  5  9]
  [ 2  6 10]
  [ 3  7 11]]

 [[12 16 20]
  [13 17 21]
  [14 18 22]
  [15 19 23]]]

'''