

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
                if self.table[index][0] == " " or self.table[index][0] == "DELETED":
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
            self.table[index] = ["DELETED", "DELETED"]


def mergeSort(original):
    global mergeSplit
    mergeSplit = []
    global mergeResult
    mergeResult = []
    mergeSortSplit(original)
    mergeSortCombine(mergeSplit)
    return mergeResult[0]

def mergeSortSplit(start):
    halfLength = round(len(start) / 2)
    new1, new2 = [], []
    for i in range(0, halfLength):
        new1.append(start.pop(0))
    for i in start:
        new2.append(i)
    if len(new1) == 1:
        mergeSplit.append(new1)
    else:
        mergeSortSplit(new1) 
    if len(new2) == 1:
        mergeSplit.append(new2)
    else:
        mergeSortSplit(new2)

def mergeSortCombine(mergeMiddle):
    merging = []
    if len(mergeMiddle) % 2 == 0:
        halfLength = len(mergeMiddle) // 2
    else:
        halfLength = (len(mergeMiddle) // 2) + 1
    for i in range(0, halfLength):
        split1 = mergeMiddle[2 * i]
        try:
            split2 = mergeMiddle[(2 * i) + 1]
        except:
            split2 = []
        combine = []
        while (len(split1) + len(split2)) != 0:
            if len(split1) == 0:
                combine.append(split2[0])
                split2.pop(0)
            elif len(split2) == 0:
                combine.append(split1[0])
                split1.pop(0)
            elif split1[0] >= split2[0]:
                combine.append(split1[0])
                split1.pop(0)
            elif split2[0] > split1[0]:
                combine.append(split2[0])
                split2.pop(0)
        merging.append(combine)
    if len(merging) == 1:
        mergeResult.append(merging[0])
    else:
        mergeSortCombine(merging)
