# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 13:50:19 2018

@author: Shubham
"""

import os
import sys
import codecs
from langdetect import detect
def process(lines,filename):
    c=0
    hin=0
    eng=0
    d=0
    outputFile = codecs.open("otherLang/"+filename, "w+", "utf-8")
    outputFile.write('id \t user_id \t date \t text\n')
    outputFile2 = codecs.open("hindi/"+filename, "w+", "utf-8")
    outputFile2.write('id \t user_id \t date \t text\n')
    outputFile1 = codecs.open("english/"+filename, "w+", "utf-8")
    outputFile1.write('id \t user_id \t date \t text\n')
    outputFile3 = codecs.open("error/"+filename, "w+", "utf-8")
    outputFile3.write('id \t user_id \t date \t text\n')
    print(len(lines))
    for i in lines[:]:
        if(len(i)>10):
            s=i.split('\t')
            try:
                if(detect(s[3])=='hi'):
                    outputFile2.write(i+"\n")
                    hin=hin+1
                elif(detect(s[3])=='en'):
                    outputFile1.write(i+"\n")
                    eng=eng+1
                else:
                    c=c+1
                    outputFile.write(i+"\n")
            except:
                d=d+1
                outputFile3.write(i+"\n")
    outputFile.close()
    outputFile1.close()
    outputFile2.close()
    outputFile3.close()
    print(filename+" "+str(hin)+" "+str(eng)+" "+str(c)+" "+str(d))
for filename in os.listdir(os.getcwd()+'\IndianData'):
    #print(filename)
    with open(os.getcwd()+"\IndianData/"+filename,'r', encoding="utf-8") as f:
        lines = f.readlines()
        #print(filename+'\t\t'+str(int(len(lines)/2)))
        process(lines,filename)
        
    