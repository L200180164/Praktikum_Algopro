# Program Identitas Diri.
## Dibuat oleh Hafid Yudo H L200180164
Nama = 'Hafid Yudo Hermansyah'
Alamat = 'Jawa Tengah'
Umur = '18'
Hobby = 'Badminton'
Jenis_Kelamin = 'Laki-Laki'
Makanan_Kesukaan = 'Gado-Gado'
Minuman_Kesukaan = 'Es Jeruk'
Status = 'Jomblo'
Prodi = 'Informatika'
Fakultas = 'Fakultas Komunikasi dan Informatika'


##Program Akun
## Dibuat oleh Hafid Yudo H L200180164
Nama = 'Hafid Yudo Hermansyah'
Tanggal_Lahir = '26 Januari 2000'
Nama_Singkat = Nama [:5]
Username = Nama [0:1] + Tanggal_Lahir [0:2] + Tanggal_Lahir [11:15]
Password = Nama [0:3] + Tanggal_Lahir [11:14]

###Program Operator.
## Dibuat oleh Hafid Yudo H L200180164
Nama = 'Hafid Yudo Hermansyah'
NIM = 'L200180164'
X = '1' + NIM[7:]
a = int(X)
b = len(Nama)
type(a)
type(b)
a / b
a // b
10 * (a - 999)
b ** 2
a % b
c = 12.5
type(c)
a / c
a // c
a % c
c > b
type(c > b)
a > b and b > c
a > 1100 or b < 10

####Program Tipe Data
## Dibuat oleh Hafid Yudo H L200180164
Nama = 'Hafid Yudo Hermansyah'
NIM = 164
Tinggi = 1.70
Berat = 60
TahunLahir = 2000
Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
type(Aku)
Aku[0]
a = NIM % 4; Aku[a]
type(Aku[a])
Aku[a:4]
type(Aku[4])
Aku[0] = 'ok'
type(Data)
type(Data[4])
Data[4][5]
Data[4][a:6]
print (Data[4][a:6])
Data[0] = 'ok'; Data
Data[-a]
range(a)
