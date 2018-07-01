# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:54:35 2018

@author: Shubham
"""


import os
import sys
import frds
import codecs
def process(lines,filenames):
    with open(os.getcwd()+"\Friends/"+filename, "w+", encoding='utf-8') as temp:
        s1=set()
        for i in lines[:]:
            if(len(i)>30):
                s=i.split('\t')
                s1.add(str(s[1]))
        #print(s1)
        for i in lines[:]:
            if(len(i)>30):
                s=i.split('\t')
                temp.write(str(s[1])+":\t")
                li=frds.friends(s[1])
                print(len(li))
                for item in li:
                    print("%s\t" % item)
                    if(item in s1):
                        temp.write(str(item))
                        print("%s\t" % item)
                temp.write("\n")
                
for filename in os.listdir(os.getcwd()+'/indian Rumor'):
    #print(filename)
    with open("./indian Rumor/"+filename,'r', encoding="utf-8") as f:
        lines = f.readlines()
        print(filename+'\t\t'+str(int(len(lines)/2)))
        process(lines,filename)