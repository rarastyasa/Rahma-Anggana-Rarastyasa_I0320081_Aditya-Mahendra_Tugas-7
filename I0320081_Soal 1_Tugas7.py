teks = "Perpustakaan Umum Surakarta"
a = teks.center(70,'=')
p = a.upper()
print(p)
p = "Prosedur Peminjaman Buku"
print(p)

buku = "Macam-macam buku: Novel, Atlas, Geografi, Fisika, Kimia, Biologi, IPS Terpadu, Sastra Jepang, Atlas, Novel, Kimia, Sastra Indonesia"
print(buku)
teks = input("Masukkan judul buku yang ingin anda pinjam: ")
judul_buku = teks.capitalize()
judulbuku = buku.count(judul_buku)
print ("Jumlah buku", judul_buku, "di perpustkaan kami saat ini sebanyak", judulbuku, "buah")
if judulbuku>=2:
    print("Buku", judul_buku, "boleh dipinjam")
else:
    print("Buku", judul_buku, "hanya boleh dibaca di perpustakaan")
ucapan = "Terimakasih sudah datang di Perpustakaan Umum Solo, Selamat Membaca!"
x = ucapan.replace("Solo","Surakarta")
print(x)
