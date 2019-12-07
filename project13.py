# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:47:27 2019

@author: orange
"""
from tkinter import *
import sqlite3 
from tkinter import scrolledtext
# =============================================================================
# conn=sqlite3.connect('OrgDB.db')
# c=conn.cursor()
# drop="drop table OrgDB"
# c.execute(drop)
# conn.close()
# =============================================================================
# =============================================================================
# conn=sqlite3.connect('OrgDB.db')
# conn.execute('''create table OrgDB
#              (EmployeeNumber     int,
#              EmployeeName        text,
#              EmployeeGender      text,
#              EmployeeNationality text,
#              EmployeeDateofBirth text,
#              EmployeeAddress     text,
#              EmployeeDepartment  text,
#              EmployeeSalary      real);''')
# print('create table')
# conn.close()
# =============================================================================


def view_Employee_submit():
    conn=sqlite3.connect('OrgDB.db')
    select=conn.cursor()
    select.execute('select *from OrgDB ')
    view=Toplevel(root)
    view.title(' Employee')
    view.geometry("550x300")
    get=scrolledtext.ScrolledText(view,width=230,height=340)
    for data in select:
# =============================================================================
#         print(data)
# =============================================================================
       get.insert(END,data)
       get.insert(END,"\n")
    get.pack()   
    conn.commit()   
       
            
        

def Add_Employee():
    def Add_Employee_submit():
        conn=sqlite3.connect("OrgDB.db")
        c=conn.cursor()
        c.execute('INSERT  into OrgDB  values(?,?,?,?,?,?,?,?)',(E_Number.get(),E_Name.get(),E_Gender.get(),E_Nationality.get(),E_DateofBirth.get(),E_Address.get(),E_Department.get(),E_Salary.get()))
        conn.commit()
        print('ok')
        
    
    add=Toplevel(root)
    add.title('Add Employee')
    add.geometry("350x300+300+200")
    
    E_Number=IntVar()
    E_Name=StringVar()
    E_Gender=StringVar()
    E_Nationality=StringVar()
    E_DateofBirth=StringVar()
    E_Address=StringVar()
    E_Department=StringVar()
    E_Salary=IntVar()
    Number=Label(add,text='EmployeeNumber').grid()
    e1 = Entry(add, textvariable=E_Number).grid(row = 0, column =1)
    Name=Label(add,text='EmployeeName').grid()
    e2 = Entry(add, textvariable= E_Name).grid(row = 1, column =1)
    Gender=Label(add,text='EmployeeGender').grid()
    e1= Radiobutton(add,text='male', variable= E_Gender,value='male').grid(row = 2, column =1)
    e2= Radiobutton(add, text='female',variable= E_Gender,value='female').grid(row = 2, column =2)
    Nationality=Label(add,text='EmployeeNationality').grid()
    e3= Entry(add, textvariable= E_Nationality).grid(row = 3, column =1)
    DateofBirth=Label(add,text='EmployeeDateofBirth').grid()
    e4= Entry(add, textvariable= E_DateofBirth).grid(row = 4, column =1)
    Address=Label(add,text='EmployeeAddress').grid()
    e5= Entry(add, textvariable= E_Address).grid(row = 5, column =1)
    Department=Label(add,text='EmployeeDepartment').grid()
    e6= Entry(add, textvariable= E_Department).grid(row = 6, column =1)
    Salary=Label(add,text='EmployeeSalary').grid()
    e7= Entry(add, textvariable= E_Salary).grid(row = 7, column =1)
    submit = Button(add, text="Add", command= Add_Employee_submit).grid(row = 8, column = 0)

    
    
    
    

root=Tk()
root.title("Add Employee")
Button(root,text='Add Employee',command=Add_Employee).grid()
Button(root,text='view Employee',command=view_Employee_submit).grid()

root.mainloop()

