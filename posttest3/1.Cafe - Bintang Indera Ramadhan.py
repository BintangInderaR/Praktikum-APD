#program Kafe
#Nama   : Bintang Indera Ramadhan
#NIM    : 2109106014
#Kelas  : Informatika A

from os import system
from datetime import datetime
weekNow = datetime.today().weekday()


#list 
makanan = []
minuman = []
listDiskon = []
listOrder = []

#Menu Harga dan Diskon
kopiHitam = 13000
kopiCappuccino = 15000
esTeh = 5000
kentangGoreng = 17000
mieGoreng = 20000
totalHarga= 0
totalDiskon = 0
totalOrder = 0
diskon1= 0.1
diskon2= 0.05 
diskon3= 0.05
diskon4= 0.05
diskon5= 0.1

tetapPesan = "y"

#==================================================

while tetapPesan=="y":
    system("cls")
    print("Halo Selamat datang di Kafe Rabbit House")
    print("========================================\n\n")
    print("ingin Pesan Apa ?\n")
    print("""
    1. Kopi Hitam       Rp.13000
    2. Kopi Cappuccino  Rp.15.000
    3. Es Teh           Rp.5000
    4. Kentang Gorang   Rp.17.000
    5. Mie Goreng       Rp.20.000 
    6. Itu saja\n""")

    print("""
    Kami Juga Memiliki Diskon Jika :
    a. Membeli 3 minuman atau lebih dengan diskon 10%
    b. Membeli 2 makanan atau lebih dengan diskon 5%
    c. Mendapatkan diskon jika pembayaran melalui E-Money sebesar 5%
    d. Diskon 5% ketika Weekend
    e. Diskon 10% ketika Weekdays\n\n  """)
    print("List Pesanan: ")
    for listOrdersekarang in listOrder:
        print("- ",listOrdersekarang)
    order = int(input("Masukkan No Pesanan 1 - 5 : "))
    

    if order == 1 :
        totalOrder += 1
        minuman.append("Kopi Hitam")
        listOrder.append("Kopi Hitam")
        print("Orderan ditambahkan\n")
        totalHarga += kopiHitam
        tetapPesan=input("ada lagi ? (y/t)")

    elif order == 2 :
        totalOrder += 1
        minuman.append("Kopi Cappucino")
        listOrder.append("Kopi Cappucino")
        print("Orderan ditambahkan\n")
        totalHarga += kopiCappuccino
        tetapPesan=input("ada lagi ? (y/t)")

    elif order == 3 :
        totalOrder += 1
        minuman.append("Es Teh")
        listOrder.append("Es Teh")
        print("Orderan ditambahkan\n")
        totalHarga += esTeh
        tetapPesan=input("ada lagi ? (y/t)")

    elif order == 4 :
        totalOrder += 1
        makanan.append("Kentang Goreng")
        listOrder.append("Kentang Goreng")
        print("Orderan ditambahkan\n")
        totalHarga += kentangGoreng
        tetapPesan=input("ada lagi ? (y/t)")

    elif order == 5 :
        totalOrder += 1
        makanan.append("Mie Goreng")
        listOrder.append("Mie Goreng")
        print("Orderan ditambahkan\n")
        totalHarga += mieGoreng
        tetapPesan=input("ada lagi ? (y/t)")

    elif order== 6 :
        if totalOrder==0:
            print("\nbelum ada order menu")
        else :
            break

    else :
        print ("Tidak ada di menu")

print("\nOke jadi pesanan anda \n=================\n")


#==================================================
print()
for iorder in listOrder:
    print("- ",iorder)

print("\nDengan Total Harga sebelum diskon : Rp.",totalHarga)

print ("\nMau bayar dengan apa ?\nmetode pembayaran : \n1. Tunai \n2. E-Wallet")
metode = int(input("Pilih Metode Pembayaran (1/2): "))

#Counter Discount
if metode==2:
    totalDiskon += (diskon3 * 100)
    listDiskon.append("Diskon E-Money 5%")
    
if len(makanan)>=2:
    totalDiskon += (diskon2 * 100)
    listDiskon.append("Diskon 2 Makanan 5%")

if len(minuman)>=3:
    totalDiskon += (diskon1 * 100)
    listDiskon.append("Diskon 3 Minuman 10%")

if weekNow < 5:
    totalDiskon += (diskon5 * 100)
    listDiskon.append("Diskon Weekdays 10%")
else: 
    totalDiskon += (diskon4 * 100)
    listDiskon.append("Diskon Weekend 5%")

print("\nAnda mendapatkan diskon \n")
for idiskon in listDiskon:
    print("- ",idiskon)


print("\nTotal Diskon anda adalah : ", int(totalDiskon),"%\n")

hargaDiskon = totalHarga - (totalHarga * totalDiskon/100)

print ("Total harga setelah diskon : Rp.", int(hargaDiskon))

print ("terima kasih, Ditunggu ya :)")
input("press ENTER to exit..")








    