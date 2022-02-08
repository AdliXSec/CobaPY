import time

def ulang(text, ulang):
    a = 0
    while(a < ulang):
        time.sleep(0.1)
        print(text)
        a = a+1

nama = input(" masukkan nama anda : ")
jumlah = int(input(" masukkan pengulangan : "))
ulang(nama, jumlah)
