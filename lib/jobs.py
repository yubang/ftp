#coding:UTF-8

"""
业务处理模块，不涉及底层实现
@author:yubang
2015-05-01
"""

import re
from lib import core


def init():
    "封装ftp服务器信息"
    obj=core.Client()
    
    ftpHost=raw_input("请输入ftp主机：")
    ftpPort=int(raw_input("请输入ftp端口："))
    
    ftpUser=raw_input("请输入ftp用户名（匿名输入ftp）：")
    ftpPassword=raw_input("请输入ftp密码（匿名输入ftp）：")
    
    obj.connectServer(ftpHost,ftpPort,ftpUser,ftpPassword)
    return obj


def destroy(obj):
    "释放连接"
    obj.closeConnection()

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
            print obj.sendCommand(re.sub(r'^[cC][dD]',"CWD",option).encode("UTF-8")+"\r\n")
        elif option == "pwd":
            #打印当前目录
            print obj.sendCommand("PWD \r\n")
        elif re.search(r'^[mM][kK][dD][iI][rR]\s.+',option):
            #创建目录
            print obj.sendCommand(re.sub(r'^[mM][kK][dD][iI][rR]','MKD',option).encode("UTF-8")+"\r\n")
        elif re.search(r'^[rR][mM][dD][iI][rR]\s.+',option):
            #删除目录
            print obj.sendCommand(re.sub(r'^[rR][mM][dD][iI][rR]','RMD',option)+"\r\n")
        elif re.search(r'^[rR][mM]\s.+',option):
            #删除文件
            print obj.sendCommand(re.sub(r'^[rR][mM]','DELE',option)+"\r\n")       
        
    destroy(obj)
    

def uploadFile():
    "上传文件到ftp服务器"
    obj=init()
    
    sourcePath=raw_input("请输入原文件路径：")
    targetPath=raw_input("请输入目标文件路径：")
    obj.uploadFile(sourcePath,targetPath)
    
    destroy(obj)

def downloadFile():
    "从ftp服务器下载文件"
    obj=init()
    targetPath=raw_input("请输入ftp文件路径：")
    obj.downloadFile(targetPath)
    destroy(obj)    

def debug():
    "调试使用"
    obj=core.Client()
    obj.connectServer("127.0.0.1",21)
    #obj.downloadFile("/upload/plan/123/434/543/fes/plan.doc")
    #obj.uploadFile("download/1","/upload/plan/123/434/543/fes/plan.doc")
