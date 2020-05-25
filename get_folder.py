# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:57:54 2020

@author: Administrator
"""

import os
import sys
def getALLFromFolder(folder):
    folderList = []
    if not os.path.exists(folder):
        print("{} not exixts".format(folder))
        return
    if os.path.isfile(folder):
        folderList.append(folder)
        return folderList
    dirs = os.listdir(folder)
    for dir in dirs:
        if os.path.isfile(dir):
            absFile = "{}{}{}".format(folder,os.sep,dir)            
            folderList.append(absFile)
        else :
            newFolder = "{}{}{}".format(folder,os.sep,dir)
            folderList.extend(getALLFromFolder(newFolder))
    return folderList

def begin():
    folder = "F:\\工作学习\\数据工程师"
    allFiles = getALLFromFolder(folder)
    if not allFiles:
        print("please check the folder")
        sys.exit(0)
    resFile = "C:\\Users\\Administrator\\Desktop\\result.txt"
    with open(resFile,'w') as f:
        for file in allFiles:
            f.write(file+"\n")
    print("done.")


if __name__ == '__main__':
    begin()