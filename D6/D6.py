import os

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D6_input.txt')
    wholeLab = []
    row = []
    with open(file_path, 'r') as f:
        for i in f:
            for j in i:
                if j == "\n":
                    break
                row.append(j)
            wholeLab.append(row)
            row = []
    return wholeLab

def moveForward(lab, position, orientation):
    if orientation == "^":
        jne
    return lab, position

def checkCollision(lab, position, orientation):
    if orientation == "^":
        if 

def findGuard(lab):
    orientation = "^" # always this so no worries
    for y, row in enumerate(lab):
        for x, item in enumerate(row):
            if item == "^":
                position = [x, y]
                return position, orientation
    return None

def main():
    lab = readInput()
    position, orientation = findGuard(lab)
    print(position)
    return None


main()
#eof