#coding:UTF-8


"""
计算机网络课程设计
@author:yubang
2015-04-23
"""


from lib import jobs
import os

def init():
    "主方法"
    os.system("clear")
    while True:
        
        print u"0.退出程序"
        print u"1.打开远程ftp连接"
        print u"2.上传文件到ftp服务器"
        print u"3.从ftp服务器下载文件"
        command=raw_input("请输入序号以选择功能：")
        if command == "0":
            break
        elif command == "1":
            print u"建立连接\n"
        elif command == "2":
            jobs.uploadFile()
        elif command == "3":
            jobs.downloadFile()
        else:
            print u"无效命令请重新输入\n"
    print u"程序已经退出！"
    
    
if __name__ == "__main__":
    #jobs.debug()
    init()
