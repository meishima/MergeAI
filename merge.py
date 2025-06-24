import random

rows, cols = (5, 5)
array = [[0 for _ in range(cols)] for _ in range(rows)] 

def showArray(arrayName):
    for row in arrayName:
        print(row)
    
def addTile():
    filledTiles = []
    for row in range(len(array)):
        for col in range(len(array[row])):
            if(array[row][col] == 0):
                filledTiles.append([row,col])
    if(len(filledTiles) > 0):
        randomTileIndex = random.randint(0,len(filledTiles)-1) # added -1 because of len() is not 0-indexed
        randomTileIndex_x = filledTiles[randomTileIndex][0]
        randomTileIndex_y = filledTiles[randomTileIndex][1]
        array[randomTileIndex_x][randomTileIndex_y] = 1
    else:
        print("Error. Can't add more more tiles to the board.")
    showArray(array)

def UserController():
    userInput = input("What would you like to do? \n1 = Add Tiles\n2 = Exit\n")
    if(userInput == "1"):
        addTile()
    elif(userInput == "2"):
        return 0
    UserController()
        
showArray(array)
UserController()

