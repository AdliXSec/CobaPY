import pyautogui as spam
import time
import os
import sys
# import webbrowser as wb

def loading():
    trg = 0
    while(trg < 12.5):
        print("Silahkan Masuk Ke whatsapp web | ")
        time.sleep(0.1)
        os.system("cls")
        print("Silahkan Masuk Ke whatsapp web / ")
        time.sleep(0.1)
        os.system("cls")
        print("Silahkan Masuk Ke whatsapp web - ")
        time.sleep(0.1)
        os.system("cls")
        print("Silahkan Masuk Ke whatsapp web \ ")
        time.sleep(0.1)
        os.system("cls")
        trg = trg + 1

def proges():
    print("Spam Akan Di Mulai")
    print("[                    ] 0% ")
    time.sleep(1)
    os.system("cls")
    print("Spam Akan Di Mulai")
    print("[=====               ] 25%")
    time.sleep(1)
    os.system("cls")
    print("Spam Akan Di Mulai")
    print("[==========          ] 50%")
    time.sleep(2)
    os.system("cls")
    print("Spam Akan Di Mulai")
    print("[===============     ] 75%")
    time.sleep(2)
    os.system("cls")
    print("Spam Akan Di Mulai")
    print("[====================] 100%")
    time.sleep(2)
    os.system("cls")

# wb.open("web.whatsapp.com")
os.system("color a")
os.system("cls")
time.sleep(1)
print("Note: Harap anda sudah membuka whatsapp web terlebih dahulu")
nama = input("Masukkan Nama Whatsapp Target : ")
pesan = input("Masukkan pesan : ")
jumlah = int(input("Masukkan jumlah spam : "))
time.sleep(2)
os.system("cls")

loading()

time.sleep(2)
spam.press("tab")
time.sleep(2)
spam.write(nama)
time.sleep(5)
spam.press("enter")
time.sleep(2)
os.system("cls")

proges()

print("Spam Dimulai")
count = 0
while(count < jumlah):
    spam.write(pesan)
    time.sleep(0.1)
    spam.press("enter")
    time.sleep(0.1)
    count = count + 1
    
os.system("cls")
print("Spam Selesai")