#Created By JiKo_KiZoRa
# -*- coding: utf-8 -*-
 
import marshal
import os
import time
import getpass
import sys
import random
 
m = '\033[31;3m'
y = '\033[93;1m'
u = '\033[95;1m'
b = '\033[94;1m'
h = '\033[92;1m'
###
a = '\033[90m'
m = '\033[91m'
h = '\033[92m'
k = '\033[93m'
b = '\033[94m'
u = '\033[95m'
bm = '\033[96m'
p = '\033[97m'
 
 
os.system('cowsay -f eyes "TEAM : TDP Official Group" | lolcat')
os.system('toilet -f standard "JiKoKiZoRa" | lolcat')
os.system('neofetch')
print b+68*"="
user = raw_input(y+'MASUKKAN NAMA ANDA [KAPITAL] : ')
print h+68*"="
print "     "+bm+user+h+",SELAMAT DATANG DI TOOL TEBAK TANGGAL LAHIR !"
print h+68*"="
 
input = 1
 
while input == 1:
                                                                        try:
                                                                            use = getpass.getpass(bm+user+y+', MASUKKAN PASSWORDNYA : ')
                                                                            if use == '123':
                                                                                print u+68*"="
                                                                                print h+"SEDANG MEMPERSIAPKAN BAHAN-BAHAN YANG ANDA BUTUHKAN !"
                                                                                print u+68*"="
                                                                                time.sleep(1)
                                                                                break
                                                                            else:
                                                                                print m+"["+y+"*"+m+"]"+u+user+", TOLONG MASUKKAN PASWORD YANG BENAR !"
                                                                                print y+"ULANGI LAGI !"
                                                                                print m+68*"+"
                                                                                time.sleep(1)
                                                                        except:
                                                                            print y+15*"%"
                                                                            print m+user+", JANGAN MEMAKSA KELUAR, LEBIH BAIK ANDA MENCARI TAHU TENTANG PEMBUAT TOOL INI !!"
                                                                            print y+68*"&"
                                                                            time.sleep(1)
                                                                            continue
 
__banner1__ = b+"""                        _______________________
                        |     |     |    |    |
                        |  1  |   3 |  5 |  7 |
                        |  9  |  11 | 13 | 15 |
                        | 17  |  19 | 21 | 23 |
                        | 25  |  27 | 29 | 31 |
                        |_____|_____|____|____|"""
 
__banner2__ = h+"""                        _______________________
                        |     |     |    |    |
                        |  2  |   3 |  6 |  7 |
                        | 10  |  11 | 14 | 15 |
                        | 18  |  19 | 22 | 23 |
                        | 26  |  27 | 30 | 31 |
                        |_____|_____|____|____|"""
 
 
__banner3__ = m+"""                        _______________________
                        |     |     |    |    |
                        |  4  |   5 |  6 |  7 |
                        | 12  |  13 | 14 | 15 |
                        | 20  |  21 | 22 | 23 |
                        | 28  |  29 | 30 | 31 |
                        |_____|_____|____|____|"""
 
__banner4__ = y+"""                        _______________________
                        |     |     |    |    |
                        |  8  |   9 | 10 | 11 |
                        | 12  |  13 | 14 | 15 |
                        | 24  |  25 | 26 | 27 |
                        | 28  |  29 | 30 | 31 |
                        |_____|_____|____|____|"""
 
 
__banner5__ = bm+"""                        _______________________
                        |     |     |    |    |
                        | 16  |  17 | 18 | 19 |
                        | 20  |  21 | 22 | 23 |
                        | 24  |  25 | 26 | 27 |
                        | 28  |  29 | 30 | 31 |
                        |_____|_____|____|____|"""
 
 
 
os.system('toilet -f standard "               Card - A" | lolcat')
print bm+68*" "
print __banner1__
print bm+68*"¿"
ulang = 0
while ulang == 0:
    try:
        satu = raw_input(bm+user+y+', APAKAH TGL LAHIR ANDA PADA '+b+'{ CARD A } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if satu == 'y' :
            card1 = ('1')
            print u+68*"="
            print h+"OK " +bm+user+h+", MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif satu == 'n':
            card1 = ('0')
            print u+68*"="
            print h+"OK " +bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print m+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
 
os.system('toilet -f standard "               Card - B" | lolcat')
print y+68*"ï"
print __banner2__
print y+68*"ï"
ulang = 1
while ulang == 1:
    try:
        dua = raw_input(bm+user+y+', APAKAH TGL LAHIR ANDA PADA '+b+'{ CARD B } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if dua == 'y' :
            card2 = ('2')
            print u+68*"="
            print h+"OK "+bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif dua == 'n':
            card2 = ('0')
            print u+68*"="
            print h+"OK " +bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print bm+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
 
 
os.system('toilet -f standard "               Card - C" | lolcat')
print b+68*"ï¿½"
print __banner3__
print b+68*"ï¿½"
ulang = 2
while ulang == 2:
    try:
        tiga = raw_input(bm+user+y+', APAKAH TGL LAHIR ANDA PADA '+b+'{ CARD C } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if tiga == 'y' :
            card3 = ('4')
            print u+68*"="
            print h+"OK "+bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif tiga == 'n':
            card3 = ('0')
            print u+68*"="
            print h+"OK "+bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print bm+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
 
 
os.system('toilet -f standard "               Card - D" | lolcat')
print h+68*"ï¿½"
print __banner4__
print h+68*"ï¿½"
ulang = 3
while ulang == 3:
    try:
        empat = raw_input(bm+user+y+', APAKAH TGL LAHIR ANDA PADA '+b+'{ CARD D } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if empat == 'y' :
            card4 = ('8')
            print u+68*"="
	    print h+"OK "+bm+user+h+",  MENUJU CARD SELANJUTNYA !"
	    print u+68*"="
            time.sleep(1)
            break
        elif empat == 'n':
            card4 = ('0')
	    print u+68*"="
	    print h+"OK "+bm+user+h+",  MENUJU CARD SELANJUTNYA !"
	    print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print bm+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
 
 
os.system('toilet -f standard "               Card - E" | lolcat')
print u+68*"ï¿½"
print __banner5__
print u+68*"ï¿½"
ulang = 0
while ulang == 0:
    try:
        lima = raw_input(bm+user+y+', APAKAH TGL LAHIR ANDA PADA '+b+'{ CARD E } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if lima == 'y' :
            card5 = ('16')
            time.sleep(1)
            break
        elif lima == 'n':
            card5 = ('0')
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print bm+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
 
__banner6__ = bm+"""                        ___________________
                        |     |     |     |
                        |  1  |  3  |  4  |
                        |-----|-----|-----|
                        |  6  |  7  | 10  |
                        |_____|_____|_____|"""
 
__banner7__ = y+"""                        ___________________
                        |     |     |     |
                        |  2  |  3  |  4  |
                        |-----|-----|-----|
                        |  6  |  8  |  11 |
                        |_____|_____|_____|"""
 
__banner8__ = h+"""                        ___________________
                        |     |     |     |
                        |  4  |  5  |  6  |
                        |-----|-----|-----|
                        |  9  |  10 |  11 |
                        |_____|_____|_____|"""
 
__banner9__ = b+"""                        ___________________
                        |     |     |     |
                        |  7  |  8  |  9  |
                        |-----|-----|-----|
                        |  10 |  11 | 15  |
                        |_____|_____|_____|"""
 
print bm+68*"="
def mengetik(w):
    for n in w + '\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik(h+'                PENEBAK TANGGAL LAHIR SUDAH BERAKHIR\n          SEKARANG MENUJU TABEL PENEBAK BULAN LAHIR ANDA')
print bm+68*"="
 
os.system('toilet -F metal "Card - A1" | lolcat')
print m+68*"Ã"
print __banner6__
print m+68*"¿"
ulang = 0
while ulang == 0:
    try:
        enam = raw_input(bm+user+y+', APAKAH BULAN LAHIR ANDA PADA '+b+'{ CARD A1 } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if enam == 'y' :
            card6 = ('1')
            print u+68*"="
            print h+"OK " +bm+user+h+", MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif enam == 'n':
            card6 = ('0')
            print u+68*"="
            print h+"OK " +bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print m+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
os.system('toilet -F metal "Card - B1" | lolcat')
print b+68*"Ã"
print __banner7__
print b+68*"¿"
ulang = 0
while ulang == 0:
    try:
        tujuh = raw_input(bm+user+y+', APAKAH BULAN LAHIR ANDA PADA '+b+'{ CARD B1 } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if tujuh == 'y' :
            card7 = ('2')
            print u+68*"="
            print h+"OK " +bm+user+h+", MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif tujuh == 'n':
            card7 = ('0')
            print u+68*"="
            print h+"OK " +bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print m+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
os.system('toilet -F metal "Card - C1" | lolcat')
print y+68*"Ã"
print __banner8__
print y+68*"¿"
ulang = 0
while ulang == 0:
    try:
        delapan = raw_input(bm+user+y+', APAKAH BULAN LAHIR ANDA PADA '+b+'{ CARD C1 } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if delapan == 'y' :
            card8 = ('3')
            print u+68*"="
            print h+"OK " +bm+user+h+", MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        elif delapan == 'n':
            card8 = ('0')
            print u+68*"="
            print h+"OK " +bm+user+h+",  MENUJU CARD SELANJUTNYA !"
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print m+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
os.system('toilet -F metal "Card - D1" | lolcat')
print bm+68*"Ã"
print __banner9__
print bm+68*"¿"
ulang = 0
while ulang == 0:
    try:
        sembi = raw_input(bm+user+y+', APAKAH BULAN LAHIR ANDA PADA '+b+'{ CARD D1 } '+y+'ADA ? '+m+'[y/n] '+h+': ')
        if sembi == 'y' :
            card9 = ('6')
            print u+68*"="
            time.sleep(1)
            break
        elif sembi == 'n':
            card9 = ('0')
            print u+68*"="
            time.sleep(1)
            break
        else:
            print bm+68*"#"
            print m+"["+y+"!"+m+"]"+bm+user+y+", MASUKKAN ANTARA "+h+"[y/n] "+y+"SAJA !"
            print m+68*"-"
            print m+68*"-"
            print h+"TOLONG ULANGI LAGI !"
            time.sleep(1)
    except:
            time.sleep(3)
            print m+68*"%"
            print m+user+y+", JANGAN MEMAKSA KELUAR"
            continue
 
 
print b+68*"="
print bm+user+h+", ANDA LAHIR PADA : "
 
jumlah = int(card1) + int(card2) + int(card3) + int(card4) + int(card5)
 
bulan = int(card6) + int(card7) + int(card8) + int(card9)
 
if jumlah == 1:
    os.system('toilet -F metal "  = 1 =" ')
elif jumlah == 2:
    os.system('toilet -F metal "  = 2 =" ')
elif jumlah == 3:
    os.system('toilet -F metal "  = 3 =" ')
elif jumlah == 4:
    os.system('toilet -F metal "  = 4 =" ')
elif jumlah == 5:
    os.system('toilet -F metal "  = 5 =" ')
elif jumlah == 6:
    os.system('toilet -F metal "  = 6 =" ')
elif jumlah == 7:
    os.system('toilet -F metal "  = 7 =" ')
elif jumlah == 8:
    os.system('toilet -F metal "  = 8 =" ')
elif jumlah == 9:
    os.system('toilet -F metal "  = 9 =" ')
elif jumlah == 10:
    os.system('toilet -F metal "  = 10 =" ')
elif jumlah == 11:
    os.system('toilet -F metal "  = 11 =" ')
elif jumlah == 12:
    os.system('toilet -F metal "  = 12 =" ')
elif jumlah == 13:
    os.system('toilet -F metal "  = 13 =" ')
elif jumlah == 14:
    os.system('toilet -F metal "  = 14 =" ')
elif jumlah == 15:
    os.system('toilet -F metal "  = 15 =" ')
elif jumlah == 16:
    os.system('toilet -F metal "  = 16 =" ')
elif jumlah == 17:
    os.system('toilet -F metal "  = 17 =" ')
elif jumlah == 18:
    os.system('toilet -F metal "  = 18 =" ')
elif jumlah == 19:
    os.system('toilet -F metal "  = 19 =" ')
elif jumlah == 20:
    os.system('toilet -F metal "  = 20 =" ')
elif jumlah == 21:
    os.system('toilet -F metal "  = 21 =" ')
elif jumlah == 22:
    os.system('toilet -F metal "  = 22 =" ')
elif jumlah == 23:
    os.system('toilet -F metal "  = 23 =" ')
elif jumlah == 24:
    os.system('toilet -F metal "  = 24 =" ')
elif jumlah == 25:
    os.system('toilet -F metal "  = 25 =" ')
elif jumlah == 26:
    os.system('toilet -F metal "  = 26 =" ')
elif jumlah == 23:
    os.system('toilet -F metal "  = 23 =" ')
elif jumlah == 24:
    os.system('toilet -F metal "  = 24 =" ')
elif jumlah == 25:
    os.system('toilet -F metal "  = 25 =" ')
elif jumlah == 26:
    os.system('toilet -F metal "  = 26 =" ')
else:
    os.system('toilet -F metal "  = 31 =" ')
 
 
if bulan == 1:
    os.system('toilet -F gay " JANUARI" ')
elif bulan == 2:
    os.system('toilet -F gay " FEBRUARI" ')
elif bulan == 3:
    os.system('toilet -F gay "   MARET" ')
elif bulan == 4:
    os.system('toilet -F gay "   APRIL" ')
elif bulan == 5:
    os.system('toilet -F gay "   MEI" ')
elif bulan == 6:
    os.system('toilet -F gay "   JUNI" ')
elif bulan == 7:
    os.system('toilet -F gay "   JULI" ')
elif bulan == 8:
    os.system('toilet -F gay " AGUSTUS" ')
elif bulan == 9:
    os.system('toilet -F gay " SEPTEMBER" ')
elif bulan == 10:
    os.system('toilet -F gay " OKTOBER" ')
elif bulan == 11:
    os.system('toilet -F gay " NOVEMBER" ')
else:
    os.system('toilet -F gay " DESEMBER" ')
 
print b+68*"="
 
def mengetik(z):
    for y in z + '\n':
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik(h+'      TERIMA KASIH TELAH MENGGUNAKAN TOOL INI..\nSALAM KAMI, MEMBER OF [TDP Official Group]')
 
print h+68*"="

