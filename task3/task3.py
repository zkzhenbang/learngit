#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog
import subprocess
import os
import re








# 创建窗体
top = Tk()
top.title("app install")
top.geometry("380x250+740+380")
top.resizable(0, 0)      #禁止缩放

# 左侧Label显示的内容，更改内容可以修改show_f5.set(XXXX)
show_f5 = StringVar()
show_f5.set('欢迎使用')

# 按下刷新设备按钮
def pressF5():
    showf5 = os.popen("adb devices")
    a=showf5.read()
    show_f5.set(a)

# 按下按钮1安装调用方法
def pressButton_1():
    filename1 = tkFileDialog.askopenfilename(initialdir ='/')
    # 向serial number设备安装filename的包
    # install_1=os.popen("adb -s <serial number> install filename1")

#  按下按钮2安装调用方法
def pressButton_2():
    filename2 = tkFileDialog.askopenfilename(initialdir ='/')
    # 向serial number设备安装filename2的包
    # install_1=os.popen("adb -s <serial number> install filename2")

#  按下按钮3安装调用方法
def pressButton_3():
    filename1 = tkFileDialog.askopenfilename(initialdir ='/')
    # 向serial number设备安装filename的包
    # install_1=os.popen("adb -s <serial number> install filename3")

show_l = Frame(top)
show_l.pack(side=LEFT)
show_r = Frame(top)
show_r.pack(side=RIGHT)

messgeShow = Label(show_l, textvariable=show_f5)
messgeShow.pack()
messgeShow.propagate(0)

f5 = Button(show_r, text="刷新设备",command=pressF5)
f5.pack(pady=5)

frm = Frame(show_r)
frm_L = Frame(frm)
frm_R = Frame(frm)
frm.pack()
frm_L.pack(side=LEFT)
frm_R.pack(side=RIGHT)

label_1 = Label(frm_L, text="设备1",width=8,height=1)
label_2 = Label(frm_L, text="设备2",width=8,height=1)
label_3 = Label(frm_L, text="设备3",width=8,height=1)
label_1.pack(pady=20)
label_2.pack(pady=20)
label_3.pack(pady=20)




button_1 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_1)
button_1.pack(pady=16,padx=10)
button_2 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_2)
button_2.pack(pady=18,padx=10)
button_3 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_3)
button_3.pack(pady=18,padx=10)







top.mainloop()

