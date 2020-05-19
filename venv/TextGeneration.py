from random import randrange
import random
import time
import numpy as np
from numpy.random import choice

PUP_SIZE = 800
MAX_FITNESS = 298
crossOver_rate = 0.25
mutation_rate = 0.005
priority = np.zeros(shape=(PUP_SIZE))
sum = 0

for i in range(PUP_SIZE):
    sum = sum + i + 1

for i in range(PUP_SIZE):
    priority[i] = (i + 1) / sum


def initialPopulation():
    pop = np.zeros(shape=(PUP_SIZE, MAX_FITNESS))
    size = PUP_SIZE
    for i in range(size):
        for j in range(MAX_FITNESS):
            pop[i][j] = randrange(28)

    return pop


def fromStrToArr(s):
    arr = []
    for i in range(MAX_FITNESS):
        if s[i] == '.':
            arr.append(26)
        elif s[i] == ' ':
            arr.append(27)
        else:
            arr.append(ord(s[i]) - ord('a'))
    return arr


def fromArrToStr(a):
    s = ""
    for i in range(MAX_FITNESS):
        if a[i] == 27:
            s = s + " "
        elif a[i] == 26:
            s = s + "."
        else:
            s = s + chr(a[i] + ord('a'))

    return s


def fitnessFunction(ans, chrom):
    # score = MAX_FITNESS
    # for i in range(MAX_FITNESS):
    #     if ans[i] != chrom[i]:
    #         score = score - 1
    return np.count_nonzero(ans == chrom)


def createNextGen(currGen, grades):
    # nextGen.append(currGen[grades.index(max(grades))])
    # grades, currGen = zip(*sorted(zip(grades, currGen)))
    order = grades.argsort()
    currGen = currGen[order]
    grades = grades[order]
    nextGen = np.zeros(shape=(PUP_SIZE, MAX_FITNESS))
    parents = random.choices(population=currGen, weights=priority, k=len(grades))
    for k in range((int)(len(grades) / 2)):
        #        parents = np.random.choices(a = currGen, size = 2, p=priority)

        child1, child2 = crossOver(parents[2 * k], parents[2 * k + 1])
        nextGen[2 * k] = child1
        nextGen[2 * k + 1] = child2

    return nextGen


def crossOver(p1, p2):
    if (np.random.random() < crossOver_rate):
        return p1, p2
    c1 = np.zeros(shape=(MAX_FITNESS))
    c2 = np.zeros(shape=(MAX_FITNESS))
    randArr = np.random.random(size=MAX_FITNESS)

    for j in range(MAX_FITNESS):
        if (randArr[j] < 0.5):
            c1[j] = p1[j]
            c2[j] = p2[j]
        else:
            c1[j] = p2[j]
            c2[j] = p1[j]

    # decide wether to make mutation or not
    mutation(c1, c2)
    return c1, c2


# mutation for a single char in solution
def mutation(c1, c2):
    randArr = np.random.random(size=MAX_FITNESS * 2)
    mutArr = np.random.random_integers(low=0, high=27, size=MAX_FITNESS * 2)
    for i in range(MAX_FITNESS):
        if (randArr[i * 2] < mutation_rate):
            c1[i] = mutArr[i * 2]
        if (randArr[i * 2 + 1] < mutation_rate):
            c2[i] = mutArr[i * 2 + 1]
    return c1, c2


def main():
    from random import randrange
    import random
    import time
    import numpy as np
    from numpy.random import choice

    PUP_SIZE = 800
    MAX_FITNESS = 298
    crossOver_rate = 0.25
    mutation_rate = 0.005
    priority = np.zeros(shape=(PUP_SIZE))
    sum = 0

    for i in range(PUP_SIZE):
        sum = sum + i + 1

    for i in range(PUP_SIZE):
        priority[i] = (i + 1) / sum

    def initialPopulation():
        pop = np.zeros(shape=(PUP_SIZE, MAX_FITNESS))
        size = PUP_SIZE
        for i in range(size):
            for j in range(MAX_FITNESS):
                pop[i][j] = randrange(28)

        return pop

    def fromStrToArr(s):
        arr = []
        for i in range(MAX_FITNESS):
            if s[i] == '.':
                arr.append(26)
            elif s[i] == ' ':
                arr.append(27)
            else:
                arr.append(ord(s[i]) - ord('a'))
        return arr

    def fromArrToStr(a):
        s = ""
        for i in range(MAX_FITNESS):
            if a[i] == 27:
                s = s + " "
            elif a[i] == 26:
                s = s + "."
            else:
                s = s + chr(a[i] + ord('a'))

        return s

    def fitnessFunction(ans, chrom):
        # score = MAX_FITNESS
        # for i in range(MAX_FITNESS):
        #     if ans[i] != chrom[i]:
        #         score = score - 1
        return np.count_nonzero(ans == chrom)

    def createNextGen(currGen, grades):

        # nextGen.append(currGen[grades.index(max(grades))])
        # grades, currGen = zip(*sorted(zip(grades, currGen)))
        order = grades.argsort()
        currGen = currGen[order]
        grades = grades[order]
        nextGen = np.zeros(shape=(PUP_SIZE, MAX_FITNESS))
        parents = random.choices(population=currGen, weights=priority, k=len(grades))
        for k in range((int)(len(grades) / 2)):
            #        parents = np.random.choices(a = currGen, size = 2, p=priority)

            child1, child2 = crossOver(parents[2 * k], parents[2 * k + 1])
            nextGen[2 * k] = child1
            nextGen[2 * k + 1] = child2

        return nextGen

    def crossOver(p1, p2):
        if (np.random.random() < crossOver_rate):
            return p1, p2
        c1 = np.zeros(shape=(MAX_FITNESS))
        c2 = np.zeros(shape=(MAX_FITNESS))
        randArr = np.random.random(size=MAX_FITNESS)

        for j in range(MAX_FITNESS):
            if (randArr[j] < 0.5):
                c1[j] = p1[j]
                c2[j] = p2[j]
            else:
                c1[j] = p2[j]
                c2[j] = p1[j]

        # decide wether to make mutation or not
        mutation(c1, c2)
        return c1, c2

    # mutation for a single char in solution
    def mutation(c1, c2):
        randArr = np.random.random(size=MAX_FITNESS * 2)
        mutArr = np.random.random_integers(low=0, high=27, size=MAX_FITNESS * 2)
        for i in range(MAX_FITNESS):
            if (randArr[i * 2] < mutation_rate):
                c1[i] = mutArr[i * 2]
            if (randArr[i * 2 + 1] < mutation_rate):
                c2[i] = mutArr[i * 2 + 1]
        return c1, c2

    def main():
        start_time = time.time()
        # create correct ans
        origin = "to be or not to be that is the question. whether tis nobler in the mind to suffer. the slings and arrows of outrageous fortune. or to take arms against a sea of troubles and by opposing end them. to die to sleep. no more. and by a sleep to say we end. the heartache and the thousand natural shocks."
        correctAns = np.array(
            [19, 14, 27, 1, 4, 27, 14, 17, 27, 13, 14, 19, 27, 19, 14, 27, 1, 4, 27, 19, 7, 0, 19, 27, 8, 18, 27, 19, 7,
             4, 27, 16, 20, 4, 18, 19, 8, 14, 13, 26, 27, 22, 7, 4, 19, 7, 4, 17, 27, 19, 8, 18, 27, 13, 14, 1, 11, 4,
             17, 27, 8, 13, 27, 19, 7, 4, 27, 12, 8, 13, 3, 27, 19, 14, 27, 18, 20, 5, 5, 4, 17, 26, 27, 19, 7, 4, 27,
             18, 11, 8, 13, 6, 18, 27, 0, 13, 3, 27, 0, 17, 17, 14, 22, 18, 27, 14, 5, 27, 14, 20, 19, 17, 0, 6, 4, 14,
             20, 18, 27, 5, 14, 17, 19, 20, 13, 4, 26, 27, 14, 17, 27, 19, 14, 27, 19, 0, 10, 4, 27, 0, 17, 12, 18, 27,
             0, 6, 0, 8, 13, 18, 19, 27, 0, 27, 18, 4, 0, 27, 14, 5, 27, 19, 17, 14, 20, 1, 11, 4, 18, 27, 0, 13, 3, 27,
             1, 24, 27, 14, 15, 15, 14, 18, 8, 13, 6, 27, 4, 13, 3, 27, 19, 7, 4, 12, 26, 27, 19, 14, 27, 3, 8, 4, 27,
             19, 14, 27, 18, 11, 4, 4, 15, 26, 27, 13, 14, 27, 12, 14, 17, 4, 26, 27, 0, 13, 3, 27, 1, 24, 27, 0, 27,
             18, 11, 4, 4, 15, 27, 19, 14, 27, 18, 0, 24, 27, 22, 4, 27, 4, 13, 3, 26, 27, 19, 7, 4, 27, 7, 4, 0, 17,
             19, 0, 2, 7, 4, 27, 0, 13, 3, 27, 19, 7, 4, 27, 19, 7, 14, 20, 18, 0, 13, 3, 27, 13, 0, 19, 20, 17, 0, 11,
             27, 18, 7, 14, 2, 10, 18, 26])

        # first set of grades
        grades = np.array(np.zeros(shape=(PUP_SIZE)))
        currGen = initialPopulation()
        for i in range(len(currGen)):
            grades[i] = fitnessFunction(correctAns, currGen[i])
        gen = 1

        f = open("t.txt", "w")
        perfect_score = MAX_FITNESS
        bStop = False
        while not bStop:  # perfect_score not in grades:
            currGen = createNextGen(currGen, grades)
            for i in range(len(currGen)):
                grades[i] = fitnessFunction(correctAns, currGen[i])
                if grades[i] == MAX_FITNESS:
                    bStop = True
            gen = gen + 1
            # if(max(grades) == 270):
            #     crossOver_rate = 30
            #     mutation_rate = 2
            f.write(str(max(grades)) + ", " + str(np.average(grades)) + "\n")
            print("max: " + str(max(grades)))
            # print("avg: " + str(sum(grades) / len(grades)))
            print("time: " + str(time.time() - start_time) + "\n")

        # print solution
        print("Solution found after " + str(gen) + " generations.")
        print("Running time: %s " % (time.time() - start_time) + "seconds.")

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
