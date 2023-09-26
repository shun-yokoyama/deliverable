#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:36:17 2023

@author: shun-yokoyama
"""
import os
import glob
from natsort import natsorted

def change_folder_name(folder_path, new_name):
    
    folder_and_file = os.listdir(folder_path)
    sorted_list = natsorted(folder_and_file)
    
    for num, path in enumerate(sorted_list):
        
        old_folder_name = os.path.join(folder_path, path)
        new_folder_name = folder_path + '/' + new_name + format(num, 'd')
        
        if os.path.isdir(old_folder_name):
            
            os.rename(old_folder_name, new_folder_name)
    
    return 'complete'
        
        
        
def change_file_name(folder_path, old_name, new_name):
    
    name_split = old_name.split('.')
    if len(name_split) > 1:
        #拡張子取得
        extension = name_split[-1]
    else:
        raise Exception("拡張子まで含めたファイル名を指定してください．")
        
    folder_and_file = os.listdir(folder_path)
    sorted_list = natsorted(folder_and_file)
    
    for num, sorted_name in enumerate(sorted_list):
        
        folder_or_file = os.path.join(folder_path, sorted_name)
        
        #フォルダ>フォルダ>ファイルの順で構成されている場合
        if os.path.isdir(folder_or_file):
        
            old_folder_name = folder_or_file
            old_file_name = glob.glob(old_folder_name + '/' + old_name)
            new_file_name = old_folder_name + '/' + new_name + format(num, 'd') + str('.') + extension
            
            for old in old_file_name:
                if os.path.isfile(old):
                    
                    os.rename(old, new_file_name)
                    
        #フォルダ>ファイルの順で構成されている場合            
        elif os.path.isfile(folder_or_file):
            
            old_file_name = folder_or_file
            new_file_name = folder_path + '/' + new_name + format(num, 'd') + str('.') + extension
            os.rename(old_file_name, new_file_name)
                    
    return 'complete'

##############################以下で条件を指定################################
#フォルダ名を変更する際に指定する
folder_path = "フォルダのパスを指定する"
new_folder_name = '新たなフォルダのkeyを指定する'

print(change_folder_name(folder_path, new_name = new_folder_name))

#ファイル名を変更する際に指定する
file_path = "ファイルのパスを指定する"
old_file_name = '*.jpg'
new_file_name = '新たなkeyを指定する'

print(change_file_name(file_path, old_name = old_file_name, new_name = new_file_name))