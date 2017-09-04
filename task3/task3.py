#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

top = Tk()
top.geometry("450x250")

welcome = Label(top, text="注册界面")  # 注册标签
welcome.pack()

frm = Frame(top)  # 界面框架
frm_L = Frame(frm)
frm_R = Frame(frm)
frm2 = Frame(top)
frm.pack()
frm_L.pack(side=LEFT)
frm_R.pack(side=RIGHT)
frm2.pack()

label_1 = Label(frm_L, text="设备1",width=10,height=2)  # 用户名标签
label_2 = Label(frm_L, text="设备2",width=10,height=2)  # 密码标签
label_3 = Label(frm_L, text="设备3",width=10,height=2)  # 再次输入密码标签
label_1.pack()
label_2.pack()
label_3.pack()


button_1 = Button (frm_R, text="安装",width=10,height=2)  # 输入框-用户名
button_1.pack()


button_2 = Button (frm_R, text="安装",width=10,height=2)
button_2.pack()


button_3 = Button (frm_R, text="安装",width=10,height=2)
button_3.pack()




top.mainloop()

