import cv2
import numpy as np

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('logo.jpg')


satir,sutun,kanal=img2.shape
roi=img1[0:satir,0:sutun]

im2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # SİYAH BEYAZ YAPAN FONKSİYON
ret, mask=cv2.threshold(im2gray,10,255,cv2.THRESH_BINARY)# TAMAMEN BÜTÜN DEĞELRİ SİYAH BEYAZ YAPTIRIR
mask_inv=cv2.bitwise_not(mask)#buda direk renkleri tersine çevirir beyazları siyah sihayları beyaz
cv2.imshow('tersi',mask_inv)
cv2.imshow('im',im2gray)
cv2.imshow('mask',mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)#mask_inv resminin  arka planına messinin arka planını koydu
cv2.imshow('maks_inv',img1_bg)

im2_fg = cv2.bitwise_and(img2,img2,mask=mask)
cv2.imshow('im2_fg',im2_fg)

son_fg = cv2.add(img1_bg,im2_fg)
img1[0:satir,0:sutun]=son_fg
cv2.imshow('son resim',img1)



cv2.waitKey(0)
cv2.destroyAllWindows()