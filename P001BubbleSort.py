#function that will sort a list in ascending order using bubble sort
def bubbleSort (numberList):
    #listLength: length of the list
    listLength = len(numberList)

    for i in range (listLength):
        for j in range (listLength-i-1):
            #Check if the current number if larger than the next number
            if(numberList[j]>numberList[j+1]):
                #Swap the numbers if above condition is true
                temp = numberList[j]
                numberList[j] = numberList[j+1]
                numberList[j+1] = temp

numberList = [3,1,7,2,10,5]
print(numberList)
bubbleSort(numberList = numberList)   
print(numberList)

# Sample input/ output
#[3, 1, 7, 2, 10, 5]
#[1, 2, 3, 5, 7, 10]


         


