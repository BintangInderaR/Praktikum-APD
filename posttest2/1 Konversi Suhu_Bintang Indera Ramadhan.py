ulang="y"
# membuat variabel baru dengan string "y" untuk pengulangan while

print("Program Konversi Suhu")
print("======================")

while ulang=="y":
    print("\n Konversi Suhu: ")
    print("a. Fahrenheit ke Celcius \nb. Kelvin ke Celcius \nc. Reamur ke Celcius")
    print("=====================\n")
    pilih=input("pilih a, b, c, ex : ")
    
    # KETERANGAN KODE DIATAS
    # kode masuk ke ke fungsi pengulangan while, dan mengoutputkan beberapa pilihan a,b,c, ex(exit).
    # Kemudian akan meminta inputan salah satu dari pilihan dengan variabel "pilih". 

    if pilih=="a":
        F=int(input("Masukkan suhu Fahrenheit: "))
        cel=(F-32)/1.8
        print("Suhu Fahrenheit > Celcius : ",cel,"°C")
        print("======================================")
        ulang=input("ingin mengulang ? (y,t) : ")
    
    # KETERANGAN KODE DIATAS
    # jika pilihan a, maka kode akan meminta untuk memasukkan suhu fahrenheit, lalu akan melakukan perhitungan
    # pada variabel "cel". Kemudian akan mengoutputkan suhu yang sudah dikonversikan ke Celcius
    # dan kode akan meminta untuk memasukkan inputan menggunakan variabel "ulang". jika ingin mengulang 'y' 
    # maka program akan kembali ke menu pilihan konversi, jika tidak ingin mengulang 'n' maka pengulangan akan berhenti
    # dan mengoutputkan "terima kasih !"

    elif pilih=="b":
        K=int(input("Masukkan suhu Kelvin: "))
        cel=K-273.15
        print("Suhu Kelvin > Celcius : ",cel,"°C")
        print("======================================")
        ulang=input("ingin mengulang ? (y,t) : ")

    # KETERANGAN KODE DIATAS
    # jika pilihan b, maka kode akan meminta untuk memasukkan suhu Kelvin, lalu akan melakukan perhitungan
    # pada variabel "cel". Kemudian akan mengoutputkan suhu yang sudah dikonversikan ke Celcius
    # dan kode akan meminta untuk memasukkan inputan menggunakan variabel "ulang". jika ingin mengulang 'y' 
    # maka program akan kembali ke menu pilihan konversi, jika tidak ingin mengulang 'n' maka pengulangan akan berhenti
    # dan mengoutputkan "terima kasih !"

    elif pilih=="c":
        R=int(input("Masukkan suhu Reamur: "))
        cel=R/0.8
        print("Suhu Reamur > Celcius : ",cel,"°C")
        print("======================================")
        ulang=input("ingin mengulang ? (y,t) : ")

    # KETERANGAN KODE DIATAS
    # jika pilihan c, maka kode akan meminta untuk memasukkan suhu Reamur, lalu akan melakukan perhitungan
    # pada variabel "cel". Kemudian akan mengoutputkan suhu yang sudah dikonversikan ke Celcius
    # dan kode akan meminta untuk memasukkan inputan menggunakan variabel "ulang". jika ingin mengulang 'y' 
    # maka program akan kembali ke menu pilihan konversi, jika tidak ingin mengulang 'n' maka pengulangan akan berhenti
    # dan mengoutputkan "terima kasih !"

    elif pilih=="ex":
        break

    # KETERANGAN KODE DIATAS
    #Jika pilihan ex, maka pengulangan akan berhenti dan langsung mengoutputkan "terima kasih !"

    else :
        print("\npilihan tidak ada\n==============\n")
        ulang="y"
    
    # KETERANGAN KODE DIATAS
    # Jika inputan pilihan tidak ada maka akan langsung mengoutputkan "pilihan tidak ada" dan langsung kembali mengulang
    # menu pilihan.
    
print("==============")
print("Terima kasih !")

input("klik tombol enter untuk keluar...")
