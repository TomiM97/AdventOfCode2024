import os
import re

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D3_input.txt')
    multiplications = []
    with open(file_path, 'r') as f:
        txt = "".join(f.readlines())
        multiplications = re.findall("mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", txt)
    return multiplications


def calculate(multiplications):
    do = True
    result = 0
    for i in multiplications:
        #print(i)
        if i == "do()":
            do = True
            continue
        if i == "don't()":
            do = False
            continue
        if do:
            digits = list(map(int, re.findall("[0-9]+", i)))
            result = result + digits[0] * digits[1]
    return result

def main():
    multiplications = readInput()
    result = calculate(multiplications)
    print(result)
    return None


main()
#eof