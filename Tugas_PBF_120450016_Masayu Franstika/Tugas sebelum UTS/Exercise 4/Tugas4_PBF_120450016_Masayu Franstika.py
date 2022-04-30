import math
import random
lamda1 = 1.148698355 
lamda2 = 0.8705505633 

#Menghitung goal yang dicetak oleh tim tuan rumah
def tuanRumah(homeRating,awayRating):
    global lamda1
    global x
    global y
    if x == y:
        raise ValueError
    else:
        lamb = lamda1**(int(homeRating)-int(awayRating))
        homeScore = 0
        z = random.random()    
        while z > 0:
            z = z - ((lamb**homeScore * math.exp(lamb * -1))/(math.factorial(homeScore)))
            homeScore += 1
        return (homeScore-1)

#Menghitung goal yang dicetak oleh tim lawan
def timLawan(homeRating,awayRating):
    global lamda2
    global x
    global y
    #Pengecekan untuk menghentikan pemain
    if x == y:
        raise ValueError
    else:
        lamb = lamda2**(int(homeRating)-int(awayRating))
        awayScore = 0
        z = random.random()    
        while z > 0:
            z = z - ((lamb**awayScore * math.exp(lamb * -1))/(math.factorial(awayScore)))
            awayScore += 1
        return (awayScore-1)

leagueSize = int(input("Masukan Jumlah Tim Dalam Liga : "))

#Inisialisasi Array Tim Dalam Liga
namatim = []
skill = []
point_tim = []
teamFor = []
perlawanan = []
kemenangan = []
seri = []
kekalahan = []

for x in range(leagueSize):
    point_tim += [0]
    teamFor += [0]
    perlawanan += [0]
    kemenangan += [0]
    seri += [0]
    kekalahan += [0]

#Memasukan nama  tim dan peringkat
for i in range(leagueSize):
    namatim += [input("Tim  : " +str(i+1)+" Nama Tim: ")]
for j in range(leagueSize):
    skill += [input("Nama Tim : " +namatim[j]+ " Peringkat : ")]

#Inisialisasi Variabel
homeScore = 0
awayScore = 0

for x in range(leagueSize):
    print(namatim[x] + " Pertandingan Kandang : ")
    print("------------------------------------------\n")
    for y in range(leagueSize):
        error = 0
        try:
            homeScore = tuanRumah(skill[x],skill[y])
        except ValueError:
            pass
            error += 1
        try:
            awayScore = timLawan(skill[x],skill[y])
        except ValueError:
            pass
        if error == 0:
            #Update List
            print(namatim[x],homeScore,"-",awayScore,namatim[y],"\n")
            teamFor[x] += homeScore
            teamFor[y] += awayScore
            perlawanan[x] += awayScore
            perlawanan[y] += homeScore
            if homeScore > awayScore:
                kemenangan[x] += 1
                kekalahan[y] += 1
                point_tim[x] += 3
            elif homeScore == awayScore:
                seri[x] += 1
                seri[y] += 1
                point_tim[x] += 1
                point_tim[y] += 1
            else:
                kemenangan[y] += 1
                kekalahan[x] += 1
                point_tim[y] += 3
        else:
            pass

print("Hasil Akhir : ")
for x in range(leagueSize):
    print(namatim[x]+(15-len(namatim[x]))*" "+" Peringkat : "+str(skill[x])+(5-len(str(skill[x])))*" "+" Point: "+str(point_tim[x])+(5-len(str(point_tim[x])))*" "+" For: "+str(teamFor[x])+(5-len(str(teamFor[x])))*" "+" Perlawanan: "+str(perlawanan[x])+(5-len(str(point_tim[x])))*" "+"Selisih Gol: "+str(teamFor[x]-perlawanan[x])+(5-len(str(teamFor[x]-perlawanan[x])))*" "+" Menang : "+str(kemenangan[x])+(5-len(str(kemenangan[x])))*" "+" Seri : "+str(seri[x])+(5-len(str(seri[x])))*" "+" Kalah : "+str(kekalahan[x])+(5-len(str(kekalahan[x])))*" ")
point_tim.sort()
print(point_tim)