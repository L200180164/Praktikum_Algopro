y = "Hafid" #Saya membuat sebuah variabel untuk dijadikan sebuah password
a = input("Masukkan Password: ") #Meminta user untuk menginputkan passwordnya
for x in range(2):
    if a==y: #Jika inputan user sama dengan variabel y
         print("Anda berhasil login.") #Menampilkan perintah "Anda berhasil login" jika a sama dengan y
         break 
    elif a!=y: #Ketika a tidak sama dengan y
         print("Maaf, anda salah meemasukkan password") #Menampilkan perintah "Maaf, anda selah memasukkan password" jika a dengan y tidak sama
         a=input("Masukkan password: ") #User diminta untuk menginputkan password kembali
else:
     print("Anda telah mencoba 3 kali. Akses anda ditolak.") #Jika sudah 3 kali maka user tidak bisa menginputkan password kembali.
