# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:31:07 2019

@author: orange
"""
# =============================================================================
# 
# def name(name):
#     print(name + "  is the file name")
# name("roaa")
# name("ruba")
# name("rasha")
# =============================================================================
# =============================================================================
# 
# def food(food):
#     for x in food:
#         print(x)
#         
# fruit=["apple","orange"]  
# food(fruit)      
# =============================================================================

# =============================================================================
# def mulitplie(x):
#     return 5*x 
# print(mulitplie(3))
# =============================================================================
# =============================================================================
# def adder(*num):
#     sum=0
#     for n in num :
#         sum =sum+n 
#     print("sum:",sum)
#         
# adder(2,3,4,5)
# ==========================================================================
# =============================================================================
# the order will effect 
# def name(*arg,arg1):
#    print(arg1)
#    for agr in a:
#        print(agr)
# name("hello","hi","welcome")
# =============================================================================
# =============================================================================
# def string(**agr):
#     for key,value in agr.items():
#         print(key,value)
#         
# string(first="roaa",seconde="ali")        
# =============================================================================
# =============================================================================
# x="roaa"
# def word():
#  print(x)
#  
# print("hello",x)
# =============================================================================
# =============================================================================
# def fact(n):
#      if n==1:
#          return 1
#      else:
#        return n*fact(n-1)
# print(fact(10))
# =============================================================================
# =============================================================================
# sum=lambda x,w,r:x+w+r
# print (sum(0,3,4))
# =============================================================================
# =============================================================================
# l=[1,2,3,4,5,6,7,8,9]
# final_list =list(map(lambda x:x*2,l))
# print(final_list)
# =============================================================================
# =============================================================================
# l=[1,2,3,4,5,6,7,8,9,10]
# 
# final_list=list(filter(lambda x:x%2==0,l))
# print(final_list)
# =============================================================================
# =============================================================================
# l=[34,5,6,23,79,97,59,78,6]
# degree= list(filter(lambda x : x>75,l))
# print(degree)
# =============================================================================
# =============================================================================
# list_num=[1,2,3,4,5,6]
# list_string=["a","e","r","t","y","m"]
# list_name=["roaa","ruba"]
# marge=list(zip(list_num,list_string,list_name))
# print(marge)
# =============================================================================
# ==============================================================================
# Q15
# =============================================================================
# =============================================================================
# number=[1,2,3]
# letters=["a","b","c"]
# marge=list(zip(number,letters))
# print(marge)
# =============================================================================
# =============================================================================
# Q14
# =============================================================================
# =============================================================================
from functools import reduce 
lists=[1,2,3,4,5,6]
x= reduce(lambda a,b: a if a<b else b,lists)
print(x)

# Q13
# =============================================================================
# =============================================================================
# c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
# print(list(c))
# =============================================================================
# =============================================================================
# Q12
# =============================================================================
# =============================================================================
# c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
# print(list(c))
# =============================================================================
# =============================================================================
# Q11
# =============================================================================
# =============================================================================
# def func(a,b):
#     return a+b
# a=list(map(func,[2,4,5],[1,2,3,2,4]))
# print(a)
# =============================================================================
# =============================================================================
# Q10
# =============================================================================
# =============================================================================
# def newfunc(a):
#     return a*a 
# x=list(map(newfunc,(1,2,3,4)))
# print(x)
# =============================================================================
# =============================================================================
# Q9
# =============================================================================
# =============================================================================
# x=list(map(int,input("enter a multiple value:").split()))
# print("list of student",x)
# =============================================================================
# =============================================================================
# Q8
# =============================================================================
# =============================================================================
# def fun(variable):
#     letters=["a","e","i","o","u"]
#     if(variable in letters):
#         return True 
#     else:
#         return False
# sq=["g","j","e","j","k","o","p","r"]
# filtered=list(filter(fun,sq))
# print(filtered)
# =============================================================================
# =============================================================================
# Q7 
# =============================================================================
# =============================================================================
# coin=('bitcoin','ether','ripple','litecoin')
# code=('BTC','ETH','XRP','LTC')
# d=dict(zip(coin,code))
# print(d)
# =============================================================================
# =============================================================================
# Q6
# =============================================================================
# =============================================================================
# x=("Joey","Monica","Ross")
# y=("Chandler","pheobe")
# z=('David','Rachel','Courtney')
# result=list(zip(coin,code))
# print(result)
# =============================================================================
# =============================================================================
# Q5
# =============================================================================
# =============================================================================
# x=lambda a,b,c:a+b+c
# print(x(5,6,2))
# =============================================================================
# =============================================================================
# Q4
# =============================================================================
# =============================================================================
# number_list=range(-5,5)
# final_list=list(filter(lambda x:x<0,number_list))
# print(final_list)
# =============================================================================
# =============================================================================
# Q3
# =============================================================================
# =============================================================================
# def multiple(a,b):
#     print("multiple 2 num :",a*b)
# multiple(2,3) 
# =============================================================================
# =============================================================================
# Q2
# =============================================================================
# =============================================================================
# from functools import reduce 
# lists=[1,2,3,4,5,6]
# x= reduce(lambda a,b:a*b,lists)
# print(x)
# =============================================================================
# Q1
# =============================================================================
# =============================================================================
# o=lambda x=1,y=2,z=3:x+z+y
# print(o())
# print(o(10))
# print(o(10,20))
# =============================================================================
# ===================================================
