with open('bilangan1.txt','r') as x:
    ConvertString1 = x.read()
    ConvertString1 = int(ConvertString1)
    #Cek Import Data
    print('Nilai Bilangan Pertama adalah : ', ConvertString1)
print(135*"-")

with open('bilangan2.txt','r') as y:
    ConvertString2 = y.read()
    ConvertString2 = int(ConvertString2)
    #Cek Import Data
    print('Nilai Bilangan kedua adalah : ', ConvertString2)
print(135*"-")

def Jumlah():
    return ConvertString1 + ConvertString2

print('Hasil dari penjumlahan 100 digit bilangan diatas adalah : ',Jumlah())