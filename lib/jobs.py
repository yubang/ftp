#coding:UTF-8

"""
业务处理模块，不涉及底层实现
@author:yubang
2015-05-01
"""

from lib import core

def init():
    "封装ftp服务器信息"
    obj=core.Client()
    
    ftpHost=raw_input("请输入ftp主机：")
    ftpPort=int(raw_input("请输入ftp端口："))
    
    obj.connectServer(ftpHost,ftpPort)
    return obj


def destroy(obj):
    "释放连接"
    obj.closeConnection()

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
