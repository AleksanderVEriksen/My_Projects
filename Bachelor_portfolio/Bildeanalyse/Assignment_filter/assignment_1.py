# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:40:04 2022

@author: eriks
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Lena-Gray-3.png')

img = np.array(img)

Gaussian = cv2.GaussianBlur(img,(5,5),0)

def Laplacian(image):
    
    out = np.zeros(image.shape, dtype=np.float)
    
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            dx = (image[i,j+1] - 2*image[i,j] + image[i,j-1])
            #print(dx, " = ",image[i,j+1], "-" ,2*image[i,j], "+", image[i,j-1])
            dy = (image[i+1,j] - 2*image[i,j] + image[i-1,j])
            out[i,j] = dx + dy
            #print(out[i,j], " = ", dx, " + ",dy)
    
    return out

def addFilter(image, laplacian):
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            image[i,j] = image[i,j] + laplacian[i,j]
    return image


Lap_gaus = Laplacian(Gaussian)
Lap_img = Laplacian(img)

fig = plt.figure()
ax1 = fig.add_subplot(121)  
ax2 = fig.add_subplot(122) 
ax1.imshow(img.astype('uint8'))
ax2.imshow(Lap_img.astype('uint8'))

fig2 = plt.figure()
ax1 = fig2.add_subplot(121) 
ax2 = fig2.add_subplot(122) 
ax1.imshow(Gaussian.astype('uint8'))
ax2.imshow(Lap_gaus.astype('uint8'))





