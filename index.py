#coding:UTF-8


"""
计算机网络课程设计
@author:yubang
2015-04-23
"""


from lib import jobs
import os,platform

def init():
    "主方法"
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")
        
    jobs.baseOption()
    
    
if __name__ == "__main__":
    init()
