# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 00:44:48 2016

@author: ad
"""
height = input("請輸入你的身高： ")

if int(height) > 130:
    print("請購票後進入遊樂區")
else:
    print("免購票，但請由大人陪同進入遊樂區。")

while True:# HW 1-2
	key = input("Please key in the word : ")
	if len(key) < 5:
		print("Please key in the word with more than five characters\n")
		continue
	if key in sampleWordList:
		print("The word is in the sampleWordList.\n")
	else:
		print("The word is NOT in the sampleWordList.\n")
  
  
  
  while True:
    if len(enter)<5:
        print (" You should enter more than five characters! ")
        continue

    elif enter in sampleWordList:
        print (" The word you entered exists! ")
        break
        
    else:
        print (" The word you entered did not exist. ")
        
a= 0
print (a)
        
