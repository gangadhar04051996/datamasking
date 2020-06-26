# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:50:55 2020

@author: tilak
"""

import subprocess
import os
import pandas as pd

class Annonymise:
    def __init__(self,path=""):
        if path == "":
            raise Exception("Path Empty error")
            return
    
        path = path.replace("\\",'/')
        os.chdir(path)
        with open('commands.txt','r') as c:
            alpha = c.read().splitlines()
        
        for i in alpha:
            subprocess.call(i,shell=True)
    def encryptexcelfile(self,name="",sheet_name=""):
        
        if name == "" or sheet_name =="":
            raise Exception("Empty path exception")
            return
        
        df = pd.read_excel(path,sheet_name=sheet_name)
    
    def encryptcsvfile(self,name=""):
        
        if name == "" :
            raise Exception("Empty csv path exception")
            return
        
        df = pd.read_csv(path)
        
    def __checkdataspread__(df):
        #check the dataframe data spread in this function
        columns = df.columns
        
        
    
    

