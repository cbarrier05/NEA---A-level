

from curses.ascii import SO


class hashTable:
    def __init__(self, size: int):
        self.table = []
        self.size = size

        for i in range(0, self.size):
            self.table.append([" ", " "])


    def hashFunction(self, key):
        # Using a folding method
        key = str(key)
        sumOfChar = 0
        for i in range(0, len(key)):
            sumOfChar += ord(key[i])
        index = sumOfChar % self.size #+ sumOfChar // self.size
        #index = index % self.size
        return index


    def isFull(self):
        if [" ", " "] in self.table:
            return False
        else:
            return True


    def insertData(self, key, inputData):
        inTable, inTableIndex = self.findKey(key, False)
        index = self.hashFunction(key)
        if inTable:
            self.table[inTableIndex].append(inputData)
        elif self.isFull() and not(inTable):
            pass
        else:
            inserted = False
            firstIndex = index
            while inserted == False:
                if self.table[index][0] == " ":
                    self.table[index] = [key, inputData]
                    inserted = True
                elif self.size == (index + 1):
                    index = 0
                else:
                    index += 1


    def findKey(self, key, needData):
        index = self.hashFunction(key)
        firstIndex = index
        found = False
        inTable = False
        while not(found):
            if self.table[index][0] == key:
                data = self.table[index]
                found = True
                inTable = True
            elif self.table[index][0] == " " or index == (firstIndex - 1) or (firstIndex == 0 and index == (self.size - 1)):
                data = "Not in Table"
                found = True
            elif self.size == (index  + 1):
                index = 0
            else:
                index += 1
        if inTable == False:
            index = "Not in Table"
        if needData == True:
            return inTable, data, index
        elif needData == False:
            return inTable, index


    def deleteKey(self, key):
        inTable, index = self.findKey(key, False)
        if index == "Not in Table":
            pass
        else:
            self.table[index] = [" ", " "]


def mergeSort(original):
    global mergeSplit
    mergeSplit = []
    #global mergeOriginalLength
    #mergeOriginalLength = len(original)
    Split(original)
    print(mergeSplit)

def Split(start):
    halfLength = round(len(start) / 2)
    new1, new2 = [], []
    for i in range(0, halfLength):
        new1.append(start.pop(0))
    for i in start:
        new2.append(i)
    if len(new1) == 1:
        mergeSplit.append(new1)
    else:
        Split(new1) 
    if len(new2) == 1:
        mergeSplit.append(new2)
    else:
        Split(new2)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mergeSort(array)
