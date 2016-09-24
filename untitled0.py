# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 04:40:06 2016

@author: ad
"""

File = open("./sample.txt","r") #開啟文字檔
Text = File.read()
Text = Text.lower()
File.close()

sampleWordList = []
marklist = [".","!","?",",","—","\"","\n"]
for mark in marklist:      #去除標點符號
    Text = Text.replace(mark," ")
        
Text = Text.split(" ")
for A in Text:
    if len(A)>5:
        sampleWordList.append(A)

print (sampleWordList)




enter = input(" Please enter a word : ")
if len(enter) < 5:
    print (" You should enter more than five characters! \n")
   
elif enter in sampleWordList:
    print (" The word you entered exists!\n ")
        
else:
    print (" The word you entered did not exist.\n ")