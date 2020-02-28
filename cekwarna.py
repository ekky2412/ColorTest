import cv2
import numpy as np 

def biru():
    for i in range(0,3):
        img=cv2.imread('tes'+str(i)+'.png',1)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_api0 = np.array([90, 150, 100])
        upper_api0 = np.array([150, 255, 255])
        mask0 = cv2.inRange(img_hsv, lower_api0, upper_api0)
        mask = mask0
        new_img = cv2.bitwise_and(img, img, mask=mask)
        
        cv2.imshow("Image"+str(i)+".png", new_img)
        cv2.imshow('gambar asli', img)
        cv2.imshow('gambar asli', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def hijau():
    for i in range(0,3):
        img=cv2.imread('tes'+str(i)+'.png',1)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_api0 = np.array([50,100,100])
        upper_api0 = np.array([70,255,255])
        mask0 = cv2.inRange(img_hsv, lower_api0, upper_api0)
        mask = mask0
        new_img = cv2.bitwise_and(img, img, mask=mask)
        
        cv2.imshow("Image"+str(i)+".png", new_img)
        cv2.imshow('gambar asli', img)
        cv2.imshow('gambar asli', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def kuning():
    for i in range(0,3):
        img=cv2.imread('tes'+str(i)+'.png',1)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_api0 = np.array([20,100,100])
        upper_api0 = np.array([40,255,255])
        mask0 = cv2.inRange(img_hsv, lower_api0, upper_api0)
        mask = mask0
        new_img = cv2.bitwise_and(img, img, mask=mask)
        
        cv2.imshow("Image"+str(i)+".png", new_img)
        cv2.imshow('gambar asli', img)
        cv2.imshow('gambar asli', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def biru_hijau():
    for i in range(0,3):
        img=cv2.imread('tes'+str(i)+'.png',1)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_api0 = np.array([90, 150, 100])
        upper_api0 = np.array([150, 255, 255])
        mask0 = cv2.inRange(img_hsv, lower_api0, upper_api0)
        lower_api1 = np.array([50,100,100])
        upper_api1 = np.array([70,255,255])
        mask1 = cv2.inRange(img_hsv, lower_api1, upper_api1)
        mask = mask0+mask1
        new_img = cv2.bitwise_and(img, img, mask=mask)
        
        cv2.imshow("Image"+str(i)+".png", new_img)
        cv2.imshow('gambar asli', img)
        cv2.imshow('gambar asli', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def hijau_kuning():
    for i in range(0,3):
        img=cv2.imread('tes'+str(i)+'.png',1)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_api0 = np.array([50,100,100])
        upper_api0 = np.array([70,255,255])
        mask0 = cv2.inRange(img_hsv, lower_api0, upper_api0)
        lower_api1 = np.array([20,100,100])
        upper_api1 = np.array([40,255,255])
        mask1 = cv2.inRange(img_hsv, lower_api1, upper_api1)
        mask = mask0+mask1
        new_img = cv2.bitwise_and(img, img, mask=mask)
        
        cv2.imshow("Image"+str(i)+".png", new_img)
        cv2.imshow('gambar asli', img)
        cv2.imshow('gambar asli', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
while(True):
    print("Menu Cek Warna")
    print("1.Warna Biru")
    print("2.Warna Hijau")
    print("3.Warna Kuning")
    print("4.Warna Biru dan Hijau")
    print("5.Warna Hijau dan Kuning")
    print("6.Exit")
    pilih=input("Pilih : ")
    type(pilih)
    if(pilih=='1'):
        biru()
    elif(pilih=='2'):
        hijau()
    elif(pilih=='3'):
        kuning()
    elif(pilih=='4'):
        biru_hijau()
    elif(pilih=='5'):
        hijau_kuning()
    elif(pilih=='6'):
            break;
    kembali=input("Kembali ke menu? (y/n) : ")
    if(kembali!='y' or kembali!='Y'):
        break;