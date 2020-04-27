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