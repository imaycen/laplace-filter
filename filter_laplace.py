from PIL import Image, ImageFilter
import cv2

#Kernel
#tamaño = (5,5)
#coeficientes = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2, 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
#Otro kernel para probar
tamaño = (3,3)
coeficientes = [0, -1, 0, -1, 4, -1, 0, -1, 0]
 
factor = 1
 
imagen_original = Image.open('lena.png')
img1 = cv2.imread('lena.png')

#Funcion en Python que determina el Laplaciano
imagen_procesada = imagen_original.filter(ImageFilter.Kernel(tamaño, coeficientes, factor))
 
#se graba el resultado 
imagen_procesada.save('laplace-lena.png')
img2 = cv2.imread('laplace-lena.png') 

#sumamos la imagen con los bordes obtenidos del laplaciano
resImg = cv2.add(img1,img2)
#resImg = cv2.subtract(img1,img2)
#cv2.imshow('Imagen', resImg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('lena-mejorada.png', resImg)

#se cierran ambos objetos creados de la clase Image
imagen_original.close()
imagen_procesada.close()
