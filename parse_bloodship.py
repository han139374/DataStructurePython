# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:18:35 2020

@author: Administrator
"""
import pandas as pd

def get_dep(df,target):
    deps = []
    temp_deps = df[df['target'] == '{}'.format(target)]['source'].tolist()
    if len(temp_deps) == 0:
        return deps
    for temp_dep in temp_deps:
        deps.append(temp_dep)
        if target == temp_dep:
            deps.remove(temp_dep)
            continue
        if temp_dep.split('.')[0] == 'ODS_IT_F':
            continue
        deps.extend(get_dep(df,temp_dep))
    return deps 
    
def begin():
    excel_name = 'C:\\Users\\Administrator\\Desktop\\table_bloodship.xlsx'
    df = pd.read_excel(excel_name)
    print(df)
    tars = ['GDS_D_IT.D_A','GDS_S_IT.S_C']
    for tar in tars:
        try:
            deps= get_dep(df,tar)
            print('{}:{}'.format(tar,str(deps)))
        except Exception as e:
            print('{}【】{}'.format(tar,e))
            pass


def get_lev_dep(df,target_info):
    deps = []
    lev = target_info[0]
    target = target_info[1]
    temp_deps = df[df['target'] == '{}'.format(target)]['source'].tolist()
    if len(temp_deps) == 0:
        return deps
    for temp_dep in temp_deps:
        temp_dep_info = [lev+1,temp_dep] 
        if target == temp_dep:
            continue
        deps.append(temp_dep_info)
        if temp_dep.split('.')[0] == 'ODS_IT_F':
            continue
        deps.extend(get_lev_dep(df,temp_dep_info))
    return deps 

def split_lev_dep(deps):
    dict_dep = {}
    if len(deps) == 0 :
        return dict_dep
    for dep in deps:
        lev = dep[0]
        dep_table = dep[1]
        if lev in dict_dep.keys():
            dict_dep[lev].append(dep_table)
        else:
            dict_dep[lev] = [dep_table]
    return dict_dep

def begin2():
    excel_name = 'C:\\Users\\Administrator\\Desktop\\table_bloodship.xlsx'
    new_excel_name = 'C:\\Users\\Administrator\\Desktop\\res.xlsx'
    df = pd.read_excel(excel_name)
    tars = ['GDS_D_IT.D_A','GDS_S_IT.S_C']
    dict_df = {}
    for tar in tars:
        try:
            deps= get_lev_dep(df,[0,tar])
            lev_deps = split_lev_dep(deps)
            new_df = pd.DataFrame()
            for key in sorted(lev_deps.keys()):
                new_df = pd.concat([new_df,pd.DataFrame({key:lev_deps[key]})],axis=1)
            dict_df[tar] = new_df.fillna('')
        except Exception as e:
            print('ERROR:{}:{}'.format(tar,e))
            pass        
    writer = pd.ExcelWriter(new_excel_name)
    for sheet in dict_df.keys():
        dict_df[sheet].to_excel(writer,index=[],sheet_name=sheet)
    writer.save()
    print('done')
    
    
if __name__ == '__main__':
    begin2()