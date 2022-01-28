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

keuzen = int(input("hoeveel mm wil je hebben?"))

print(mmzak(keuzen))


