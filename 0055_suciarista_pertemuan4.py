#operasi logika atau booblean
# not, or, and, xor
print('===NOT===')
a = True
b = not a
print('data a =',a)
print('-------------NOT')
print('data b =',b)

# OR (jika salah satu true, maka hasilnya adalah true)
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR' ,b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika dua buah nilai true, maka hasil true)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b 
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true, sisanya false)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b 
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b 
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b 
print(a,'XOR',b,'=',c)

# logika dan komprasi
# membuat gabungan area rentang dari angka
# ++++++++3---------10++++++++
inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3 \natau\nlebih besar dari 10\n:"))
# ++++++++3---------
# memeriksa angka kurang adri 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)
# ---------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)
print("==============================")

# ---------3+++++++10------
# kasus irisan
inputUser = float(input("masukkanangka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -----3+++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# +++++10-----
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)

# if dan else statements
# 1. if 
# 2. kondisi
# 3. aksi
nama = input ("siapa nama anda?")
# 1. program if inline
if nama == "ucup" : print("kamu ganteng abiezzzz!!!")
print("akhir dari program")
# 2. program if indentation
if nama == "ucup" :
    print("kamu ganteng abiezzzz!!")
    print("kamu juga keren banget")
print("akhir dari program")

# 3. else statement
if nama == "paijo" :
    print("hai paijo, si keren!")
else:
    print("ah kamu bukan paijo,kamu gak keren")
print("akhir dari program")

# ELIF = else if statement
nama = input("siapa nama anda?")
# if kondisi :
#  aksi true
# elif kondisi :
#  aksi true
# elif kondisi :
#  aksi true
# else :
#  aksi
if nama == "ucup" : # kondisi 1
    print("hai ganteng abiizz!!") # aksi true 1
elif nama == "paijo" : # kondisi 2
    print("hai si kece bangetts!!!") # aksi true 2
elif nama == "mario": # kondisi 3
    print("hai humoriss!!") # aksi true 3
else:
    print("au ah gak kenal!!") # aksi false
print("akhir dari program")

# Latihan Tugas
usia = float(input("usia: "))
if usia == usia >= 0 and usia <= 12 :
    print("anak-anak")
elif usia == usia >= 13 and usia <= 17 :
    print("remaja")
elif usia == usia >= 18 and usia <= 59 :
    print("dewasa")
else :
    print("lansia")
