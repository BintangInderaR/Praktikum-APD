def data_mhs(nama,nim,fakultas,prodi,ipk,dic):
    dic[nama]= [nim,fakultas,prodi,ipk]
    return dic
    # kode diatas mendefinisikan/membuat fungsi "data_mhs" yang berisi rumus agar nanti dapat menambahkan 
    # mahasiswa kedalam list dictionary
    
list_mhs=dict()
# kode diatas digunakan untuk membuat variabel yang berisi dictionary untuk menampung list mahasiswanya

jumlah_mhs=0
# variabel untuk list menu 2

print("Program Data Mahasiswa \n=================")

while True: 
    print("\nMenu\n1.Input Mahasiswa Baru \n2.Lihat List Mahasiswa \n3.Keluar")

    pilih=int(input("Pilih Nomor : "))
    # digunakan sebagai navigasi menu dengan memasukkan salah satu nomor yang ada di list menu

    if pilih==1:
        jumlah_mhs +=1
        nama=str(input("Masukkan Nama Lengkap Mahasiswa : "))
        nim=int(input("Masukkan Nim Mahasiswa (contoh:2109106000): "))
        fakultas=str(input("Masukkan Fakultas: "))
        prodi=str(input("Masukkan Prodi: "))
        ipk=float(input("Masukkan IPK Mahasiswa (contoh: 1.0): "))
        print("========================\n Mahasiswa Sudah Ditambahkan \n\n", data_mhs(nama,nim,fakultas,prodi,ipk,list_mhs))

    # KETERANGAN KODE DIATAS
    # Jika pilihan menu 1,variabel jumlah_mhs akan ditambah 1 dan kemudian
    # kita akan diminta untuk memasukkan nama, nim, fakultas, prodi, dan ipk. setelah dimasukkan
    # maka inputan akan di print menggunakan fungsi data_mhs yang dibuat sebelumnya dan 
    # mengeluarkan outputan list dictionary

    elif pilih==2:
        if jumlah_mhs==0:
            print("\n=====================\n mahasiswa belum ada")
        else:
            print("========================\n List Mahasiswa \n\n", data_mhs(nama,nim,fakultas,prodi,ipk,list_mhs))

    # KETERANGAN KODE DIATAS
    # Jika pilihan adalah menu 2, yang pertama adalah mengecek jumlah variabel "jumlah_mhs", jika sama dengan 0
    # maka akan mengeluarkan output "mahasiswa belum ada", selain itu jika "jumlah_mhs">0 maka dia akan mengeluarkan
    # output list dictionary
    
    elif pilih==3: 
        break
    # KETERANGAN KODE DIATAS
    # Jika pilihan 3 maka program akan berhenti dan keluar dari looping 
    # dan mengeluarkan output "Terima kasih Telah Menggunakan Program ini"

print ("\n=======================\n Terima kasih Telah Menggunakan Program ini")
input("klik tombol enter untuk keluar...")
