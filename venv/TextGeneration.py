def initialPopulation():
    pop = []
    size = 200
    for i in range(size):
        chrome = []

        for i in range(28):
            chrome.append(randrange(28))

        pop.append(chrome)

    return pop
def fromStrToArr(s):
    arr = []
    for i in range(300):
        if s[i] == '.':
            arr[i] = 26
        elif s[i] == ' ':
            arr[i] = 27
        else:
            arr[i] = s[i] - 'a'
    return arr
def main():
    grades = []
    currGen = initialPopulation()
    for l in currGen:
        grades.append(fitnessFunction(l))
    gen = 1

    createNextGen(currGen, grades)

    while 300 not in grades:
        s = "to be or not to be that is the question. whether tis nobler in the mind to suffer. the slings and arrows of outrageous fortune. or to take arms against a sea of troubles and by opposing end them. to die to sleep. no more. and by a sleep to say we end. the heartache and the thousand natural shocks."
        correctAns = fromStrToArr(s)
        currGen = createNextGen(currGen, grades)
        grades = []
        for l in currGen:
            grades.append(fitnessFunction(l))
        gen = gen + 1
        if gen % 750 == 0:
            currGen = initialPopulation()
        #print(gen)

    index = grades.index(300)