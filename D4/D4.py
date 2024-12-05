import os

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D4_input.txt')
    wordMatrix = []
    wordRow = []
    with open(file_path, 'r') as f:
        for i in f:
            for j in i:
                if j == "\n":
                    break
                wordRow.append(j)
            wordMatrix.append(wordRow)
            wordRow = []
    return wordMatrix

def checkXMAS(wordMatrix):
    result = 0
    maxRow = len(wordMatrix) - 1 
    maxColumn = len(wordMatrix[0]) - 1
    for row, list in enumerate(wordMatrix):
        for column, letter in enumerate(list):
            if letter == "X":
                if row + 3 <= maxRow:  # straight down check
                    if wordMatrix[row + 1][column] == "M":
                        if wordMatrix[row + 2][column] == "A":
                            if wordMatrix[row + 3][column] == "S":
                                result += 1
                if row + 3 <= maxRow and column + 3 <= maxColumn: # low right check
                    if wordMatrix[row + 1][column + 1] == "M":
                        if wordMatrix[row + 2][column + 2] == "A":
                            if wordMatrix[row + 3][column + 3] == "S":
                                result += 1
                if column + 3 <= maxColumn: # straight right check
                    if wordMatrix[row][column + 1] == "M":
                        if wordMatrix[row][column + 2] == "A":
                            if wordMatrix[row][column + 3] == "S":
                                result += 1
                if row - 3 >= 0 and column + 3 <= maxColumn: # high right check
                    if wordMatrix[row - 1][column + 1] == "M":
                        if wordMatrix[row - 2][column + 2] == "A":
                            if wordMatrix[row - 3][column + 3] == "S":
                                result += 1
                if row - 3 >= 0: # straight up check
                    if wordMatrix[row - 1][column] == "M":
                        if wordMatrix[row - 2][column] == "A":
                            if wordMatrix[row - 3][column] == "S":
                                result += 1
                if row - 3 >= 0 and column - 3 >= 0: # high left check
                    if wordMatrix[row - 1][column - 1] == "M":
                        if wordMatrix[row - 2][column - 2] == "A":
                            if wordMatrix[row - 3][column - 3] == "S":
                                result += 1
                if column - 3 >= 0:  # straight left check
                    if wordMatrix[row][column - 1] == "M":
                        if wordMatrix[row][column - 2] == "A":
                            if wordMatrix[row][column - 3] == "S":
                                result += 1
                if row + 3 <= maxRow and column - 3 >= 0: # low left check
                    if wordMatrix[row + 1][column - 1] == "M":
                        if wordMatrix[row + 2][column - 2] == "A":
                            if wordMatrix[row + 3][column - 3] == "S":
                                result += 1
    return result

def checkX_MAS(wordMatrix):
    result = 0
    maxRow = len(wordMatrix) - 1 
    maxColumn = len(wordMatrix[0]) - 1
    for row, list in enumerate(wordMatrix):
        for column, letter in enumerate(list):
            if letter == "A":
                if row - 1 >= 0 and row + 1 <= maxRow and column - 1 >= 0 and column + 1 <= maxColumn: # check surroundings
                    if wordMatrix[row - 1][column - 1] == "M" and wordMatrix[row + 1][column + 1] == "S": # \
                        if wordMatrix[row + 1][column - 1] == "M" and wordMatrix[row - 1][column + 1] == "S": # /
                            result += 1
                    if wordMatrix[row - 1][column - 1] == "S" and wordMatrix[row + 1][column + 1] == "M": # \
                        if wordMatrix[row + 1][column - 1] == "M" and wordMatrix[row - 1][column + 1] == "S": # /
                            result += 1
                    if wordMatrix[row - 1][column - 1] == "S" and wordMatrix[row + 1][column + 1] == "M": # \
                        if wordMatrix[row + 1][column - 1] == "S" and wordMatrix[row - 1][column + 1] == "M": # /
                            result += 1
                    if wordMatrix[row - 1][column - 1] == "M" and wordMatrix[row + 1][column + 1] == "S": # \
                        if wordMatrix[row + 1][column - 1] == "S" and wordMatrix[row - 1][column + 1] == "M": # /
                            result += 1
                
    return result

def main():
    wordMatrix = readInput()
    XMASresult = checkXMAS(wordMatrix)
    X_MASresult = checkX_MAS(wordMatrix)
    print(f"part 1: {XMASresult}")
    print(f"part 2: {X_MASresult}")
    return None


main()
#eof