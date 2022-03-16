#Encryption
def checkLen(psswrd, lim):
    return False if (len(psswrd) > lim) or (len(psswrd) <=0) else True
def tf1(ch, params):
    return chr(( ord(ch) // params['c'])+ params['b'])
def tf2(ch, params):
    return chr( (ord(ch) % params['c'])+ params['b'])
def tf3(firstval, secval):
    return '+' if (firstval> secval ) else '-'
def tf(ch, params):
    return tf1(ch, params)+ tf2(ch,params)+(tf3(tf1(ch, params), tf2(ch, params) ) )
def enkrip(psswrd, params):
    return ''.join ([ tf( passw, params) for passw in psswrd] )

#Decryption
def d_sisa(ch, params):
    return ord(ch) - params['b']
def d_div(ch, params):
    return d_sisa(ch, params) *params['c']
def dtf(ch1, ch2, params):
    return chr (d_div(ch1, params)+d_sisa(ch2, params))
def dekrip(psswrd, params):
    return ''.join( [ dtf(psswrd[i], psswrd[i+1] ,params) for i in range(0, len(psswrd), 3) ] )

#Visualization
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def show_password(db):
    clear()
    print('Menampilkan Password :')
    print()
    maks = max(map( lambda x: len(x[0]), db))
    maks_total= max( map(lambda x:len(x[0] + x[1] ),db) )
    hiasan = lambda n:'' .join( ['-' for i in range(n) ])
    span= 5
    connector =':'
    print( hiasan (maks_total+ span+ len(connector) ) )
    for passw in db:
        tambahan_space= maks-len(passw[0])+span
        tam = ' '.join( ['' for i in range(tambahan_space) ] ) 
        print( passw[0] + tam + connector + passw[1] )
        print( hiasan (maks_total+ span + len(connector) ) ) 

lim = 100
p ={'c': 26, 'b': 80}
db = []

print("Pilih 1 = Enkripsi dan 2 = Dekripsi")
pilih = int(input("Masukkan Pilihan : "))
if pilih == 1:
    print("Enkripsi")
    psswrd = input("Masukkan Password : ")
    if checkLen(psswrd, lim) == False:
        print("Password terlalu panjang atau kurang dari 1")
    else:
        print("Password yang di enkripsi : ", enkrip(psswrd, p))
        db.append([psswrd, enkrip(psswrd, p)])
        show_password(db)
elif pilih == 2:
    print("Dekripsi")
    psswrd = input("Masukkan Password : ")
    if checkLen(psswrd, lim) == False:
        print("Password terlalu panjang atau kurang dari 1")
    else:
        print("Password yang di dekripsi : ", dekrip(psswrd, p))
        db.append([psswrd, dekrip(psswrd, p)])
        show_password(db)