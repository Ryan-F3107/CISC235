'''
Name: Ryan Fernandes
Cisc 235, Assignment 1.2
'''
import random #to use the random generator
import timeit #to use the timeit function

def linearSearch(array,keyVal):
    for i in range(0,len(array)):
        if array[i] == keyVal:
            return True
    return False

def algorithmA(array, targetArray): #function iterates through the target array and searches with the supplied array.
    for i in targetArray:
        linearSearch(array,i)

def mergeSort(array):
    i = j = k = 0
    if len(array) >1: #check if array is not empty
        middle = len(array)//2  #finding the middle of array
        #divide the array
        left = array[:middle]
        right = array[middle:]
        mergeSort(left)
        mergeSort(right)
        while i < len(left) and j < len(right):
            if left[i] < right [j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[i]
                j+=1
            k+=1
         # final check if any code was left out
        while j<len(right):
            array[i] = right[j]
            i+=1
            j+=1

        while k<len(left):
            array[i] = left[k]
            i+=1
            k+=1

def binSearch(array, target, lowIndex = 0, highIndex = None):
    if highIndex == None:
        highIndex = len(array)-1
    if lowIndex > highIndex:
        return False
    else:
        midIndex = (lowIndex + highIndex) //2
        if target == array[midIndex]:
            return True
        elif target < array[midIndex]:
            return binSearch(array,target,lowIndex,midIndex-1)
        else:
            return binSearch(array,target,midIndex+1,highIndex)

#Function runs Merge Sort function & Binary Search function
def algorithmB(array, targetArray):
    mergeSort(array)
    for i in targetArray:
        binSearch(array, i)

def createList(n):
    array = [] #empty list
    for i in range(0,n):
        nextInput = (random.randint(1,n+1)//2)*2    #creates a random number that is even
        array.append(nextInput) #adds the random number into the generated array
    return array

def targetList(k, array):
    targetArray = [] #empty list
    firstHalf = k//2
    secondHalf = k-firstHalf
    for i in range(0,firstHalf):
        nextInput = array[random.randint(0,len(array)-1)]   #obtain a random number from the main list to be appended into the targetArray
        targetArray.append(nextInput)
    for i in range(0,secondHalf):   #appends random odd number into half of the target array.
        nextInput = ((random.randint(1,len(array)+1)//2)*2)+1 #generates random ODD numbers to be appended into the target array.
        targetArray.append(nextInput)
    return targetArray

def main():
    global k, n # k and n are global variables
    setupA = '''from __main__ import algorithmA, createList, targetList, k, n
array = createList(n)
targetArray = targetList(k, array)
'''
    setupB = '''from __main__ import algorithmB, createList, targetList, k, n
array = createList(n)
targetArray = targetList(k, array)
'''
    stmtA = '''algorithmA(array, targetArray)
'''
    stmtB = '''algorithmB(array, targetArray)
'''

    i = 1000
    n = 1000
    print("N = 1000")
    print("")
    print("%-5s%-25s%-25s" % ('k', 'Algorithm A Time (ms)', 'Algorithm B Time (ms)'))
    print("--------------------------------------------------")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt= stmtA, setup = setupA, number = i)) * 1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))* 1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 2000
    print("N = 2000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 5000
    print("N = 5000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 10000
    print("N = 10000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))


main()
