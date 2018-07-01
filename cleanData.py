# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 11:11:08 2018

@author: Shubham
"""

import os
import preprocessor as p

import os
import sys
def process(lines,filenames):
    with open(os.getcwd()+"\IndianData/"+filename, "w+", encoding='utf-8') as temp:
        s1=set()
        for i in lines[:]:
            if(len(i)>30):
                s=i.split('\t')
                s1.add(str(s[1]))
        #print(s1)
        for i in lines[:]:
            if(len(i)>30):
                s=i.split('\t')
                temp.write(s[0]+'\t'+s[1]+"\t"+s[2]+'\t'+p.clean(s[3])+'\n')
                
for filename in os.listdir(os.getcwd()+'/indian Rumor'):
    #print(filename)
    with open("./indian Rumor/"+filename,'r', encoding="utf-8") as f:
        lines = f.readlines()
        print(filename+'\t\t'+str(int(len(lines)/2)))
        process(lines,filename)