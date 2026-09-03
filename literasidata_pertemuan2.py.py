nama = "suci arista" #menyimpan nama string
umur = 18 # menyimpan umur integer
berat = 55.1 # menyimpan berat float
# menampilkan data
print("nama : ", nama)
print("umur : ", umur)
print("berat : ", berat)
#mengubah tipe data
# mengubah dari string menjadi integer
angka_string = "123"
data_string = int(angka_string)
# mengubah float menjadi integer
angka_float = 45.67
data_float = int(angka_float)
# mengubah integer menjadi float
angka_int = 89
data_integer = float(angka_int)
#mengubah integer menjadi string
angka_integer = 89
angka_integer1 = str(angka_integer)
#menampilkan data
print("data = ", data_string, " bertipe = ", type(data_string)) 
print("data = ", data_float, " bertipe = ", type(data_float))
print("data = ", data_integer, " bertipe = ", type(data_integer))
print("angka = ", angka_integer1, " bertipe = ", type(angka_integer1))
#membuet program input
nama = str(input("Siapa nama anda: "))
usia = int(input("Berapa umur anda: "))
tinggi = float(input("Berapa tinggi badan anda: "))
print("nama aku adalah: ", nama)
print("Umur aku adalah: ", usia)
print("Tinggi aku adalah: ", tinggi, "cm")