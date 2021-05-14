import cv2
img = cv2.imread('saat.jpg')

#cv2.imshow('saat',img)

print(img[80,80]) # 80 e 80 noktasındaki değerleri gösterir mavi yeşil ve kırmızı değeri gösterir
img[80,80]=[255,255,255] # o noktadaki pikselin değerini değştirdik ve o noktada beyaz renk oluştu

bolge = img[30:120,100:200]
img[70:160,0:100] = bolge #resmin bu kordinatlarına aldığımız bolgedeki kısmı tekrar koyuyoruz
#img[30:120, 100:200] = [255,255,255] # bu kısım full beyaz olur
cv2.rectangle(img,(100,30),(200,120),(0,255,255),2)# resmin bu kısmına sarı renkte bi diktörtgen koyar,bölge kısmı büyüklüğünde yaptık.son 2 kalınlık

cv2.imshow('saat',img)
cv2.imshow('saat2',bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()