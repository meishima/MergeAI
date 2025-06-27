import random

ROW, COLUMN = (5, 5)
array = [[0 for _ in range(COLUMN)] for _ in range(ROW)] 

def ShowBoard(arrayName):
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
    ShowBoard(array)
    
def MoveTile(row,column,direction):
    if(array[row][column] != 0):
        match direction: # "array[row][column] = 0" is repeated a lot. should simplify.
            case "left":
                if(column != 0):
                    if(array[row][column-1] == array[row][column]):
                        array[row][column] = 0
                        array[row][column-1] += 1
            case "right":
                if(column != COLUMN - 1): # -1 Added because of 0-index situation 
                    if(array[row][column+1] == array[row][column]):
                        array[row][column] = 0
                        array[row][column+1] += 1
            case "up":
                if(row != 0):
                    if(array[row-1][column] == array[row][column]):
                        array[row][column] = 0
                        array[row-1][column] += 1
            case "down":
                if(row != ROW - 1): # -1 Added because of 0-index situation 
                    if(array[row+1][column] == array[row][column]):
                        array[row][column] = 0
                        array[row+1][column] += 1
    else:
        print("You can't merge a 0 into another 0")
    ShowBoard(array)

def UserController():
    startInput = input("What would you like to do? \n1 = Add Tiles\n2 = Move Tile\n3 = Exit\n")
    match startInput:
        case "1":
            AddTile()
        case "2":
            moveInput_row = int(input("Select the row of the tile that you would like to move:"))
            moveInput_column = int(input("Select the column of the tile that you would like to move:"))
            moveInput_direction = input("Select the direction that you would like to move your tile (Left,Right,Up,Down):").lower()
            MoveTile(moveInput_row,moveInput_column,moveInput_direction)
        case _:
            return 0
    Heuristic(array)
    UserController()
        
def Heuristic(board):
    empty = 0
    highestTile = 0
    for row in range(len(array)):
        for col in range(len(array[row])):
            if(board[row][col] == 0):
                empty += 1
            if(board[row][col] > highestTile):
                highestTile = board[row][col]
    score = empty * 2 + highestTile * 1.5 # Random modifiers, can tweak them later on.
    print("Empty Tiles Left:",empty)
    print("Highest Tile:", highestTile)
    print("Score:",score)
    return score
    
    
ShowBoard(array)
UserController()
# Need Heuristic Function to evaluate the score of the move.
# Need to use expectimax to simulate the board. (explain why expetimax rather than minimax in docs)
