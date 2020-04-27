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


def main():
    print(initialPopulation())


if __name__ == "__main__":
    main()





