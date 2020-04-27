from random import randrange

def initialPopulation():
    pop = []
    size = 200
    for i in range(size):
        chrome = []

        for i in range(8):
            chrome.append(randrange(8))

        pop.append(chrome);

    return pop

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

def main():
    grades = []
    for l in initialPopulation():
        grades.append(fitnessFunction(l))


    while (grades.count(49)):





if __name__ == "__main__":
    main()





