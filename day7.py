# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:26:54 2019

@author: orange
"""

import numpy as np 
# =============================================================================
# b= np.array([1,2,3,4])
# print(b)
# =============================================================================
# =============================================================================
# c=np.array([[1,2,4,6,6],[1,2,3,4,5]])
# print(c)
# =============================================================================
# =============================================================================
# a=np.arange(12).reshape(3,4)
# print(a)
# print(a.size)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# =============================================================================
# =============================================================================
# g= np.ones( (2,4) , dtype=np.int16 )*6
# print(g)
# =============================================================================
# =============================================================================
# a = np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]]) 
# print('a array:')
# print (a)
# print('\n quicksort:')
# print (np.sort(a,kind='quicksort') )
# print('\n mergesort')
# print (np.sort(a,kind='mergesort') ) 
# print('\n heapsort:')
# print (np.sort(a,kind='heapsort') ) 
# print('\n sort as flattened arra:')
# print (np.sort(a,axis=None) )
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# f=[1, 2, 0, 4,5,6]
# plt.plot(f)
# plt.show()
# =============================================================================
# =============================================================================
# Q1
# =============================================================================
# =============================================================================
# a=np.zeros((10,10))
# print(a)
# =============================================================================
# =============================================================================
# Q1
# =============================================================================
# =============================================================================
# a=np.ones((10,10))
# print(a)
# =============================================================================
# =============================================================================
# Q1
# =============================================================================
# =============================================================================
# a=np.ones((10,10))*5
# print(a)
# =============================================================================
# =============================================================================
# Q2
# =============================================================================
# =============================================================================
# a=np.arange(30,70)
# print(a)
# =============================================================================
# =============================================================================
# Q3
# =============================================================================
# =============================================================================
# a=np.arange(30,70,2)
# print(a)
# =============================================================================
# =============================================================================
# Q4
# =============================================================================
# =============================================================================
# n=np.identity(3,dtype=None)
# print(n)
# =============================================================================
# =============================================================================
# Q5
# =============================================================================
# =============================================================================
# print(np.random.randint(0,1))
# =============================================================================
# =============================================================================
# Q6
# =============================================================================
# =============================================================================
# a=np.arange(2,14).reshape(3,4)
# for a in a:
#     for a in a:
#      print(a)
# =============================================================================
# =============================================================================
# Q7
# =============================================================================
# =============================================================================
# a=np.arange(20)
# for List in a: 
#    if List>=9 and List<=15:
#      print(List)
#     
# =============================================================================
# =============================================================================
# Q8
# =============================================================================
# x=[1,8,3,5]
# y=np.random.randint(0,11,4)
# print(x*y)
# =============================================================================
# Q9
# =============================================================================
# =============================================================================
# a=np.arange(12).reshape(3,4)
# print(a.shape)
# =============================================================================

# =============================================================================
# Q10
# =============================================================================
# =============================================================================
# =============================================================================
# x = np.random.random((3,3,3))
# print(x)
# =============================================================================
# Q11
# =============================================================================
# =============================================================================
# a=np.array([9,-1,2,5])
# b=np.array([1,-6,0,10])
# c=np.array([[1,8,2,5],[3,1,7,9]])
# print("a-b: ",a-b) 
# print("a*b: ",a*b)
# print("a.dot(b):",a.dot(b)) 
# print("a*2: ",a*2) 
# print("np.sin(a): ",np.sin(a)) 
# print("a<3: ",a<3) 
# print("a.sum():",a.sum()) 
# print("a.sum(axis=0): ",a.sum(axis=0))
# print("c.sum():",c.sum())
# print("c.sum(axis=0): ",c.sum(axis=0)) 
# print("a.min(): ",a.min()) 
# print("a.max(): ",a.max())
# print("a.mean(): ",a.mean()) 
# print("a average() ",np.average(a)) 
# print("a median(): ",np.median(a)) 
# print("a std(): ",np.std(a)) 
# print("a var(): ",np.var(a)) 
# print("c.cumsum(): ",c.cumsum()) 
# print("a[1:2] ",a [1:2]) 
# print("a[2:]: ",a [2:]) 
# print("c[-1]: ",c[-1] )
# =============================================================================
# =============================================================================
# Q12
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# X = range(1, 50)
# Y = [value * 3 for value in X]
# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# plt.show()
# =============================================================================
# =============================================================================
# Q13
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# x1 = [10,20,30]
# y1 = [20,40,10]
# plt.plot(x1, y1, label = "line 1")
# x2 = [10,20,30]
# y2 = [40,10,30]
# plt.plot(x2, y2, label = "line 2")
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Two or more lines on same plot with suitable legends ')
# plt.legend()
# plt.show()
# =============================================================================
# =============================================================================
# Q14
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
# plt.show()
# =============================================================================
# =============================================================================
# Q15
# =============================================================================
# =============================================================================
# import matplotlib.pyplot as plt
# x = ['Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
# plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.title("PopularitY of Programming Language")
# plt.xticks(x_pos, x)
# #
# plt.show()
# =============================================================================
