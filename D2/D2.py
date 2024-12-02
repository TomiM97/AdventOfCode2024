import os

def readInput():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'D2_input.txt')
    masterlist = []
    with open(file_path, 'r') as f:
        for i in f:
            masterlist.append(list(map(int, i.split())))
    return masterlist

def safetyCheck(list):
    result = True
    increasing = True
    #print(list)
    if list[0] > list[1]:
        increasing = False
    for index, item in enumerate(list):
        if index == 0: # Just skipping the first loop
            previtem = item
            continue
        if previtem == item: # number stays the same
            result = False
            print(f"same number {previtem} {item}")
            break
        if increasing == True:
            if previtem > item: # Check if it increases still
                result = False
                print(f"changes to decreasing {list}")
                break
            elif item - previtem > 3: # Check that it doesn't increase too much
                result = False
                print(f"increases too much {previtem - item}")
                break
        if increasing == False:
            if previtem < item: # Check if it decreases still
                result = False
                print(f"changes to increasing {list}")
                break
            elif previtem - item > 3: # Check that it doesn't decrease too much
                result = False
                print(f"decreases too much {previtem - item}")
                break  
        previtem = item     
    return result

def dampenedSafetyCheck(list):
    result = False
    for index, item in enumerate(list):
        if index == 0:
            dampedList = list[index+1:]
        elif index < len(list):
            dampedList = list[:index] + list[index+1:]
        else:
            dampedList = list[:index]
        #print(dampedList)
        if safetyCheck(dampedList) == True:
            result = True
    return result

def analysis(masterlist):
    result = 0
    for list in masterlist:
        if safetyCheck(list) == True:
            result += 1
        elif dampenedSafetyCheck(list) == True:
            result += 1

    return result

def main():
    masterlist = readInput()
    result = analysis(masterlist)
    print(result)
    return None


main()
#eof