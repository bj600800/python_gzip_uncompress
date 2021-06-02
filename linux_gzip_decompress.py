#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    zipfile.py      
# @Author:      Eric Dou        
# @Time:        2021/6/2 15:28 

"""Function: """

import gzip
import os
import shutil

path = r'F:\python_script_learning\test'
filelists = os.listdir(path)
for i in filelists:
    if os.path.isdir(os.path.join(path,i)):
        dirpath = os.path.join(path,i)
        gzfile = os.listdir(dirpath)
        if len(gzfile) == 1:
            for i in gzfile:
                with gzip.open(os.path.join(dirpath,i), 'rb') as f_in:
                    writefile = i.replace('.gz','.pdb')
                    with open(os.path.join(dirpath,writefile), 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)


