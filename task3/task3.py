#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

top = Tk()
top.geometry("300x150")
frm=Frame(top)
frm_l=Frame(frm)
frm_r=Frame(frm)

message=Message(frm_l,text="haha")
message.pack()

button_f5=Button(frm_r,text="刷新设备")
button_f5.pack(side=TOP)

# 编辑界面右侧标签显示及按钮
label_1=Label(frm_r,text="设备1",)
label_2=Label(frm_r,text="设备2")
label_3=Label(frm_r,text="设备3")
button_1=Button(frm_r,text="安装",)
button_2=Button(frm_r,text="安装")
button_3=Button(frm_r,text="安装")
label_1.pack(side=LEFT)
button_1.pack(side=RIGHT)
label_2.pack(side=LEFT)
button_2.pack(side=RIGHT)
label_3.pack(side=LEFT)
button_3.pack(side=RIGHT)



frm.pack()
frm_l.pack(side=LEFT)
frm_r.pack(side=RIGHT)
top.mainloop()

