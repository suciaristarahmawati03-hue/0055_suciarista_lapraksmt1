# perulangan : while, for, do while, forech
# perulangan hanya fokus pada while dan for
# variabel = tempat menyimpan hanya 1 nilai
# array = dapat menyimpan banyak nilai dan berbagai type data ,banyak kebebasan 
# array mempunyai value dan index (penulisan diawali dengan {})
# array memiliki berbagai jenis salah satunya list
# value :
# index :dimulai dari 0

# program 5.1 for
# # perulangan (loop)
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
# for kondisi :
#     aksi
# dengan list
angka2 = [0,1,2,3,4] # ini adalah list
print(angka2)
for i in angka2 :
    print(f"i sekarang -> {i}") # print(f) -> kombinasi text dan variabel
print("akhiri dari program\n")
#dengan range
angka3 = range (5)
for i in angka3:
    print(f"i sekarang ->{i}")
print("akhiri dari program\n")
angka4 = range (1,10)
for i in angka4 :
    print(f"i sekarang->{i}")
    #print("saya keren")
print("akhiri dari program\n")
# menggunakan string
data_str = "saya ganteng abiizz"
for huruf in data_str :
    print(huruf)
print("akhiri dari program\n")

# program 5.2 while loop
# while loop
# while kondisi : 
#      aksi ini
#      aksi itu
print("===contoh 1===\n")
angka = 4
while angka > 5 : 
    print("ipin lari ipin!!!")
print("===contoh 2===\n")
angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5 :
    angka += 1
    # angka = angka + 1
    print(f"angka sekarang -> {angka}")
    print("ipin lari ipin")
print("program berakhir, ipin sudah jauh")

# program 5.3 continue and pass
# pass -> dia berfungsi sebagai dumny, tidak akan diekskusi
angka = 0
while angka < 5 : 
    angka = angka + 1
    if(angka == 3): 
        pass # ini tidak akan dieksekusi
    print(angka)
# continue
angka = 0 
print(f"angka sekarang ->{angka}")
while angka < 5 : 
    angka = angka + 1
    print(f"angka sekarang ->{angka}") # aksi 1
    if(angka == 3): 
        print("nice")
        continue # akan membuat loop melomcat ke step selanjutnya
    print("whasssup") # aksi 2
print("pinish")

# program 5.4 break 
# break
angka = 0 
print(f"angka sekarang -> {angka}")
while angka < 5: 
    angka = angka + 1
    print(f"angka sekarang -> {angka}") # aksi 1
    if(angka == 3):
        print("nice")
        break
    print("whassup") # aksi 2
print("cukup mas")

# program 5.5 latihan perulangan 
# latihan membuat segitiga
# 1. menggunakan for
sisi = 4
count = 1 
for i in range (sisi):
    print("*" * count)
    count += 1
# 2. menggunakan while
sisi = 4
count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break

# tugas latihan 
# bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan
print("tugas latihan")
print("nomer 1")
print("===bilangan ganjil dan genap (1 - 50)===")
print("\n---bilangan ganjil---")
angka = 0
while angka < 50:
    angka += 1
    if angka % 2 != 0 : # angka ganjil
        print(f"{angka} bilangan ganjil")
    else: # jika tidak terpenuhi maka angka genap
        print(f"{angka} bilangan genap")
print("end")

# semua bilangan prima antara 1 sampai 100 menggunakan perulangan 
print("nomer 2")
print("===bilangan prima (1-100)===")
angka2 = 1
while angka2 < 100:
    angka2 += 1
    for i in range(2, angka2):
        if angka2 % i == 0:
            break
    else:
        print(f"{angka2} bilangan prima")

