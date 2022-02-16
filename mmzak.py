import random
def mmzak(aantal):
    mm ={
        "rood":0,
        "blauw":0,
        "geel":0,
        "bruin":0
    }
    kleuren = ["blauw", "rood","geel","bruin"]
    for i in range(aantal):
        mm [random.choice(kleuren)] +=1
    return mm 

kleuren = ["oranje", "blauw", "groen", "bruin"]

def zak(aantal:int):
    leeglijst =[]
    for i in range(aantal):
        leeglijst.append(random.choice(kleuren))
    
    return leeglijst

keuzen = int(input("hoeveel mm wil je hebben?"))

lijst = mmzak(keuzen)

def gesorteerd(sorteer):
    if isinstance (sorteer,list):
        sortedd = sorted(sorteer)
        return sortedd
    else:
        return dict(sorted(lijst.items(), key=lambda x:x[1]))

print(gesorteerd(lijst))

