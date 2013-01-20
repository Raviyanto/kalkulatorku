# Definisikan
import galat

def tambah(a, b):
    try:
        return galat.iniString(a) + galat.iniString(b)
    except ValueError:
        print "Perhatikan ini bukan angka!"

def kurang(a, b):
    try:    
        return galat.iniString(a) - galat.iniString(b)
    except ValueError:
        print "Perhatikan ini bukan angka!"

def kali(a, b):
    try:
        return galat.iniString(a) * galat.iniString(b)
    except ValueError:
        print "Perhatikan ini bukan angka!"

def bagi(a, b):
    try:
        return galat.iniString(a) / galat.iniString(b)
    except ZeroDivisionError:
        print "Perhatikan bilangan kedua adalah nol!"
    except ValueError:
        print "Perhatikan ini bukan angka!"    
