#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog
import subprocess
import os
import re


 # 获得adb devices命令下设备信息
devices = str(os.popen("adb devices"))

# 获得设备 serial number
serial_nos = []
for item in devices.split():
    filters = ['list', 'of', 'device', 'devices', 'attached']
    if item.lower() not in filters:
        serial_nos.append(item)

# 点击安装按钮调用方法
def getFile():
    # filename = tkFileDialog.askopenfilename(initialdir ='/')
    p = os.popen("adb devices")
    a = p.read()
    deviceInfo = subprocess.check_output('adb devices -l')
    deviceName = re.findall(r'device product:(.*)\smodel', deviceInfo, re.S)[0]
    print a

    # sysInfo = subprocess.check_output('adb shell cat /system/build.prop')
    # androidVersion = re.findall("version.release=(\d\.\d)*", sysInfo, re.S)[0]
    # deviceInfo = subprocess.check_output('adb devices -l')
    # deviceName = re.findall(r'device product:(.*)\smodel', deviceInfo, re.S)[0]
    # print filename
    # print serial_nos
    # print androidVersion
    # print deviceName


def connectDevcie():
    '''''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        '''''获取设备列表信息，并用"\r\n"拆分'''
        deviceInfo = subprocess.check_output('adb devices').split("\r\n")
        '''''如果没有链接设备或者设备读取失败，第二个元素为空'''
        if deviceInfo[1] == '':
            return False
        else:
            return True
    except Exception, e:
        print "Device Connect Fail:", e


def getAndroidVersion():
    try:
        if connectDevcie():
            # 获取系统设备系统信息
            sysInfo = subprocess.check_output('adb shell cat /system/build.prop')
            # 获取安卓版本号
            androidVersion = re.findall("version.release=(\d\.\d)*", sysInfo, re.S)[0]
            return androidVersion
        else:
            return "Connect Fail,Please reconnect Device..."
    except Exception, e:
        print "Get Android Version:", e


def getDeviceName():
    try:
        if connectDevcie():
            # 获取设备名
            deviceInfo = subprocess.check_output('adb devices -l')
            deviceName = re.findall(r'device product:(.*)\smodel', deviceInfo, re.S)[0]
            return deviceName
        else:
            return "Connect Fail,Please reconnect Device..."
    except Exception, e:
        print "Get Device Name:", e



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




button_1 = Button (frm_R, text="安装",width=8,height=1,command=getFile)  # 输入框-用户名
button_1.pack(pady=16)
button_2 = Button (frm_R, text="安装",width=8,height=1)
button_2.pack(pady=18)
button_3 = Button (frm_R, text="安装",width=8,height=1)
button_3.pack(pady=18)







top.mainloop()

