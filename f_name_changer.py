#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:36:17 2023

@author: shun-yokoyama
"""
import os
import re
import glob


def change_folder_name(folder_path, new_name):
    
    folder_and_file = os.listdir(folder_path)
    sorted_list = sorted(folder_and_file, key=lambda x: int(re.search(r'\d+', x).group()))
    
    for num, path in enumerate(sorted_list):
        
        old_folder_name = os.path.join(folder_path, path)
        new_folder_name = folder_path + '/' + new_name + format(num, 'd')
        
        if os.path.isdir(old_folder_name):
            
            os.rename(old_folder_name, new_folder_name)
    
    return 'complete'
        
        
        
def change_file_name(folder_path, old_name, new_name):
    
    folder_and_file = os.listdir(folder_path)
    sorted_list = sorted(folder_and_file, key=lambda x: int(re.search(r'\d+', x).group()))
    print(sorted_list)

    
    for num, sorted_name in enumerate(sorted_list):
        
        folder_or_file = os.path.join(folder_path, sorted_name)
        
        #フォルダ>フォルダ>ファイルの順で構成されている場合
        if print(os.path.isdir(folder_or_file)):
        
            old_folder_name = folder_or_file
            old_file_name = glob.glob(old_folder_name + '/' + old_name)
            new_file_name = old_folder_name + '/' + new_name + format(num, 'd') + '.bmp'
            
            for old in old_file_name:
                if os.path.isfile(old):
                    
                    os.rename(old, new_file_name)
                    
        #フォルダ>ファイルの順で構成されている場合            
        elif os.path.isfile(folder_or_file):
            
            old_file_name = folder_or_file
            new_file_name = folder_path + '/' + new_name + format(num, 'd') + '.bmp'
            os.rename(old_file_name, new_file_name)
                    
            
    return 'complete'

##############################以下で条件を指定################################
folder_path = '名前を変更したいフォルダのパスを指定'
file_path = '名前を変更したいファイルのパスを指定'
#現在のファイル名の型
#(例) image1.png~image100.png --> image*.png
old_file_name = '現在のファイル名'

print(change_folder_name(folder_path, new_name = 'folder'))
print(change_file_name(file_path, old_name = old_file_name, new_name = 'file'))
#############################################################################
#上記の例でフォルダ100個に対して実行するとフォルダ名はfolder0~folder99
#100個のファイルに対して実行するとファイル名はfile0~file99となる．
##############################################################################