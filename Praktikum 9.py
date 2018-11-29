##Kegiatan 1
berkas = open("L200180164","w")
berkas.write("L200180164 \n")
berkas.write("26-01-2000 \n")
berkas.write("Hafid Yudo H \n")
berkas.close()

##Kegiatan 2
berkas = open("L200180164","w")
berkas.write("L200180164 \n")
berkas.write("26/01/2000 \n")
berkas.write("Hafid Yudo H \n")
berkas.write("Soloo \n")
berkas.close()

import shelve
a = open("L200180164","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Hafid")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Hafid")

print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])

##Kegiatan 3
import shelve
a = open("L200180164","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Hafid")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

##Kegiatan 4
import shelve
a = shelve.open("Hafid")
print ("Nama :" , a['b'][0])
print ("Kota :" , a['b'][1])
print ("TL   :" , a['b'][2])
print ("NIM  :" , a['b'][3])
