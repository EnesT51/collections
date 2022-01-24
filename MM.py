import random

kleuren = ["oranje", "blauw", "groen", "bruin"]

def zak(aantal:int):
    leeglijst =[]
    for i in range(aantal):
        leeglijst.append(random.choice(kleuren))
    
    print(leeglijst)
aantal = int (input("hoeveel m&m wil je? "))
zak(aantal)






     


