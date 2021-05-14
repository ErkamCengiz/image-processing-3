import cv2
import numpy as np

img1= cv2.imread('resim.jpg')
img2= cv2.imread('logo.jpg')


#toplam = cv2.add(img1,img2)# iki resmi birleştirip çıkarır.
toplam = cv2.addWeighted(img1,0.8,img2,0.2,0)# hangi resmi daha baskın görmek istiyosak ona göre ayarlıyoruz.

cv2.imshow('toplam',toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()