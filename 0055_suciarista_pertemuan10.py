# list = variabel untuk menyimpan banyak data
# tuple tidak bisa dirubah datanya (menggunakan tanda kurung() biasa)
# set menggunakan ({}) ketika memasukkan data yg sama saat di print tidak akan muncul doble
# distionary = struktur data key dan value 
# key=pengganti index

# LIST program 10.1 tuples dan sets
# menggunakan kurang siku
data_list = [10,2,4,3,2]
print(data_list)

# tuples
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan 
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets(himpunan)
data_sets = {10,4,3,2,7,6,5}
print(data_sets)
print(list(data_sets)[0])

## distionary program 10.2 dictionary
# list -> array, mengakses dengan menggunakan index
data_list = ["ucup","rendi","salsa"]
print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key
data_dict = {
    "key":"value",
    "cp":"ucup",
    "rd":"rendi",
    "sl":"salsa",
    "nmbr":100,
    "list":data_list
}
print(data_dict["cp"])
print(data_dict["nmbr"])
print(data_dict["list"])

##---operasi dictionary---(program 10.3 operasi dictionary)
data_dict = {
    "cup":"ucup surucup",
    "pet":"opet saripet",
    "ndo":"nando surundo",
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary:{LENDICT}")

# mengecek key exist atau tidak
KEY = "ucup"
CHECKKEY = KEY in data_dict
print(f"apakah{KEY} ada di data_dict:{CHECKKEY}")

# mengakses value(read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # check key dengan message

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)

data_dict.update({"ucup":"ucup surucup"})
print(data_dict)
data_dict.update({"iwn":"iwan mang keren"}) # akan ditambah jika ada
print(data_dict)

# menghapus data
del data_dict["iwn"]
print(data_dict)

##---looping dictionary---(program 10.4)
teman_teman = {
    "ucup":"ucup surucup",
    "tong":"sotong surotong",
    "lur":"lur sedulur",
    "wel":"bung towel"
}

# looping first try (yang keluar hanya key)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item
keys = teman_teman.keys()
print(keys)
for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

item = teman_teman.items()
print(item)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key},value = {value}")


print("---TUGAS LATIHAN---")
print("1. Tuple")
# a. data diti
mahasiswa = ("suci arista","2605060055","teknologi informasi")
# b. menampilkan NIM dan Prodi dengan mengakses index
print("NIM:",mahasiswa[1])
print("Prodi:",mahasiswa[2])
# c. mencoba mengubah elemen tuple (baris di bawah ini akan menyebabkan error jika tidak dikomentari)
# mahasiswa[2] = "teknologi informasi"
# d. membuat set dan mencetaknya
nilai_angka = {10,4,3,2,4,10,7,5}
print("isi set nilai_angks:", nilai_angka)
print("2. manipulasi dictionary")
# a. membuatdictionary data_mahasiswa
data_mahasiswa = {
    "nim" : "240101",
    "nama" : "suci arista",
    "prodi" : "teknologi informasi"
}
# b.  mengubah nilai "prodi" sekaligus menambahkan key baru "angkatan"
data_mahasiswa.update({
    "prodi":"teknik sipil",
    "angkatan":"2026"
})
# c. menghapus data "nim" dan menampilkan hasil akhir
del data_mahasiswa["nim"]
print("hasil akhir dictionary:", data_mahasiswa)
print("perulangan pada dictionary")
# a. membuat  dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
total_belanja = 0
# b. perulangan untuk menampilkan barang dan harga
for buah, harga in keranjang.items():
    print(f"harga {buah}: Rp {harga}")
    total_belanja += harga
# c. menampilkan total belanja
print(f"total belanja: Rp {total_belanja}")