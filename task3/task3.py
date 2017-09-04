#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog

top = Tk()
top.geometry("450x250")

f5 = Button(top, text="刷新设备")  # 注册标签
f5.pack(pady=5)

frm = Frame(top)  # 界面框架
frm_L = Frame(frm)
frm_R = Frame(frm)
frm2 = Frame(top)
frm.pack()
frm_L.pack(side=LEFT)
frm_R.pack(side=RIGHT)
frm2.pack()

label_1 = Label(frm_L, text="设备1",width=8,height=1,)  # 用户名标签
label_2 = Label(frm_L, text="设备2",width=8,height=1)  # 密码标签
label_3 = Label(frm_L, text="设备3",width=8,height=1)  # 再次输入密码标签
label_1.pack(pady=20)
label_2.pack(pady=20)
label_3.pack(pady=20)


def getFile():
    filename = str(tkFileDialog.askopenfilename(initialdir ='/'))
    tishi_1=Toplevel()
    text_filename=Text(tishi_1,text=filename)
    text_filename.pack()

button_1 = Button (frm_R, text="安装",width=8,height=1,command=getFile)  # 输入框-用户名
button_1.pack(pady=16)
button_2 = Button (frm_R, text="安装",width=8,height=1)
button_2.pack(pady=18)
button_3 = Button (frm_R, text="安装",width=8,height=1)
button_3.pack(pady=18)







top.mainloop()

