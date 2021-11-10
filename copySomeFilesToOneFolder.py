# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:31:24 2020

@author: hx
@功能   : 将不同文件下的文件拷贝到同一个目录下
@缺陷   : 文件同名会覆盖
          目标文件夹不能在源文件夹下
          执行一次copy一次，已copy的不会略过
"""

import shutil
import os
import sys

#遍历文件夹下所有文件，返回包含文件绝对路径的list
def get_all_files(file_path):
    files = []
    for file in os.listdir(file_path):
        abs_file = '{}{}{}'.format(file_path,os.sep,file)
        if os.path.isdir(abs_file):            
            files.extend(get_all_files(abs_file))
        else:
            files.append(abs_file)
    return files
    
def begin():
    src_folder = 'F:\\工作学习\\操作系统'
    if not os.path.exists(src_folder):
        print('文件夹不存在:{}'.format(src_folder))
        sys.exit(0)
    tar_folder = 'F:\\工作学习\\操作系统_合并'
    if not os.path.exists(tar_folder):
        print('文件夹不存在:{},将自动创建'.format(tar_folder))
        os.makedirs(tar_folder)
    files = get_all_files(src_folder)
    if files is None or len(files) == 0:
        print('没有查询到文件:{}'.format(src_folder))
        return
    print('共{}文件'.format(len(files)))
    for file in files :
        file_name = file.split(os.sep)[-1]
        tar_file = '{}{}{}'.format(tar_folder,os.sep,file_name)
        #print('src:{},tar:{}'.format(file,tar_file))
        #break
        shutil.copyfile(file,tar_file)
        



if __name__ == '__main__':
    begin()