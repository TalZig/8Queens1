import random
def fitnessFunction(list):
    grade = 49
    slant = 0
    for i in range(0,7):
        for j in range(i + 1,7):
            slant = j - i
            if(list[i] == list[j]):
                grade = grade - 2
            else:
                if(list[i] + slant == list[j] or list[i] - slant == list[j]):
                    grade = grade - 2
    return grade


def mutation(list, i):
    list[i] = random.randint(0,7)
    return list

def crossOver(list1, list2):
    randNum = random.randint(0,10)
    if(randNum <2):
        return list1 ,list2
    childrenList1 =[]
    childrenList2 = []
    for j in range(0,7):
        i = random.randint(0, 1)
        if(i == 1):
            childrenList1[j] = list1[j]
            childrenList2[j] = list2[j]
        else:
            childrenList1[j] = list2[j]
            childrenList2[j] = list1[j]

    for i in range (0,7):
        randNum = random.randint(0, 500)
        if(randNum == 0):
            childrenList1 = mutation(childrenList1,i)
        randNum = random.randint(0,500)
        if(randNum == 0):
            childrenList2 = mutation(childrenList2,i)
        return childrenList1, childrenList2