# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:45:16 2020

@author: Administrator
"""

import re


def begin():
    old_str = 'col1 number(4,3),col2 varchar2(10),col3 number,col4 number(4,0)'
    new_str = re.sub(r'(\d),(\d)',r'\1@\2',old_str)
    print(new_str)

def begin2():
    def _replace(matched):
        m = matched.group()
        change = re.sub(',', '@', m)
        return change
    old_str = 'col1 number(4,3),col2 varchar2(10),col3 number,col4 time with zone,col5 number(4,0)'
    new_str = re.sub(r'\d,\d',_replace,old_str)
    for col in new_str.split(','):
        col_name = col.replace('@',',').split(' ')[0]
        col_type = str(col.replace('@',',').split(' ')[1:])
        print('col: {} {}'.format(col_name,col_type))


if __name__ == '__main__':
    begin2()























    
