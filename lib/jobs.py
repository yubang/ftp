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
    print u"上传"
    destroy(obj)
    

def debug():
    "调试使用"
    obj=core.Client()
    obj.connectServer("127.0.0.1",21)
    obj.downloadFile("/upload/plan.doc")
