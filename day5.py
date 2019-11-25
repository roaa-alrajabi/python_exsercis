# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:21:28 2019

@author: orange
"""
# =============================================================================
# class person:
#     def hello(self):
#         print("hello")
# p= person()
# p.hello()
# =============================================================================
# =============================================================================
# constructor & destructor
# =============================================================================
# =============================================================================
# class person:
#     def __init__(self,name):
#         self.name=name
#     def whome(self):
#         return "I am "+ self.name
#     def __del__(self):
#         print("I have been deleted  ")
#         
# p=person('tom') 
# print(p.whome())
# print(p.name) 
# del p      
# =============================================================================
# =============================================================================
# private and public 
# =============================================================================
# =============================================================================
# class Encapsulation(object):
#     def __init__(self,name,age,major):
#         self.Apublic=name
#         self._Bprotected=age
#         self.__Cprivate=major
#     def getprivate(self):
#         return self.__Cprivate
# 
# x=Encapsulation("roaa",23,"cis")
# print(x.Apublic)
# print(x._Bprotected)
# print(x.getprivate())
# =============================================================================
# =============================================================================
# class Parent(object):
#     def __init__(self, name,age,salary):
#         self.name=name
#         self._age=age
#         self.__salary=salary
#         
#     def public(self):
#        print("call pub")
#     def _protected(self):
#        print("call protected")
#     def __private(self):
#        print("call private")
#      
# class child(Parent):
#   def foo(self):
#         self.public()
#         self._protected()
#         print(self.name)
#         print(self._age)
# c=child("roaa",40,100)
# c.foo()
# c.public()    
# =============================================================================
# =============================================================================
# class Circle:
#     def __init__(self, radius): 
#       self.__radius= radius
#       
#     def setRadius(self, radius):  
#             self.__radius= radius
#     def getRadius(self): 
#       return self.__radius
#   
#     
#     def __add__(self, another_circle):
#       return Circle( self.__radius+ another_circle.__radius)
#   
#     
# c1 = Circle(4)
# print(c1.getRadius())
# c2 = Circle(5)
# print(c2.getRadius())
# c3 = c1 + c2
# print(c3.getRadius())   
# =============================================================================
# =============================================================================
# Q1
# =============================================================================
class employee:
    def __init__(self,number:int,name:str,Address:str,salary:float,jobtilte:str):
        self.number=number
        self.__name=name
        self.__Address=Address
        self.__salary=salary
        self.__jobtilte=jobtilte
    
    def getname(self):
        return self.__name
    
    def Setaddress(self,Address):
        self.__Address=Address
    
    def getadderss(self):
        return self.__Address
    
    def getsalary(self):
        return self.__salary
    def getjobtilte(self):
        return self.__jobtilte
    
    def __del__(self):
        print(self.__name,"has been deleted")
    
        
employee1=employee(1,"Mohammad Kalid","Amman,Jordan",500,"consultant")
print('Employee1 Information')
print("Employee Number1:",employee1.number)
print('Name:',employee1.getname())
print("Address:",employee1.getadderss())
print("Salary:",employee1.getsalary())
print("Job Tilte:",employee1.getjobtilte())
employee1.Setaddress('USA')
print('Employee1 New_address:',employee1.getadderss())
print("------------------------------------------")

employee2=employee(2,"Hala Rana","Aqaba,Jordan",750.0,"manager")
print('Employee1 Information:',"Employee Number2:",employee2.number,
      'Name:',employee2.getname(),"Address:",employee2.getadderss(),
     "Salary:",employee2.getsalary(),"Job Tilte:",employee2.getjobtilte())

del employee1
del employee2

       