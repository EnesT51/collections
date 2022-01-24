import random
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList,minimum,maximaal):
    leeglist =[]
    x = random.randrange(minimum,maximaal)
    for i in range(x):
        spel = random.choice(spelList)
        leeglist.append(spel)
    return leeglist


print(spelProgramma(spelList,3,11))


