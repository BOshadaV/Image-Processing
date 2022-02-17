# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:33:08 2021

@author: Asus
"""
from datetime import datetime#import datetime library
start=datetime.now()#calling now attribute from datetime

import skimage.io as sk #import skimage.io library as sk
import matplotlib.pyplot as plt #import matplotlib.pyplot library
import numpy as np #import numpy library as np

img=sk.imread('sampleFiles/ouc_pg_convocation.jpg') #load image from a url

R=img[:,:,0] #abstract red channel from the image
G=img[:,:,1] #abstract green channel from the image
B=img[:,:,2] #abstract blue channel from the image

plt.figure() #a plot figure is created
plt.imshow(R, cmap='Reds') #the red channel image was displayed

plt.figure() #a plot figure is created
plt.imshow(G, cmap='Greens') #the green channel image ws displayed

plt.figure() #a plot figure is created
plt.imshow(B, cmap='Blues') #the blue channel was displayed

rot_90=np.rot90(img) #image was rotated by 90 degrees
plt.figure() #a plot is created
plt.imshow(rot_90) #the rotated imaged is displayed

rot_180=np.rot90(img,2) #the image was rotated by 180 degrees
plt.figure() #a figure was created
plt.imshow(rot_180) #the 180 degree roated image was displayed

rot_270=np.rot90(img,3) #the image was rotated by 270 degrees
plt.figure() #a figure was created
plt.imshow(rot_270) #the 270 degree roated image was displayed

flip_hr=np.fliplr(img) #the image was horizontally flipped
plt.figure() #a figure was created
plt.imshow(flip_hr) #the flipped image was displayed

flip_ver=np.flipud(img) #the image was vertically flipped
plt.figure() #a figure was created
plt.imshow(flip_ver) #the vertically flipped image was displayed

moon=sk.imread('sampleFiles/moon.jpg') #the moon image was loaded
dark_sky=sk.imread('sampleFiles/dark_sky.jpg') #the dark sky image was loaded

plt.figure() #a figure is created
plt.hist(moon.ravel(), bins=255, color='k') #the histogram of moon is displayed

plt.figure() #a figure is created
plt.hist(dark_sky.ravel(), bins=255, color='k') #the histogram of dark sky waas displayed

ouc_pg_convocation=sk.imread('sampleFiles/ouc_pg_convocation.jpg') #the our pg convocation image was loaded
R_img=ouc_pg_convocation[:,:,0] #the red channel was extracted from the image
G_img=ouc_pg_convocation[:,:,1] #the green channel was extracted from the image
B_img=ouc_pg_convocation[:,:,2] #the blue channel was extracted from the image
plt.figure() #a figure was created
plt.hist(R_img.ravel(),bins=255, color='r') #the histogram of red channel was displayed
plt.figure() #a figure was created
plt.hist(G_img.ravel(),bins=255, color='g') #the histogram of green channel was displayed
plt.figure() #a figure was created

print(datetime.now()-start) #the run time duration was printed