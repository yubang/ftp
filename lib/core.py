#coding:UTF-8


"""
ftp客户端实现核心方法
@author:yubang
2014-04-23
"""

import socket,re,time


class Client(object):
    def __init__(self):
        print u"初始化对象"
        self.__fileSocket=None
    def __del__(self):
        print u"对象回收"
    def __initConnect(self):
        "初始化连接"
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((self.__ftpHost, self.__ftpPort))
    def __sendCommand(self,command):
        "发送指令到ftp服务器"
        self.__socket.send(command)
        data=self.__socket.recv(255).strip()
        data=self.__dealMessage(data)
        print u"服务器返回信息：",data['message']
        return data
    def __port(self):
        "主动模式"
        pass
    def __pasv(self):
        "被动模式"
        if self.__fileSocket != None:
            self.__fileSocket.close()
        #尝试以被动模式连接ftp
        ip,port=self.__getPortAndIp(self.__sendCommand("PASV\r\n")['message'])
        print u"连接",ip,":",port
        self.__fileSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__fileSocket.connect((ip,port))
        
    def __login(self):
        "登录ftp服务器"
        print u"尝试连接到ftp服务器"
        data=self.__socket.recv(255).strip()
        data=self.__dealMessage(data)
        
        #尝试登陆
        self.__sendCommand("USER FTP\r\n")
        if self.__sendCommand("PASS FTP\r\n")['status'] != 2:
            print u"密码不正确！"
            exit()
        
        self.__sendCommand("PWD\r\n")
        
        #被动模式
        self.__pasv()
        self.__sendCommand("LIST\r\n")
        print self.__socket.recv(255).strip()
        
                
    def __dealMessage(self,data):
        "处理ftp服务器返回的信息"
        datas={}
        datas['status']=int(data[0])
        datas['infoType']=int(data[1])
        datas['infoMessage']=int(data[2])
        datas['message']=data[4:len(data)]
        return datas
    def __getPortAndIp(self,data):
        "获取被动监听的ip和端口"
        d=re.search(r'[\d]+,[\d]+,[\d]+,[\d]+,[\d]+,[\d]+',data).group()
        d=d.split(",")
        d=map(int,d)
        
        return str(d[0])+"."+str(d[1])+"."+str(d[2])+"."+str(d[3]),d[4]*256+d[5]
        
    def connectServer(self,ftpHost,ftpPort):
        "连接ftp服务器，显式调用"
        self.__ftpHost=ftpHost
        self.__ftpPort=ftpPort
        self.__initConnect()
        self.__login()
    def closeConnection(self):
        "关闭与ftp服务器的连接，显式调用"
        self.__socket.close()
        self.__fileSocket.close()
