import datetime
mahasiswa1 = {
    "nama":"ucup surucup",
    "nim":"19022001",
    "sks_lulus":130,
    "beasiswa": "false",
    "lahir":datetime.datetime(2001,4,10) # tahun, tanggal,bulan
}
mahasiswa2 = {
    "nama":"azan maghrib",
    "nim":"19022002",
    "sks_lulus":"140",
    "beasiswa":"True",
    "lahir":datetime.datetime(2002,10,10) # tahun,tanggal,bulan
}
mahasiswa3 = {
    "nama":"slamet dunia akhirat",
    "nim":"19022003",
    "sks_lulus":"100",
    "beasiswa":"True",
    "lahir":datetime.datetime(1977,5,20) #tahun, tanggal, bulan
}
data_mahasiswa = {
    "MAH001":mahasiswa1,
    "Mah002":mahasiswa2,
    "MAH003":mahasiswa3,
}
print(f"{"KEY":<6}{"Nama":<6}{"SKS":<3}{"Beasiswa":<9}{"Lahir":<10}")
print("-"*50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{"KEY":<6}{"Nama":<17}{"SKS":<3}{"Beasiswa":<9}{"Lahir":<10}")

import datetime
mahasiswa_template = {
    "nama":"nama",
    "nim":00000000,
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,1,11)
}
data_mahasiswa = { }
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("NAMA MAHASISWA:")
mahasiswa['nim'] = input("NIM MAHASISWA:")
mahasiswa['sks_lulus'] = int(input("SKS LULUS:"))
TAHUN_LAHIR = int(input("Tahun lahir(yyyy):"))
BULAN_LAHIR = int(input("Bulan lahir(1-12):"))
TANGGAL_LAHIR = int(input("Tanggal lahir(1-31):"))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)

import datetime
import os
import string
import random
# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}
data_mahasiswa = { }
while True :
    # os.system("cls") #  untuk windows
    os.system("clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa:")
    mahasiswa['nim'] = input("Nim Mahasiswa:")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus:"))
    TAHUN_LAHIR = int(input("Tahun lahir(yyyy):"))
    BULAN_LAHIR = int(input("Bulan lahir(1-12):"))
    TANGGAL_LAHIR = int(input("Tanggal lahir(1-31):"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    data_mahasiswa = { }
    # dari program sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS LULUS':<10} {"Tanggal Lahir":<10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA =  data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
        print("\n")
    is_done = input("mau tambah lagi bro (y/n)?")
    if is_done == "n":
        break
print("\nAkhir dari program,terima kasih")



print("---TUGAS LATIHAN---")
import datetime
import os
import random
import string

buku_template = {
    "judul":"judul",
    "penulis":"penulis",
    "tahun_terbit": 0,
    "tgl_pinjam": datetime.datetime(1111,1,11),
    "status":"TERSEDIA",
}
data_buku = {}
while True:
    # gunakan "cls" jika menjalankan di windows, atau "clear" di Linux/macOS
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^65}")
    print(f"{'INPUT & DAFTAR BUKU':^65}")
    print("-"*65)

    buku = dict.fromkeys(buku_template.keys())
    buku["judul"] = input("judul buku\t\t: ")
    buku["penulisan"] = input("penulis\t\t\t: ")
    buku["tahun_terbit"] = int(input("tahun terbit(YYYY)\t: "))

    tahun = int(input("tahun terakhir pinjam (YYYY)\t: "))
    bulan = int(input("bulan terakhir pinjam (1-12)\t: "))
    tanggal = int(input("tanggal terakhir pinjam (1-31)\t: "))
    buku["tgl_pinjam"] = datetime.datetime(tahun, bulan, tanggal)
    while True:
        status_input = input("Status (TERSEDIA / TIDAK)\t: ").strip().upper()
        if status_input in ["TERSEDIA", "TIDAK"]:
            buku["status"] = status_input
            break
        print("input tidak valid! masukkan hanya 'TERSEDIA' atau 'TIDAK'.")

    KEY = "".join("random.choice(string.ascii_uppercase) for_in range(6)")
    data_buku.update({KEY: buku})
    print(
        f"\n{'KEY':<8}{'JUDUL BUKU':<22}{'PENULUS':<18}"
        f"{'TAHUN':<7}{'TGL PINJAM':<14}{'STATUS':<10}"
    )
    print("-"*85)
    for key in data_buku:
        judul = data_buku[key]["judul"]
        penulis = data_buku[key]["penulis"]
        tahun_terbit = data_buku[key]["tahun_terbit"]
        tgl_pinjam = data_buku[key]["tgl_pinjam"].strftime("%d-%m-%Y")
        status = data_buku[key]["status"]
        print(
            f"{str(key):<8}{str(judul):<22}{str(penulis):<18}"
            f"{str(tahun_terbit):<7}{str(tgl_pinjam):<14}{str(status):<10}"
        )
    print()
    is_done = input("mau tambah buku lagi (y/n)? ").strip().lower()
    if is_done == "n":
        break
print("\nAkhir dari program, terimakasihhh")