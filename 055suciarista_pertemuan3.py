# operasi aritmatika 3.1
a = 10
b = 3

#modulus: sisa pembagian
# modulus jika dibagi menghasilkan 0 maka dikatakan genap jika terdapat sisa berarti dikatakan ganjil

# operasi tambah +
hasil = a + b 
print(a,'+',b,'=',hasil)

# operasi kurang -
hasil = a + b 
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat)**
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# latihan konversi satuan temperature 3.2
# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah", celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "kelvin")

# operasi komperasi 3.3
# setiap hasil dari operasi komperasi adalah boolean
# >,<,>=,<=,==,!=,is,is not
a = 4
b = 2

# lebih besar dari >
print("============ lebih besar dari (>)")
hasil = a > 3
print(a,'>',b,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print("============ kurang dari (<)")
hasil = a < 3
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("============ lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("============ kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("============ sama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("============ tidak sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi obj identity (bukan literasi)
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print('x is y =',hasil)

# 'is not' sebagai komparasi obj identity (bukan literasi)
x = 5 # ini adalah assignment membuat object 
y = 6
hasil = x is not y 
print('x is not y =',hasil)

# Tugas latihan 
print("\nTUGAS LATIHAN LAPRAK\n")
print("1. hitung luas, volume dan keliling")
panjang = 12
lebar = 5 
tinggi = 8
print("luas: ")
print("l= 2*" "(p*l)+(p*t)+(l*t)")
hasil = 2 * (12 * 5) + (12 * 8) + (5 * 8)
print(2,'*',"(12 * 5)",'+',"(12 * 8)",'+',"(5 * 8)",'=',hasil) 
print("volume:")
print("v=(p*l*t)")
hasil = (12 * 5 * 8)
print("(12 * 5 * 8)",'=',hasil)
print("keliling:")
print("k= 4 * (p * l * t)")
hasil = 4 * (12 * 5 * 8)
print(4,'*',"(12 * 5 * 8)",'=',hasil)

# pembenaran luas bangunan lebih luas dari 50
hasil_luas = (256) > 50
print(256, '>',50,'=',hasil_luas)

# pembenaran volume bangunan bernilai 480
hasil_volume = (480) == 480
print(480, '==',480,'=',hasil_volume)