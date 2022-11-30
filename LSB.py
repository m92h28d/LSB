from matplotlib import pyplot as plt
import cv2 as cv
import math
import time
st = time.time()

secret_text = "GeeksforGeeks"
bitStream = ''.join(format(ord(i), '08b') for i in secret_text) 

hid=0
image = cv.imread('baboon.png',0)
im=image.copy()
difSeq=0*image.copy()
h,w=image.shape
for i in range(h):
    for j in range(w):
        if hid<len(bitStream):
            a1=image[i][j]
            bindata = format(a1, '08b')
            bindata=bindata[0:7] + bitStream[hid]
            a2=int(bindata,2)
            image[i][j]=a2
            hid+=1
            difSeq[i][j]=(a2-a1)**2
mse=0     
for i in range(h):
    for j in range(w):    
        mse+=difSeq[i][j] 
     
mse =mse/(h*w)
print(mse)  
print( 10*(math.log10((255**2)/mse) ))
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


hist1  = cv.calcHist([image],[0],None,[256],[0,256])
hist2  = cv.calcHist([im],[0],None,[256],[0,256])

plt.figure('hist')
plt.plot(hist2)
plt.plot(hist1)
plt.show()

plt.figure('LSB')
plt.imshow(image,cmap='gray', vmin=0, vmax=255)
plt.show()

plt.figure('Original')
plt.imshow(im,cmap='gray', vmin=0, vmax=255)
plt.show()


#cv.imshow('LSB', image)
#cv.imshow('Original', im)
#cv.waitKey(0)
