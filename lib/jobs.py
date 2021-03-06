#coding:UTF-8

"""
业务处理模块，不涉及底层实现
@author:yubang
2015-05-01
"""

import re,os,platform
from lib import core


def init():
    "封装ftp服务器信息"
    obj=core.Client()
    
    print u"请输入ftp主机："
    ftpHost=raw_input()
    print u"请输入ftp端口："
    ftpPort=int(raw_input())
    
    print u"请输入ftp用户名（匿名输入FTP）："
    ftpUser=raw_input()
    print u"请输入ftp密码（匿名输入FTP）："
    ftpPassword=raw_input()
    
    obj.connectServer(ftpHost,ftpPort,ftpUser,ftpPassword)
    return obj


def destroy(obj):
    "释放连接"
    obj.closeConnection()

def appHelp():
    "输出帮助信息"
    print u""
    print u"--------------帮助---------------"
    print u"ls：列出当前目录文件列表"
    print u"cd 路径：切换工作路径"
    print u"pwd：打印工作路径"
    print u"mkdir 文件夹路径：创建文件夹"
    print u"rmdir 文件夹路径：删除文件夹"
    print u"rm 文件路径：删除文件"
    print u"clear：清屏"
    print u"upload 本地文件路径 服务器文件路径 ：上传文件"
    print u"download 服务器文件路径 ：下载文件"
    print u"quit：退出程序"
    print u"help：帮助"
    print u"--------------帮助---------------"
    print u""
    
    
def baseOption():
    "实现连接ftp服务器基本操作"
    obj=init()
    print u"输入help显示可用指令"
    while True:
        option=raw_input("请输入指令：")
        if option == "quit":
            #退出程序
            break
        elif option == "ls":
            #列出目录下的文件
            fps=obj.getFileList()
            for fp in fps:
                print fp
        elif re.search(r'^[cC][dD][\s].+',option):
            #切换目录
            result=obj.sendCommand(re.sub(r'^[cC][dD]',"CWD",option).encode("UTF-8")+"\r\n")
            if result['status'] == 2:
                print u"切换路径成功"
            else:
                print u"切换路径失败"
        elif option == "pwd":
            #打印当前目录
            result=obj.sendCommand("PWD \r\n")
            print u"当前路径：",result['message']
        elif re.search(r'^[mM][kK][dD][iI][rR]\s.+',option):
            #创建目录
            result=obj.sendCommand(re.sub(r'^[mM][kK][dD][iI][rR]','MKD',option).encode("UTF-8")+"\r\n")
            if result['status'] == 2:
                print u"创建目录成功"
            else:
                print u"创建目录失败"
        elif re.search(r'^[rR][mM][dD][iI][rR]\s.+',option):
            #删除目录
            result=obj.sendCommand(re.sub(r'^[rR][mM][dD][iI][rR]','RMD',option)+"\r\n")
            if result['status'] == 2:
                print u"删除目录成功！"
            else:
                print u"删除目录失败！"
        elif re.search(r'^[rR][mM]\s.+',option):
            #删除文件
            result=obj.sendCommand(re.sub(r'^[rR][mM]','DELE',option)+"\r\n")
            if result['status'] == 2 :
                print u"删除文件成功"
            else:
                print u"删除文件失败"       
        elif re.search(r'^[u][p][l][o][a][d]\s.+?\s.+',option):
            #上传文件
            strs=option.split(" ")
            obj.uploadFile(strs[1],strs[2])
        elif re.search(r'^[dD][oO][wW][nN][lL][oO][aA][dD]\s.+',option):
            #下载文件
            strs=option.split(" ")
            obj.downloadFile(strs[1])
        elif option == "help":
            #输出帮助信息
            appHelp()
        elif option == "clear":
            #清屏
            if platform.system() == "Linux":
                os.system("clear")
            else:
                os.system("cls")
        else:
            print u"你的输入有误，请重新输入！"
                
    destroy(obj)
    

def uploadFile():
    "上传文件到ftp服务器"
    obj=init()
    print u"请输入原文件路径："
    sourcePath=raw_input()
    print u"请输入目标文件路径："
    targetPath=raw_input()
    obj.uploadFile(sourcePath,targetPath)
    
    destroy(obj)

def downloadFile():
    "从ftp服务器下载文件"
    obj=init()
    print u"请输入ftp文件路径："
    targetPath=raw_input()
    obj.downloadFile(targetPath)
    destroy(obj)    


