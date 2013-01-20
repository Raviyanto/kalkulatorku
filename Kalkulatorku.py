#!/usr/bin/python

import galat
import operasi

print "\n"
print "Program Kalkulatorku"
print "\n"

program_berjalan = True

while program_berjalan:
       
    print "Tulis + untuk penjumlahan"
    print "Tulis - untuk pengurangan"
    print "Tulis * untuk perkalian"
    print "Tulis / untuk pembagian"
    print "Tulis x untuk keluar"  
    
    
   
# Menu pilihan.
    pilihan = raw_input()   
    
    if pilihan == "+":
        angka_pertama = raw_input("Masukkan angka pertama: ")
        angka_kedua = raw_input("Masukkan angka kedua: ")
        print "Hasil penjumlahan kedua angka:"
        print operasi.tambah(angka_pertama, angka_kedua)
        print "\n"
    elif pilihan == "-":
        angka_pertama = raw_input("Masukkan angka pertama: ")
        angka_kedua = raw_input("Masukkan angka kedua: ")
        print "Hasil pengurangan kedua angka:"
        print operasi.kurang(angka_pertama, angka_kedua)
        print "\n"
    elif pilihan == "*":
        angka_pertama = raw_input("Masukkan angka pertama: ")
        angka_kedua = raw_input("Masukkan angka kedua: ")
        print "Hasil perkalian kedua angka:"
        print operasi.kali(angka_pertama, angka_kedua)
        print "\n"
    elif pilihan == "/":
        angka_pertama = raw_input("Masukkan angka pertama: ") 
        angka_kedua = raw_input("Masukkan angka kedua: ")
        print "Hasil pembagian kedua angka:"
        print operasi.bagi(angka_pertama, angka_kedua)
        print "\n"
    elif pilihan == "x":
        program_berjalan = False
    else:
        print "Silakan pilih sesuai simbol yang tersedia."
        print "\n"

else:
    print "Terima kasih telah menggunakan Kalkulatorku."
