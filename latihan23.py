print("LATIHAN")
 
print("A. PENULISAN FORMAT NAMA YANG BENAR")
nama = input ("Masukkan Nama Client: ")
 
print("B.KETENTUAN PANJANG NOMOR TELEPON.")
ulang="y"
while ulang=="y":
    import re
    nomor=input("Masukkan Nomor Telepon: ")
    hitung=len(str(nomor))
    lis=list(str(nomor))
    cek=nomor.count("+")
    if hitung > 14 or hitung<10:
        ulang = "y"
        print("maksimal karakter 14 dan minimal 10 silahkan input ulang nomor")
    elif lis[0] != "0" and cek == 0:
        ulang = "y"
        print("nomor harus diawali 0 atau gunakan +62")
    else:
        ulang="t"
 
 
print("---------------------")
print ("Nama : "+nama.title())
print ("Nomor :",nomor)
print("---------------------")
