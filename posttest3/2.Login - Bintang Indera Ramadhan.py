#program Kafe
#Nama   : Bintang Indera Ramadhan
#NIM    : 2109106014
#Kelas  : Informatika A

users = {}
nav = " "
admin = users["admin"] = "1234"

def userBaru():
    userBaru = input("Masukkan Username Baru : ")
    if userBaru in users:
        print("Username sudah ada")
    else:
        passBaru = input("Masukkan Password Baru : ")
        users[userBaru] = passBaru
        print("\n\nAkun berhasil dibuat !")
        input("Tekan enter untuk kembali")

#=======================================================

def userAda():
    salah = 0

    while salah < 3 :
        login = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        if login in users and users[login] == password:
                print("login Berhasil")
                print("selamat datang")
                input("Tekan enter untuk Log out")
                break
        else :
            print("username/password salah\n")
            salah +=1
    if salah == 3 :
        print("login gagal")

#=======================================================

def adminMode():
    salah = 0

    while salah < 3 :
        login = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        if login in users and users[login] == password:
                print("login Berhasil\n")
                adminNav()
        else :
            print("username/password salah\n")
            salah +=1
    if salah == 3 :
        print("login gagal")

#=======================================================

def adminNav():
    adminNavi = 0
    numUser = len(users)
    while True:
        print("Welcome Admin\n==================")
        print("""
        1. Lihat List Users
        2. Logout""")
        adminNavi = int(input("Input Navigation Number 1 - 2: "))

        if adminNavi == 1:
            print("List User: \n")
            for iuser in users:
                print("- ",iuser)
            input("Tekan Enter Untuk Kembali..")
            adminNavi = 0
        elif adminNavi == 2:
            mainMenu()

#=======================================================

def mainMenu():
    while True:
        print ("\nProgram Login \n_________________________\n")
        print ("""
        1. Login
        2. Login Admin
        3. Register
        4. Exit
        """)
        nav= int(input("\n Input Navigation Number 1 - 4: "))
        if nav == 1:
            userAda()
        elif nav== 2: 
            adminMode()
        elif nav== 3: 
            userBaru()
        elif nav == 4:
            print("Exiting...")
            exit()
        else:
            print("Invalid Input")

#=======================================================
mainMenu()