                                                   # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
tmp_path = 'C:\\Users\\hanxu\\Desktop\\tmp'
src_files = os.listdir(tmp_path)
for file in src_files :
    print('{}{}{}'.format(tmp_path,os.sep,file))
'''

import shutil
import os
from PyPDF2 import PdfFileReader,PdfFileWriter
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams

def split_pdf():
    src_path = 'C:\\Users\\hanxu\\Desktop\\src\\'
    tar_path = 'C:\\Users\\hanxu\\Desktop\\tmp\\'
    src_file_names = os.listdir(src_path)
    if 0 == len(src_file_names):
        print('{}空文件夹'.format(src_path))
        return
    for src_file_name in src_file_names:
        src_file = '{}{}'.format(src_path,src_file_name)
        f = open(src_file,'rb')
        pdf_reader = PdfFileReader(f)
        pages_nums = pdf_reader.numPages
        print('文档 : "{}"\t开始拆分'.format(src_file_name))
        print('文档 : "{}"\t总页数:{}'.format(src_file_name,pages_nums))
        for cur_pdf_num in range(1, pages_nums + 1):
            tar_file_name = src_file_name.replace('.pdf','_{}.pdf'.format(cur_pdf_num))
            tar_file = '{}{}'.format(tar_path,tar_file_name)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(cur_pdf_num-1))
            pdf_writer.write(open(tar_file, 'wb'))
            print('文档 : ”{}“\t第{}页: -> : {}'.format(src_file_name,cur_pdf_num,tar_file_name))
        f.close()

def read_pdf(file_name):
    if not os.path.exists(file_name):
        print('{}文件不存在'.format(file_name))
        return {'src_name':file_name,'tar_file':'','company':''}
    f = open(file_name,'rb')
    praser = PDFParser(f)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()
    if not doc.is_extractable:
        print('{} error'.format(file_name))
        f.close()
        return {'src_name':file_name,'tar_file':'','company':''}
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        i=0
        tar_file = ''
        company = ''
        for x in layout:
            i = i+1
            if (isinstance(x, LTTextBoxHorizontal)):
                if i == 2 :
                    tar_file = x.get_text().split('：')[1].strip()
                if i == 3 :
                    company = x.get_text().split('：')[0]
                if i == 3 :
                    continue
    f.close()
    return  {'src_name':file_name,'tar_file':tar_file,'company':company}



def rename_pdf():
    src_path = 'C:\\Users\\hanxu\\Desktop\\tmp\\'
    tar_path = 'C:\\Users\\hanxu\\Desktop\\tar\\'
    src_file_names = os.listdir(src_path)
    if 0 == len(src_file_names):
        print('{}空文件夹'.format(src_path))
        return
    for src_file_name in src_file_names:
        src_file = '{}{}'.format(src_path,src_file_name)
        tar_file_name = read_pdf(src_file)['tar_file']
        if tar_file_name is None or tar_file_name == '':
            print('请检查文档是否有错误:{}'.format(src_file))
            continue
        tar_file = '{}{}{}'.format(tar_path,tar_file_name,'.pdf')
        print('重命名：{}->{}'.format(src_file_name,tar_file_name))
        shutil.copyfile(src_file,tar_file)

def read_pdf2(file_name):
    if not os.path.exists(file_name):
        print('{}文件不存在'.format(file_name))
        return {'src_name':file_name,'tar_file':'','company':''}
    f = open(file_name,'rb')
    praser = PDFParser(f)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()
    if not doc.is_extractable:
        print('{} error'.format(file_name))
        f.close()
        return {'src_name':file_name,'tar_file':'','company':''}
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    i=0
    for page in doc.get_pages():
        need_page = 12
        i = i+1
        if need_page > i:
            continue
        print("第{}页".format(i))
        interpreter.process_page(page)
        layout = device.get_result()
        j=0
        for x in layout:
            j = j+1
            #print("第{}行".format(j))
            if (isinstance(x, LTTextBoxHorizontal)):
                print(x)
                #print(x.get_text())
        if need_page <= i:
            break
    f.close()
    #return  {'src_name':file_name,'tar_file':tar_file,'company':company}

def begin():
    read_pdf2("C:\\Users\\Administrator\\Desktop\\aa.pdf")
    #split_pdf()
    #rename_pdf()



if __name__ == '__main__':
    begin()





