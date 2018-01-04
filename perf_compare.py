'''
python 有3种类似的数组数据结构
    1、list
    2、array
    3、numpy.array
针对这3种数据结构求和的方法：for循环，python自带的sum() 函数，numpy.sum() 函数
对于list 数据结构来说，3种求和方法性能从高到低：sum,for,numpy.sum
对于array 数据结构来说，3种求和方法性能从高到低:numpy.sum,sum,for
对于numpy.array 数据结构来说，3种求和方法性能从高到低:numpy.sum,sum,for
一般情况下都是使用numpy.array 数据结构，并使用numpy.sum 这种方法求和，性能最好
验证代码如下：
'''
import timeit
common_for = '''
for d in data:
    s += d
'''
common_sum = '''
sum(data)
'''
common_numpy_sum = '''
numpy.sum(data)
'''

def timeit_list(n,loops):
    list_setup = '''
import numpy
data = [1] * {}
s = 0
'''.format(n)
    print('list:')
    print(timeit.timeit(common_for,list_setup,number = loops))
    print(timeit.timeit(common_sum,list_setup,number = loops))
    print(timeit.timeit(common_numpy_sum,list_setup,number = loops))

def timeit_array(n,loops):
    array_setup = '''
import numpy
import array
data = array.array('L',[1] * {})
s = 0
'''.format(n)
    print('array:')
    print(timeit.timeit(common_for,array_setup,number=loops))
    print(timeit.timeit(common_sum,array_setup,number=loops))
    print(timeit.timeit(common_numpy_sum,array_setup,number=loops))

# timeit.timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)
# stmt 执行语句，对应此列就是求和的方法
# setup 表示导入执行语句的环境。对应于此列就是求和对象，3种数据结构
# number 执行语句的次数


def timeit_numpy(n,loops):
    numpy_setup = '''
import numpy
data = numpy.array([1] * {})
s = 0
'''.format(n)
    print('numpy:')
    print(timeit.timeit(common_for,numpy_setup,number=loops))
    print(timeit.timeit(common_sum,numpy_setup,number=loops))
    print(timeit.timeit(common_numpy_sum,numpy_setup,number=loops))

if __name__ == '__main__':
    timeit_list(50000,500)
    timeit_array(50000,500)
    timeit_numpy(50000,500)

'''
输出结果：
list:
0.9750489423518208
0.17103307848246296
1.1372533139456766
array:
1.0522430320954466
0.2317780696683398
0.013543432477862272
numpy:
2.1035650884406687
1.9166693818074405
0.011469995832646518
'''

# 这里解释下format()  函数在此列的用法
list_setup = '''
import numpy
data = [1] * {}
s = 0
'''
print(list_setup)
'\nimport numpy\ndata = [1] * 50000\ns = 0\n'
print(list_setup.format(5))
'\nimport numpy\ndata = [1] * 50000\ns = 0\n'
print(list_setup.format(50000))
'\nimport numpy\ndata = [1] * 50000\ns = 0\n'
#此语句执行的话就会产生一个列表，保护50000个1
