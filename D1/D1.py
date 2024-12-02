import os

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D1_input.txt')
    list1 = []
    list2 = []
    with open(file_path, 'r') as f:
        for i in f:
            temp = i.split()
            list1.append(int(temp[0]))
            list2.append(int(temp[1]))
    return list1, list2

def sortLists(list1, list2):
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    return list1_sorted, list2_sorted

def calculateDistances(list1_sorted, list2_sorted):
    distance = 0
    for i, j in enumerate(list1_sorted):
        distance = distance + abs(j - list2_sorted[i])
    return distance

def calculateSimilarity(list1_sorted, list2_sorted):
    similarity = 0
    for i, j in enumerate(list1_sorted):
        #print(i, list1_sorted.count(j))
        #print(i, list2_sorted.count(j))
        similarity = similarity + j * list2_sorted.count(j)
    return similarity


def main():
    list1, list2 = readInput()
    list1_sorted, list2_sorted = sortLists(list1, list2)
    #print(list1_sorted)
    #print(list2_sorted)
    distance = calculateDistances(list1_sorted, list2_sorted)
    similarity = calculateSimilarity(list1_sorted, list2_sorted)
    print(f"distance is {distance}")
    print(f"similarity is {similarity}")
    return None


main()
#eof