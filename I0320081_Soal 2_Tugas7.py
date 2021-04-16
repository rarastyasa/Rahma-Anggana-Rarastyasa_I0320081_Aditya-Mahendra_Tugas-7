teks = "Perhitungan pada Persegi Panjang"
a = teks.center(50, "*")
print(a)

import math
panjang = float(input("Masukkan panjangnya: "))
lebar = float(input("Masukkan lebarnya: "))

#Menghitung luas persegi panjang dan pembulatan ke atas
luas = panjang*lebar
print("Luas persegi panjang adalah", luas,  "cm persegi")
print("Hasil pembulatan ke atas luas persegi panjang adalah", math.ceil(luas), "cm persegi")
print()

#Menghitung keliling persegi panjang dan pembulatan ke bawah
keliling = panjang+lebar
print("Keliling persegi panjang adalah", keliling, "cm")
print("Hasil pembulatan kebawah persegi panjang adalah", math.floor(keliling), "cm")
print()

#Mengitung diagonal sisi persegi panjang
diagonal_sisi = panjang*panjang+lebar*lebar
print("Panjang diagonal sisi persegi panjang adalah", math.sqrt(diagonal_sisi))
