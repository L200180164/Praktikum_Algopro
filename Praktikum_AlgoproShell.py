Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: D:\GitHub\FIX.py =========================
>>> Nama #Menampilkan hasil Hafid Yudo Hermansyah, karena Hafid Yudo Hermansyah telah tersimpan pada variabel Nama.
'Hafid Yudo Hermansyah'
>>> Alamat #Menampilkan hasil Jawa Tengah, karena Jawa Tengah telah tersimpan pada variabel Alamat.
'Jawa Tengah'
>>> Umur #Menampilkan hasil 18, karena 18 telah tersimpan pada variabel Umur.
'18'
>>> Hobby #Menampilkan hasil Badminton, karena Badminton telah tersimpan pada variabel Hobby.
'Badminton'
>>> Jenis_Kelamin #Menampilkan hasil Laki-Laki, karena Laki-Laki telah tersimpan pada variabel Jenis_Kelamin.
'Laki-Laki'
>>> Makanan_Kesukaan #Menampilkan hasil Gado-Gado, karena Gado-Gado telah tersimpan pada variabel Makanan_Kesukaan.
'Gado-Gado'
>>> Minuman_Kesukaan #Menampilkan hasil Es Jeruk, karena Es Jeruk telah tersimpan pada variabel Minuman_Kesukaan.
'Es Jeruk'
>>> Status #Menampilkan hasil Jomblo, karena Jomblo telah tersimpan pada variabel Status.
'Jomblo'
>>> Prodi #Menampilkan hasil Informatika, karena Informatika telah tersimpan pada variabel Prodi.
'Informatika'
>>> Fakultas #Menampilkan hasil Fakultas Komunikasi dan Informatika, karena Fakultas Komunikasi dan Informatika telah tersimpan pada variabel Fakultas.
'Fakultas Komunikasi dan Informatika'
>>> 
>>> Nama #Menampilkan hasil Hafid Yudo Hermansyah, karena Hafid Yudo Hermansyah telah tersimpan pada variabel Nama.
'Hafid Yudo Hermansyah'
>>> Tanggal_Lahir #Menampilkan hasil 26 Januari 2000, karena 26 Januari 2000 telah tersimpan pada variabel Tanggal_Lahir.
'26 Januari 2000'
>>> NIM #Menampilkan hasil L200180164, karena L200180164 telah tersimpan pada variabel NIM.
'L200180164'
>>> X #Menampilkan hasil 1164, variabel X menyimpan data 1 kemudian menambahkan dengan 3 digit terakhir dari NIM.
'1164'
>>> a #Menampilkan hasil 1164, karena variabel a menyimpan konversi string variabel X ke integer.
1164
>>> b #Menampilkan hasil 21, karena variabel b menghitung jumlah indeks dari variabel Nama.
21
>>> type(a) #Menampilkan hasil <class 'int'>, menampilkan type data dari variabel a.
<class 'int'>
>>> type(b) #Menampilkan hasil <class 'int'>, menampilkan type data dari variabel b.
<class 'int'>
>>> a / b #Menampilkan hasil 55.42857142857143, Operasi pembagian antara bilangan dari variabel a dengan variabel b.
55.42857142857143
>>> a // b #Menampilkan hasil 55, Operasi pembagian dengan pembulatan ke bawah antara bilangan variabel a dengan variabel b.
55
>>> 10 * (a - 999) #Menampilkan hasil 1650, Operasi Perkalian semacam ini dapat digunakan untuk mengalikan data dengan type integer dan juga float.
1650
>>> b ** 2 #Menampilkan hasil 441, Operasi Aritmatika ini digunakan untuk perpangkatan, type data yang dapat digunakan dalam operasi aritmatika perpangkatan ini diantara integer dan float.
441
>>> a % b #Menampilkan hasil 9, Operasi Aritmatika ini untuk memunculkan hasil dari Sisa Hasil Bagi antara variabel a dengan variabel b.
9
>>> c #Menampilkan 12.5, karena pada variabel c telah tersimpan 12.5
12.5
>>> type(c) #Menampilkan <class 'float', menampilkan type data dari 12.5
<class 'float'>
>>> a /c #Menampilkan 93.12 , Operasi pembagian aritmatika antara bilangan variabel a dengan variabel c.
93.12
>>> a // c #Menampilkan hasil 93, Operasi pembagian dengan pembulatan ke bawah antara bilangan dari variabel a dengan variabel c.
93.0
>>> a % c #Menampilkan hasil 1.5 , Operasi sisa hasil bagi antara bilangan variabel a dengan variabel c.
1.5
>>> c > b #Menampilkan hasil False, Operasi boolean ini digunakan untuk menampilkan perbandingan lebih dari. Type data dari ini adalah Boolean.
False
>>> type(c>b) #Menampilkan hasil <class 'bool'>, type dari data ini adalah boolean.
<class 'bool'>
>>> a > b and b > c #Digunakan untuk perbandingan antara dua variabel.
True
>>> a > 1100 or b < 10 #Digunkan untuk perbandingan antara dua variabel.
True
>>> 
>>> Nama
'Hafid Yudo Hermansyah'
>>> NIM
164
>>> Tinggi
1.7
>>> Berat
60
>>> TahunLahir
2000
>>> Aku #Menampilkan isi dari variabel TahunLahir, Berat, Tinggi, NIM, Nama.
(2000, 60, 1.7, 164, 'Hafid Yudo Hermansyah')
>>> Data #Menampilkan isi dari variabel TahunLahir, Berat, Tinggi, NIM, Nama.
[2000, 60, 1.7, 164, 'Hafid Yudo Hermansyah']
>>> type(Aku) #Menampilkan type data dari variable Aku.
<class 'tuple'>
>>> Aku[0] #Menampilkan element tuple indeks 0.
2000
>>> a = NIM % 4; Aku[a] #NIM 164 dibagi 4 kemudian sisa hasil baginya adalah 0 kemudian dimasukan ke variabel Aku tuple a.
2000
>>> type(Aku[a]) #Menampilkan type data dari element tuple indeks a.
<class 'int'>
>>> Aku[a:4] #Slicing dimulai indeks ke 0 hingga indeks ke 4.
(2000, 60, 1.7, 164)
>>> type(Aku[4]) #Menampilkan type data dari variabel Aku indeks ke 4.
<class 'str'>
>>> Aku[0] = 'ok' #Hasilnya ERROR karena element sebuah tuple tidak dapat diubah.
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Aku[0] = 'ok' #Hasilnya ERROR karena element sebuah tuple tidak dapat diubah.
TypeError: 'tuple' object does not support item assignment
>>> type(Data) #Menampilkan type data dari variabel Data.
<class 'list'>
>>> type(Data[4]) #Menampilkan type data dari element list ke 4
<class 'str'>
>>> Data[4][5] #Menampilkan list indeks 5 pada list 4.
' '
>>> Data[4][a:6] #Menampilkan list 0 sampai 5 dari list 4.
'Hafid '
>>>(Data[4][a:6]) #Menampilkan list indeks 0 sampai 6 dari list 4.
Hafid 
>>> Data[0] = 'ok'; Data #Mengubah Element list pada indeks 0 menjadi ok
['ok', 60, 1.7, 164, 'Hafid Yudo Hermansyah']
>>> Data[-a] #Menampilkan huruf atau angka terakhir pada indeks akhir ke 3 dari list.
'ok'
>>> range(a) #Menampilkan daftar atau koleksi dari indeks.
range(0, 0)
>>> 
