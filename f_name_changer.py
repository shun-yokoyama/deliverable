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
        
        #フォルダ>フォルダ>ファイルの場合
        if print(os.path.isdir(folder_or_file)):
            print("folder")
            old_folder_name = folder_or_file
            old_file_name = glob.glob(old_folder_name + '/' + old_name)
            new_file_name = old_folder_name + '/' + new_name + format(num, 'd') + '.bmp'
            #print(str(old_file_name))
            for old in old_file_name:
                if os.path.isfile(old):
                    print('ok')
                    os.rename(old, new_file_name)
                    
        #フォルダ>ファイルの場合            
        elif os.path.isfile(folder_or_file):
            
            old_file_name = folder_or_file
            new_file_name = folder_path + '/' + new_name + format(num, 'd') + '.bmp'
            os.rename(old_file_name, new_file_name)
            print('ok')
                    
            
    return 'complete'

folder_path = 'E:\Fujita Lab\舌診断研究データ\Segmentation(舌本体)/mask'
folder_path1 = 'E:\Fujita Lab\舌診断研究データ\Segmentation(舌本体)/train_data/train1'
folder_path2 = 'E:\Fujita Lab\舌診断研究データ\Segmentation(舌本体)/train_data/train2'
folder_path3 = 'E:\Fujita Lab\舌診断研究データ\Segmentation(舌本体)/train_data/train3'
old_name1 = 'image*.bmp'
old_name2 = '*.bmp'

print(change_folder_name(folder_path1, new_name = 'images'))
print(change_folder_name(folder_path2, new_name = 'images'))
print(change_folder_name(folder_path3, new_name = 'images'))

print(change_file_name(folder_path1, old_name = old_name1, new_name = 'image'))
print(change_file_name(folder_path1, old_name = old_name2, new_name = '3ch_teacher'))

print(change_file_name(folder_path2, old_name = old_name1, new_name = 'image'))
print(change_file_name(folder_path2, old_name = old_name2, new_name = '3ch_teacher'))

print(change_file_name(folder_path3, old_name = old_name1, new_name = 'image'))
print(change_file_name(folder_path3, old_name = old_name2, new_name = '3ch_teacher'))

print(change_file_name(folder_path, old_name = old_name2, new_name = 'mask'))