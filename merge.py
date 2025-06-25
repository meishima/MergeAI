import random

ROWS, COLUMN = (5, 5)
array = [[0 for _ in range(COLUMN)] for _ in range(ROWS)] 

def showArray(arrayName):
    for row in arrayName:
        print(row)
    
def AddTile():
    filledTiles = []
    for row in range(len(array)):
        for col in range(len(array[row])):
            if(array[row][col] == 0):
                filledTiles.append([row,col])
    if(len(filledTiles) > 0):
        randomTileIndex = random.randint(0,len(filledTiles)-1) # added -1 because of len() is not 0-indexed
        randomTileIndex_row = filledTiles[randomTileIndex][0]
        randomTileIndex_column = filledTiles[randomTileIndex][1]
        array[randomTileIndex_row][randomTileIndex_column] = 1
    else:
        print("Error. Can't add more more tiles to the board.")
    showArray(array)
    
def MoveTile(row,column,direction):
    match direction:
        case "Left":
            if(column != 0):
                if(array[row][column-1] == array[row][column]):
                    array[row][column] = 0
                    array[row][column-1] =+ 1
        case "Right":
            if(column != COLUMN): #FIX THIS TOMORROW NOT COMPLETED
                if(array[row][column+1] == array[row][column]):
                    array[row][column] = 0
                    array[row][column-1] =+ 1
    showArray()

def UserController():
    startInput = input("What would you like to do? \n1 = Add Tiles\n2 = Move Tile\n3 = Exit\n")
    match startInput:
        case "1":
            AddTile()
        case "2":
            moveInput_row = int(input("Select the row of the tile that you would like to move:"))
            moveInput_column = int(input("Select the column of the tile that you would like to move:"))
            moveInput_direction = input("Select the direction that you would like to move your tile (Left,Right,Up,Down):")
            MoveTile(moveInput_row,moveInput_column,moveInput_direction)
        case _:
            return 0
    UserController()
        
showArray(array)
UserController()

