import random


def generateMaze(size):
    mazeWidth = (2 * size) + 1
    usedTiles = []
    path = []
    currentTile = [1, 1, "path"]
    currentPath = [1, 1]
    selected = True
    while selected == True:
        if not(currentPath in path):
            path.append(currentPath)
        possible = ["left", "right", "up", "down"]
        if [currentPath[0], currentPath[1] - 2] in path:
            possible.remove("up")
        if [currentPath[0], currentPath[1] + 2] in path:
            possible.remove("down")
        if [currentPath[0] - 2, currentPath[1]] in path:
            possible.remove("left")
        if [currentPath[0] + 2, currentPath[1]] in path:
            possible.remove("right")
        if currentPath[0] <= 2:
            if "left" in possible:
                possible.remove("left")
        if currentPath[0] >= (mazeWidth - 3):
            if "right" in possible:
                possible.remove("right")
        if currentPath[1] <= 2:
            if "up" in possible:
                possible.remove("up")
        if currentPath[1] >= (mazeWidth - 3):
            if "down" in possible:
                possible.remove("down")
        if len(possible) == 0:
            count = 0
            for i in usedTiles:
                if not(i[0] == currentTile[0]) or not(i[1] == currentTile[1]):
                    count += 1
            if count == len(usedTiles):
                usedTiles.append(currentTile)
            currentIndex = path.index([currentPath[0], currentPath[1]])
            if currentIndex == 0:
                selected = False
            else:
                currentPath = path[currentIndex - 1]
                for i in usedTiles:
                    if i[0] == currentPath[0] and i[1] == currentPath[1]:
                        currentTile = usedTiles[usedTiles.index(i)]
        else:
            next = random.randint(0,(len(possible) - 1))
            movement = possible[next]
            if movement == "left":
                newPath = [currentPath[0] - 2, currentPath[1]]
                currentTile.append("left")
            elif movement == "right":
                newPath = [currentPath[0] + 2, currentPath[1]]
                currentTile.append("right")
            elif movement == "up":
                newPath = [currentPath[0], currentPath[1] - 2]
                currentTile.append("up")
            elif movement == "down":
                newPath = [currentPath[0], currentPath[1] + 2]
                currentTile.append("down")
            if [currentTile[0], currentTile[1]] in path and selected == True:
                count = 0
                for i in usedTiles:
                    if i[0] == currentTile[0] and i[1] == currentTile[1]:
                        usedTiles[usedTiles.index(i)] = currentTile
                    else:
                        count += 1
                if count == len(usedTiles):
                    usedTiles.append(currentTile)
            currentPath = newPath
            currentTile = [currentPath[0], currentPath[1], "path"]
    for i in usedTiles:
        if "left" in i:
            usedTiles.append([i[0] - 1, i[1], "path"])
            path.append([i[0] - 1, i[1]])
        if "right" in i:
            usedTiles.append([i[0] + 1, i[1], "path"])
            path.append([i[0] + 1, i[1]])
        if "up" in i:
            usedTiles.append([i[0], i[1] - 1, "path"])
            path.append([i[0], i[1] - 1])
        if "down" in i:
            usedTiles.append([i[0], i[1] + 1, "path"])
            path.append([i[0], i[1] + 1])
    for xcoord in range(0, mazeWidth):
        for ycoord in range(0, mazeWidth):
            if not([xcoord, ycoord] in path):
                usedTiles.append([xcoord, ycoord, "wall"])
    return usedTiles

mazeSize = 5
mazeArray = generateMaze(mazeSize)
mazeSorted = sorted(mazeArray)
for i in range(0,(2 * mazeSize) + 1):
    printing = []
    for x in mazeSorted:
        if i == x[1]:
            printing.append(x[2])
    print(printing)
#print(mazeSorted)
