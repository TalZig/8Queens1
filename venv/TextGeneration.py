from random import randrange
import random

def initialPopulation():
    pop = []
    size = 1200
    for i in range(size):
        chrome = []

        for j in range(298):
            chrome.append(randrange(28))

        pop.append(chrome)

    return pop

def fromStrToArr(s):
    arr = []
    for i in range(298):
        if s[i] == '.':
            arr.append(26)
        elif s[i] == ' ':
            arr.append(27)
        else:
            arr.append(ord(s[i]) - ord('a'))
    return arr

def fromArrToStr(a):
    s = ""
    for i in range(298):
        if a[i] == 27:
            s = s + " "
        elif a[i] == 26:
            s = s + "."
        else:
            s = s + chr(s[i] + ord('a'))
    return s

def fitnessFunction(ans, chrom):
    score = 298
    for i in range(298):
        if ans[i] != chrom[i]:
            score = score - 1
    return score


def createNextGen(currGen, grades):
    nextGen =[]

    # elitism
    for i in range(4):
        # highest = grades.index(max(grades))
        #temp = currGen[highest]
        #nextGen.append(temp)
        #currGen.pop(highest)
        #grades.pop(highest)

        lowest = grades.index(min(grades))
        currGen.pop(lowest)
        grades.pop(lowest)
    grades, currGen = zip(*sorted(zip(grades, currGen)))
    pool = []
    nextGen.append(currGen[len(currGen)-1])
    nextGen.append(currGen[len(currGen)-2])
    nextGen.append(currGen[len(currGen) -3])
    nextGen.append(currGen[len(currGen)-4])
    help = 1
    for i in range(len(grades)):
        count = help*2
        while count > 0:
            pool.append(currGen[i])
            count = count - 1
        help = help + 1


    for k in range((int)(len(grades)/2)):
        choose = randrange(len(pool))
        parent1 = pool[choose]
        choose = randrange(len(pool))
        parent2 = pool[choose]

        child1, child2 = crossOver(parent1, parent2)
        nextGen.append(child1)
        nextGen.append(child2)

    return nextGen

def specialSort(l1, l2):
    for i in range(len(l1) - 1):
        for j in range(len(l1) - 1 - i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                l2[j], l2[j + 1] = l2[j + 1], l2[j]

def crossOver(p1, p2):
    randNum = random.randint(0, 100)
    if (randNum < 25):
        return p1, p2
    c1 = []
    c2 = []
    for j in range(298):
        i = random.randint(0, 1)
        if(i == 1):
            c1.append(p1[j])
            c2.append(p2[j])
        else:
            c1.append(p2[j])
            c2.append(p1[j])

    for i in range (298):
        randNum = random.randint(0, 400)
        if(randNum < 1):
            c1 = mutation(c1,i)
        randNum = random.randint(0,400)
        if(randNum < 1):
            c2 = mutation(c2,i)
    return c1, c2

def mutation(list, i):
    list[i] = random.randint(0, 28)
    return list

def main():
    origin = "to be or not to be that is the question. whether tis nobler in the mind to suffer. the slings and arrows of outrageous fortune. or to take arms against a sea of troubles and by opposing end them. to die to sleep. no more. and by a sleep to say we end. the heartache and the thousand natural shocks."
    correctAns = fromStrToArr(origin)
    grades = []
    currGen = initialPopulation()
    for l in currGen:
        grades.append(fitnessFunction(correctAns, l))
    gen = 1

    while 298 not in grades:
        currGen = createNextGen(currGen, grades)
        grades = []
        for l in currGen:
            grades.append(fitnessFunction(correctAns, l))
        gen = gen + 1
        # if gen % 750 == 0:
        #     currGen = initialPopulation()
        print("gen: " + str(gen))
        print("max grade: " + str(max(grades)))
        print("")

    index = grades.index(298)
    print(fromArrToStr(currGen[index]))


    # print ans


if __name__ == "__main__":
    main()