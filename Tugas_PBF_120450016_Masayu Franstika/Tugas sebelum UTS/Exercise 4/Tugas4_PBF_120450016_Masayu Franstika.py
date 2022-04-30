import numpy as np
import random

skill_tim_A = {'save': 81, 'tackle1': 79, 'passing': 78, 'tackle2':60, 'dribble1': 76, 'dribble2': 80, 'intercepts':85, 'shoot': 92}
skill_tim_B = {'save': 86, 'tackle1': 80, 'passing': 81, 'tackle2':70, 'dribble1': 70, 'dribble2': 81, 'intercepts':86, 'shoot': 90}
mentality_A = {'GK':80, 'DF':79, 'MD':78, 'ATK':77}
mentality_B = {'GK':77,'DF':78, 'MD':79, 'ATK':80}
supporter_A = 100000
Supporter_B = 115000
b = 0
a = 0
t = 90

curr = "A"
def cek_skill(skill, mentality):
    def alpha(mentality):
        return np.random.uniform(0,0.025) * (mentality/100)
    def beta():
        return np.random.uniform(0,0.025) * (supporter_A/(supporter_A+Supporter_B))
    return skill*(1-(alpha(mentality)+beta()))

def md_(x,y):
    return cek_skill(x,y)

def atk_(x,y):
    return cek_skill(x,y)

def gk_(x,y):
    return cek_skill(x,y)

def df_(x,y):
    return cek_skill(x,y)

def mulai():
    fieldMid()

def hasil():
    global a, b
    return print(f'skor sementara :  {a} - {b}')

def stopBreak(x):
    x = 0
    return x
def hasil_final():
    global a,b
    return print(f'skor akhir {a} - {b}')
    
def fieldMid():
    global t, curr
    if t >= 0:
        if curr == "A":
            if md_(skill_tim_A.get('dribble1'), mentality_A.get('MD')) > md_(skill_tim_B.get('tackle2'), mentality_B.get('MD')):
                t -= 1
                print('Bola dipassing ke striker tim A')
                print(f'waktu  tersisa {t} menit')
                curr = "A"
            else:
                t -= 2
                print('Bola diambil oleh striker tim B')
                print(f'waktu  tersisa {t} menit')
                curr = "B"
        else:
            if md_(skill_tim_B.get('dribble1'), mentality_B.get('MD')) > md_(skill_tim_A.get('tackle2'), mentality_A.get('MD')):
                t -= 1
                print('Bola passing ke striker tim B')
                print(f'waktu  tersisa {t} menit')
                curr = "B"
            else:
                t -= 2
                print('Bola direbut oleh striker tim A')
                print(f'waktu  tersisa {t} menit')
                curr = "A"
        fieldAtk()
    else:
        stopBreak(t)
            
def fieldAtk():
    global t, curr, a, b
    if t >= 0:
        if curr == "B":
            if atk_(skill_tim_B.get('dribble2'),mentality_B.get('ATK')) > df_(skill_tim_A.get('tackle1'),mentality_A.get('DF')):
                print('striker tim B akan melakukan shooting')
                print(f'waktu  tersisa {t} menit')
                t -= 1
                if atk_(skill_tim_B.get('shoot'),mentality_B.get('ATK')) > gk_(skill_tim_A.get('save'),mentality_A.get('GK')):
                    t -= 2
                    print('GOALLLLL!!!!')
                    print(f'waktu tersisa {t} menit')
                    b += 1
                    hasil()
                    fieldMid()
                    curr = "B"
                else:
                    t -= 3
                    print('sayang sekali bung, bola tidak memasuki gawang')
                    print(f'waktu  tersisa {t} menit')
                    curr = "A"
            else:
                t -= 2
                print('Bola direbut oleh bek dari tim A')
                print(f'waktu  tersisa {t} menit')
                curr = "A"
        else:
            if atk_(skill_tim_A.get('dribble2'),mentality_A.get('ATK')) > df_(skill_tim_B.get('tackle1'),mentality_B.get('DF')):
                t -= 1
                print('striker tim A akan melakukan shooting')
                print(f'waktu  tersisa {t} menit')
                if atk_(skill_tim_A.get('shoot'),mentality_A.get('ATK')) > gk_(skill_tim_B.get('save'),mentality_B.get('GK')):
                    t -= 2
                    print('GOALLLLL!!!!')
                    print(f'waktu  tersisa {t} menit')
                    a += 1
                    hasil()
                    fieldMid()
                    curr = "A"
                else:
                    t -= 3
                    print('sayang sekali bung, bola tidak memasuki gawang')
                    print(f'waktu tersisa {t} menit')
                    curr = "B"
            else:
                t -= 2
                print('Bola direbut oleh bek dari tim B')
                print(f'waktu tersisa {t} menit')
                curr = "B"
        fieldDf()
    else:
        stopBreak(t)

def fieldDf():
    global curr, t
    if t >= 0:
        if curr == "B":
            if df_(skill_tim_B.get('passing'), mentality_B.get('DF')) > atk_(skill_tim_A.get('intercepts'),  mentality_A.get('ATK')):
                t -= 2
                print('Bola passing ke pemain gelandang B')
                fieldMid()
            else:
                t -= 1
                print('Bola direbut oleh striker tim A')
                fieldAtk()
        else:
            if df_(skill_tim_A.get('passing'), mentality_A.get('DF')) > atk_(skill_tim_B.get('intercepts'),  mentality_B.get('ATK')):
                t -= 2
                print('Bola dioper ke pemain gelandang A')
                fieldMid()
            else:
                t -= 1
                print('Bola direbut oleh striker tim B')
                fieldAtk() 
    else:
        stopBreak(t)
mulai()
