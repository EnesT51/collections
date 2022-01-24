dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print(dagen)
print(dagen[0:5])
print(dagen[5:7])
dagen.reverse()
print(dagen)
print(dagen[2:7])
print(dagen[0:2])

list1 =[1,2,3,4,5,6,7,8,9,10]
list2 =[2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists(list1,list2):
    print("----------------------")
    for teller in range(10):
        print(list1[teller], "+", list2[teller], "=",list1[teller] + list2[teller])

addAndDisplayLists(list1,list2)

def substractAndDisplayLists(list1, list2):
    print("-----------------------")
    for teller in range(10):
        print(list1[teller], "-", list2[teller], "=",list1[teller] - list2[teller])

substractAndDisplayLists(list1,list2)

def multiplyAndDisplayLists(list1, list2):
    print("-----------------------")
    for teller in range(10):
        print(list1[teller], "*", list2[teller], "=",list1[teller] * list2[teller])

multiplyAndDisplayLists(list1,list2)

def divideAndDisplayLists(list1, list2):
    print("-----------------------")
    for teller in range(10):
        print(list1[teller], "/", list2[teller], "=",list1[teller] / list2[teller])

divideAndDisplayLists(list1,list2)





