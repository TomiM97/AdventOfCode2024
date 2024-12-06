import os
import math

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D5_input.txt')
    rules = []
    updates = []
    with open(file_path, 'r') as f:
        for i in f:
            if "|" in i:
                rules.append(list(map(int, i.split("|"))))
            elif "," in i:
                updates.append(list(map(int, i.split(","))))
            else:
                continue
    return rules, updates

def calculateMiddleNumbers(correctUpdate):
    midNumber = correctUpdate[math.floor(len(correctUpdate)/2)]
    return midNumber

def findAllIndexes(pagesToUpdate, search):
    indexes = []
    for index, item in enumerate(pagesToUpdate):
        if item == search:
            indexes.append(index)
    return indexes

def checkCorrectness(rules, updates):
    correctResult = 0
    correctedResult = 0
    for pagesToUpdate in updates:
        correct = True
        for rule in rules:
            if rule[0] in pagesToUpdate and rule[1] in pagesToUpdate:
                beforeRule = findAllIndexes(pagesToUpdate, rule[0])
                afterRule = findAllIndexes(pagesToUpdate, rule[1])
                for i in beforeRule:
                    for j in afterRule:
                        if i > j:
                            correct = False
        if correct:
            correctResult = correctResult + calculateMiddleNumbers(pagesToUpdate)
        else:
            correctedUpdates = correctionCamp(pagesToUpdate, rules)
            correctedResult = correctedResult + calculateMiddleNumbers(correctedUpdates)

    return correctResult, correctedResult

def correctionCamp(faultyUpdates, rules):
    bruteforceCounter = 0
    while bruteforceCounter < 10000: # Brute force ftw
        for rule in rules:     
            correct = False
            while correct == False:
                if rule[0] in faultyUpdates and rule[1] in faultyUpdates:
                        beforeRule = findAllIndexes(faultyUpdates, rule[0])
                        afterRule = findAllIndexes(faultyUpdates, rule[1])
                        for indexB, i in enumerate(beforeRule):
                            for indexA, j in enumerate(afterRule):
                                if i < j:
                                    correct = True
                                else:
                                    faultyUpdates[i], faultyUpdates[j] = faultyUpdates[j], faultyUpdates[i]
                                    beforeRule[indexB] = j
                                    afterRule[indexA] = i
                                    #print(rule)
                                    #print(faultyUpdates)
                else:
                    correct = True
            bruteforceCounter += 1
    correctedUpdates = faultyUpdates                              
    return correctedUpdates

def main():
    rules, updates = readInput()
    correctResult, correctedResult = checkCorrectness(rules, updates)
    print(correctResult)
    print(correctedResult)
    return None


main()
#eof