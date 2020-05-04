from random import randrange
import random
import time


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
            s = s + chr(a[i] + ord('a'))

    return s


def fitnessFunction(ans, chrom):
    score = 298
    for i in range(298):
        if ans[i] != chrom[i]:
            score = score - 1
    return score


def createNextGen(currGen, grades):
    nextGen = []

    # elitism
    for i in range(4):
        lowest = grades.index(min(grades))
        currGen.pop(lowest)
        grades.pop(lowest)
    nextGen.append(currGen[len(currGen) - 1])
    nextGen.append(currGen[len(currGen) - 2])
    nextGen.append(currGen[len(currGen) - 3])
    nextGen.append(currGen[len(currGen) - 4])


    grades, currGen = zip(*sorted(zip(grades, currGen)))
    pool = []

    help = 1
    for i in range(len(grades)):
        count = help
        while count > 0:
            pool.append(currGen[i])
            count = count - 1
        help = help + 1

    for k in range((int)(len(grades) / 2)):
        choose = randrange(len(pool))
        parent1 = pool[choose]
        choose = randrange(len(pool))
        parent2 = pool[choose]

        child1, child2 = crossOver(parent1, parent2)
        nextGen.append(child1)
        nextGen.append(child2)

    return nextGen


def crossOver(p1, p2):
    randNum = random.randint(0, 99)
    crossOver_rate = 25
    if (randNum < crossOver_rate):
        return p1, p2
    c1 = []
    c2 = []
    for j in range(298):
        i = random.randint(0, 1)
        if (i == 1):
            c1.append(p1[j])
            c2.append(p2[j])
        else:
            c1.append(p2[j])
            c2.append(p1[j])

    # decide wether to make mutation or not
    mutation_rate = 1
    for i in range(298):
        randNum = random.randint(0, 399)
        if (randNum < mutation_rate):
            c1 = mutation(c1, i)
        randNum = random.randint(0, 399)
        if (randNum < mutation_rate):
            c2 = mutation(c2, i)
    return c1, c2

#mutation for a single char in solution
def mutation(list, i):
    list[i] = random.randint(0, 27)
    return list


def main():
    start_time = time.time()
    #create correct ans
    origin = "to be or not to be that is the question. whether tis nobler in the mind to suffer. the slings and arrows of outrageous fortune. or to take arms against a sea of troubles and by opposing end them. to die to sleep. no more. and by a sleep to say we end. the heartache and the thousand natural shocks."
    correctAns = fromStrToArr(origin)

    #first set of grades
    grades = []
    currGen = initialPopulation()
    for l in currGen:
        grades.append(fitnessFunction(correctAns, l))
    gen = 1

    perfect_score = 298
    while perfect_score not in grades:
        currGen = createNextGen(currGen, grades)
        grades = []
        for l in currGen:
            grades.append(fitnessFunction(correctAns, l))
        gen = gen + 1

    #print solution
    index = grades.index(perfect_score)
    print("Solution found after " + str(gen) + " generations.")
    print("Running time: %s " % (time.time() - start_time) + "seconds.")
    print(fromArrToStr(currGen[index]))


if __name__ == "__main__":
    main()
