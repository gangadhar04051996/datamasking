# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:50:55 2020

@author: tilak
"""

import subprocess
import os
import pandas as pd
import cryptography

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
        return df
    
    def encryptcsvfile(self,name=""):
        
        if name == "" :
            raise Exception("Empty csv path exception")
            return
        
        df = pd.read_csv(path)
        return
        
    def __checkdataspread__(self,df):
        #check the dataframe data spread in this function
        columns = df.columns
        for i in columns:
            
            keys = df[i].value_counts().keys().tolist()
            vals = df[i].value_counts().tolist()
            hofdf = len(df[i])/10  #10% of len
            if len(vals) < hofdf:
                colmune =encryptcolumn(df[i])
                df[i]= columne
        return df
                
    def __encryptcolumn__(self,df):
        #encrypt the column and return 
        
        return df
    
    def __decryptcolumn__(self,df):
        
        #need to check if using a public private key architecture
        return df
            
            
        
        
    
    

