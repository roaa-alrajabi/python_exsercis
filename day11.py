# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:30:38 2019

@author: orange
"""
# =============================================================================
# from tkinter import *
# root=Tk(className="first page")
# root.geometry("300x150+50+50")
# s=root.winfo_screenmmwidth()
# w=root.winfo_screenmmwidth()
# root.mainloop()
# print(s)
# print(w)
# =============================================================================
# =============================================================================
# import tkinter as tk
# root=tk.Tk()
# lable=tk.Label(root,text="roaa",padx=10,pady=10)
# lable.pack()
# root.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# top=Tk()
# top.geometry("200x100")
# b=Button(top,text="simple")
# b.pack()
# top.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# def passed():
#     print("click here")
# root=Tk()
# button=Button(root,text="click",command=passed)  
# button.pack(padx=40,pady=40)  
# root.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# from tkinter import messagebox
# def Pressed():
#     dialog_title="please answer"
#     dialog_text="Do you like to travel?"
#     answer=messagebox.askquestion(dialog_title,dialog_text)
#     if answer=='yes':
#         print("I like this !")
#     else:
#         print("You must have clicked the wrong button by accident.")
# root=Tk()
# button=Button(root,text="Press Me :p",command=Pressed)
# button.pack(padx=40,pady=40)
# root.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# # =============================================================================
# =============================================================================
# win=Tk()
# v=StringVar()
# e=Entry(win,textvariable=v)
# e.pack()
# v.set("roaa ali")
# print(v.get())
# win.mainloop() 
# =============================================================================
# =============================================================================
# from tkinter import *
# root = Tk()
# root.title('menu_win')
# def notdone():
#     messagebox.showinfo('Not implemented', 'Not yet available')
# top = Menu(root)
# root.config(menu=top)
# file = Menu(top,tearoff=0)
# file.add_command(label='New...', command=notdone)
# file.add_command(label='Open...', command=notdone)
# file.add_separator()
# file.add_command(label='Quit', command=root.destroy)
# top.add_cascade(label='File', menu=file)
# edit = Menu(top,tearoff= 0)
# edit.add_command(label='Cut', command=notdone)
# edit.add_command(label='Paste', command=notdone)
# top.add_cascade(label='Edit', menu=edit)
# root.mainloop()    
# =============================================================================
# =============================================================================
# from tkinter import *
# from tkinter.colorchooser import *
# def getcolor():
#     color=askcolor()
#     print(color)
# Button(text="color",command=getcolor).pack()
# mainloop()   
# =============================================================================
# =============================================================================
# Q1
# =============================================================================
# =============================================================================
# =============================================================================
# def act ():
#     if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
#          z = messagebox.showinfo("Login", "Successful login")
#          print (z)
#          if z == "ok":
#              parent.destroy()
#     else:
#          messagebox.showinfo("Login", "Wrong User Name or Password")
# parent = Tk()
# value1 = StringVar()
# value2 = StringVar()
# name = Label(parent, text = "Name").grid(row=0, column = 0)
# e1 = Entry(parent, textvariable= value1).grid(row = 0, column =1)
# password = Label(parent, text ="Password").grid(row = 1, column = 0)
# e2 = Entry(parent, textvariable= value2).grid(row = 1, column =1)
# submit = Button(parent, text="Submit", command= act).grid(row = 4, column = 0)
# parent.mainloop()
# =============================================================================
# =============================================================================
# =============================================================================
# Q2
# =============================================================================
# from tkinter import *
# from tkinter import messagebox
# from tkinter import scrolledtext
# def open_child1():
#     dialog_title=""
#     dialog_text="This is a message"
#     answer=messagebox.showinfo(dialog_title,dialog_text)
# def open_child2():
#     top=Tk()
#     top.title('Child window 2')
#     top.geometry('400x250')
#     name=Label(top,text="Emy Number").place(x=30,y=50)
#     email=Label(top,text="Emy Name").place(x=30,y=90)
#     e1=Entry(top).place(x=100,y=50)
#     e2=Entry(top).place(x=100,y=90)
#     button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
#     button.pack()
#     top.mainloop()
# def open_child3():
#     win=Tk()
#     win.title("Welcome")
#     win.geometry('350x200')
#     txt=scrolledtext.ScrolledText(win,width=40,height=10)
#     txt.grid(column=0,row=0)
#
#
#
# root = Tk()
# root.title('Root window')
# Button(root, text = 'open child window 1', command = open_child1).grid()
# Button(root, text = 'open child window 2', command = open_child2).grid()
# Button(root, text = 'open child window 3', command = open_child3).grid()
# root.mainloop()
#
# 
# =============================================================================
# Q3
# =============================================================================
# =============================================================================
# from tkinter import *
# from tkinter.colorchooser import *
# root = Tk()
# def getcolor():
#     color=askcolor()
#     root.config(background=color[1])
# Button(root,text="select",command=getcolor).pack()
# mainloop()
# =============================================================================
