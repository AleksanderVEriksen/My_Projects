# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:33:00 2022

@author: eriks
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
import glob

def imagesToBlur(path):
  gg = []
  for file in glob.glob(path):
    a = cv2.imread(file)
    gg.append(a)
  return np.copy(gg)



Blur_Test = imagesToBlur("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Color//test//images//*.*")
Blur_Train = imagesToBlur("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Color//train//images//*.*")
Blur_Val = imagesToBlur("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Color//valid//images//*.*")


Blur_train_sample = np.zeros(Blur_Train.shape)
Blur_test_sample = np.zeros(Blur_Test.shape)
Blur_valid_sample = np.zeros(Blur_Val.shape)


for imgs in range(0,len(Blur_Train)):
  Blur_train_sample[imgs] = cv2.GaussianBlur(Blur_Train[imgs], (5,55),0)
for imgs in range(0,len(Blur_Test)):
  Blur_test_sample[imgs] = cv2.GaussianBlur(Blur_Test[imgs], (5,55),0)
for imgs in range(0,len(Blur_Val)):
  Blur_valid_sample[imgs] = cv2.GaussianBlur(Blur_Val[imgs], (5,55),0)
  

for x in range(0,len(Blur_train_sample)):
  status = cv2.imwrite("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Blur//train//"+"train"+str(x)+".PNG",Blur_train_sample[x])

for x in range(0,len(Blur_test_sample)):
  status = cv2.imwrite("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Blur//test//"+"test"+str(x)+".PNG",Blur_test_sample[x])

for x in range(0,len(Blur_valid_sample)):
  status = cv2.imwrite("C://Users//eriks//OneDrive//Skrivebord//Cat_dataset//Blur//valid//"+"valid"+str(x)+".PNG",Blur_valid_sample[x])
