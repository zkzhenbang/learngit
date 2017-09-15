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


# 对安装的结果进行反馈，弹出toplevel提示用户
def tishi():
    toplevel_tishi=Toplevel()
    toplevel_tishi.geometry("200x80+740+380")
    toplevel_tishi.attributes("-topmost", 1)
    label_tishi=Label(toplevel_tishi,text=tishi_message)
    label_tishi.pack()

# 按下刷新设备按钮
def pressF5():
    global b
    showf5 = os.popen("adb devices")
    a=showf5.read()
    # 将adb devices得到的内容放入列表
    b = a.split()
    if len(b)>10:
        show_f5.set("连接设备超过3台，请减少数量")
    elif len(b)>4 and len(b)<=10:
        show_f5.set(a)
    else:
        show_f5.set("未检测到设备，请重新连接")


# 按下按钮1安装调用方法
def pressButton_1():
    global tishi_message
    filename1 = tkFileDialog.askopenfilename(initialdir ='/')
    try:
        # 向serial number1的设备安装filename的包
        install_1=os.popen("adb -s %s install %s"%(b[4],filename1))
    except:
        show_f5.set("请点击刷新设备")
    else:
        get_result1 = install_1.read()
        getresult1 = get_result1.split()
        number1 = (len(getresult1))

        if getresult1[number1 - 1] == "Success":
            tishi_message="设备1安装成功！"
            tishi()

        else:
            tishi_message = "设备1安装失败！"
            tishi()

#  按下按钮2安装调用方法
def pressButton_2():
    filename2 = tkFileDialog.askopenfilename(initialdir ='/')
    try:
        # 向serial number2的设备安装filename2的包
        install_2=os.popen("adb -s %s install %s"%(b[6],filename2))
    except:
        show_f5.set("请点击刷新设备")
    else:
        get_result2 = install_2.read()
        getresult2 = get_result2.split()
        number2=(len(getresult2))
        if getresult2[number2-1]=="Success":
            show_f5.set("设备2安装成功！")
        else:
            show_f5.set("设备2安装失败！")


#  按下按钮3安装调用方法
def pressButton_3():
    try:
        filename3 = tkFileDialog.askopenfilename(initialdir ='/')
        # 向serial number3的设备安装filename3的包
        install_3=os.popen("adb -s %s install %s"%(b[8],filename3))
    except:
        show_f5.set("请点击刷新设备")
    else:
        get_result3 = install_3.read()
        getresult3 = get_result3.split()
        number3 = (len(getresult3))
        if getresult3[number3 - 1] == "Success":
            show_f5.set("设备3安装成功！")
        else:
            show_f5.set("设备3安装失败！")



# 布局设置
show_l = Frame(top)
show_l.pack(side=LEFT)
show_r = Frame(top)
show_r.pack(side=RIGHT)

# 界面左侧消息显示框
messgeShow = Label(show_l, textvariable=show_f5)
messgeShow.pack()
messgeShow.propagate(0)

# 刷新设备按钮
f5 = Button(show_r, text="刷新设备",command=pressF5)
f5.pack(pady=5)

frm = Frame(show_r)
frm_L = Frame(frm)
frm_R = Frame(frm)
frm.pack()
frm_L.pack(side=LEFT)
frm_R.pack(side=RIGHT)

# 右侧3个设备标签
label_1 = Label(frm_L, text="设备1",width=8,height=1)
label_2 = Label(frm_L, text="设备2",width=8,height=1)
label_3 = Label(frm_L, text="设备3",width=8,height=1)
label_1.pack(pady=20)
label_2.pack(pady=20)
label_3.pack(pady=20)

# 右侧3个安装标签
button_1 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_1)
button_1.pack(pady=16,padx=10)
button_2 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_2)
button_2.pack(pady=18,padx=10)
button_3 = Button (frm_R, text="安装",width=8,height=1,command=pressButton_3)
button_3.pack(pady=18,padx=10)







top.mainloop()