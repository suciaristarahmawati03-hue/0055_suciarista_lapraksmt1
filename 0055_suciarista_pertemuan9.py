##---LIST---
# kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup","adit","siti"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran 
data_campuran = [1,"bakwan",2,"cireng","ucup",True, "adit", False]
print(data_campuran)

## Cara alternatif membuat list
data_range = range (0,10,2) # range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range (0,10)]
print(list_for)

# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if=  [i for i in range(0,10) if i %2 != 0]
print(list_for_if)

## --- operasi list ---
# index 0(-3) 1(-2) 2(-1)
data = ["ucup","adit","dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data [-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list 
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list
# menambahkan item pada list sesuai posisi 
print(f"data sebelum ditambah = \n{data}")
# data.insert(posisi,item)
data.insert(1,"asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("ririn")
print(f"data ditambah lagi = \n{data}")

# menambah list dengan list 
data_baru = ["luffy","zoro","nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi jarwo
data[2] = "jarwo"
print(f"data rubah = \n{data}")

# menghapus data
data.remove("ucup")
print(f"data hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")

##---operasi list---
# index 0(-3) 1(-2) 2(-1)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = (jumlah_angka_4)")
print(f"jumlah angka 3 = (jumlah_angka_3)")

# ambil posisi data
data = ["rendi","iqbal","gana","khairil"]
print(f"data = {data}")
index_iqbal = data.index("iqbal")
index_gana = data.index("gana")
print(f"index si iqbal = {index_iqbal}")
print(f"index si gana = {index_gana}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")
print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

## ---nested list ---
data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
list_2d = [data_0, data_1, 6,7]
print(f"list 2d = {list_2d}")

# contoh penggunaan
peserta_0 = ["rendi",25,"laki-laki"]
peserta_1 = ["joni",10,"laki-laki"]
peserta_2 = ["eka",50,"wanita"]
list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")
for peserta in list_peserta:
    print(f"nama\t :{peserta[0]}")
    print(f"umur\t :{peserta[1]}")
    print(f"gender\t :{peserta[2]}\n")

# LATIHAN 1
print("---TUGAS LATIHAN 1---")
print("1. MEMBUAT LIST AWAL")
kendaraan = ["motor","mobil","sepeda","bus"]
print(f"list awal kendaraan : {kendaraan}")

print("a. tambahkan truk diakhir list")
kendaraan.append("truck")
print(f"kendaraan ditambah lagi = {kendaraan}")

print("b. sisipkan becak di index 1")
kendaraan.insert(1,"becak")
print(f"kendaraan_disisipkan becak = {kendaraan}")

print("c. hapus data yang berada paling belakang")
kendaraan.pop()
print(f"kendaraan_akhir = {kendaraan}")

print("d. ubah elemen sepeda menjadi skuter")
kendaraan[2] = "skuter"
print(f"kendaraan dirubah = {kendaraan}")

print("e. tampilkan informasi jumlah total data")
total_data = len(kendaraan)
print(f"jumlah total data sekarang:", total_data)

print("2. LIST AWAL SESUAI SOAL")
angka = [75,80,90,75,85,100,65]
print("list awal:",angka)

print("a. cari tahu index ke berapa skor 100 berada")
index_100 = angka.index(100)
print(f"skor 100 berada di index ke:,{index_100}")

print("b. hitung ada berapa banyak siswa yang mendapat skor 50")
jumlah_75 = angka.count(75)
print(f"jumlah siswa yang mendapat skor 75 = {jumlah_75}")

print("c. urutkan list tersebut dari nilai terkecil ke terbesar")
angka.sort()
print(f"list setelah diurutkan(terkecil ke terbesar) = {angka}")

print("d. balikan urutan list tersebut menjadi dari terbesar ke terkecil")
angka.reverse()
print(f"list setelah dibalik(terbesar ke terkecil) = {angka}")

print("3.)")
print("membuat dua list awal sesuai soal")
menu_utama = ["nasi goreng","mie ayam"]
menu_tambahan = ["kerupuk","es teh"]
# menggabungkan menu_tambahan ke dalam menu_utama menggunakan extend()
menu_utama.extend(menu_tambahan)
print(f"hasil data gabungan menu = \n{menu_utama}\n")

print("4. LIST AWAL SESUAI SOAL")
data_barang = [
    ["buku",5000],
    ["pensil",2000],
    ["penggaris",3000]
]
# a. menampilkan harga dari "pensil" menggunakan index spesifik [baris][kolom]
harga_pensil = data_barang[1][1]
print(f"a. harga dari pensil = {harga_pensil}")
# b. menggunakan perulangan untuk membaca data satu per satu dengan format tertentu 
print("b. daftar nama dan harga barang:")
for barang in data_barang:
    print(f"nama:{barang[0]},harga:{barang[1]}")
