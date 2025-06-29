import random
import copy

ROW, COLUMN = (5, 5)
array = [[0 for _ in range(COLUMN)] for _ in range(ROW)] 

def ShowBoard(board):
    for row in board:
        print(row)
    
def AddTile(board):
    filledTiles = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == 0):
                filledTiles.append([row,col])
    if(len(filledTiles) > 0):
        randomTileIndex = random.randint(0,len(filledTiles)-1) # added -1 because of len() is not 0-indexed
        randomTileIndex_row = filledTiles[randomTileIndex][0]
        randomTileIndex_column = filledTiles[randomTileIndex][1]
        board[randomTileIndex_row][randomTileIndex_column] = 1
    else:
        print("Error. Can't add more more tiles to the board.")
    ShowBoard(board)
    
def MoveTile(row,column,direction,board):
    if(board[row][column] != 0):
        match direction: # "board[row][column] = 0" is repeated a lot. should simplify.
            case "left":
                if(column != 0):
                    if(board[row][column-1] == board[row][column]):
                        board[row][column] = 0
                        board[row][column-1] += 1
                        return 1
            case "right":
                if(column != COLUMN - 1): # -1 Added because of 0-index situation 
                    if(board[row][column+1] == board[row][column]):
                        board[row][column] = 0
                        board[row][column+1] += 1
                        return 1
            case "up":
                if(row != 0):
                    if(board[row-1][column] == board[row][column]):
                        board[row][column] = 0
                        board[row-1][column] += 1
                        return 1
            case "down":
                if(row != ROW - 1): # -1 Added because of 0-index situation 
                    if(board[row+1][column] == board[row][column]):
                        board[row][column] = 0
                        board[row+1][column] += 1
                        return 1
    else:
        print("You can't merge a 0 into another 0")
    ShowBoard(board)
    return 0

def UserController():
    startInput = input("What would you like to do? \n1 = Add Tiles\n2 = Move Tile\n3 = Expectimax\n4 = Exit\n")
    match startInput:
        case "1":
            global array
            AddTile(array)
        case "2":
            moveInput_row = int(input("Select the row of the tile that you would like to move:"))
            moveInput_column = int(input("Select the column of the tile that you would like to move:"))
            moveInput_direction = input("Select the direction that you would like to move your tile (Left,Right,Up,Down):").lower()
            MoveTile(moveInput_row,moveInput_column,moveInput_direction,array)
        case "3":
            Repeater(array)
        case _:
            return 0
    Heuristic(array)
    UserController()
        
def Heuristic(board):
    empty = 0
    highestTile = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == 0):
                empty += 1
            if(board[row][col] > highestTile):
                highestTile = board[row][col]
    score = empty * 2 + highestTile * 1.5 # Random modifiers, can tweak them later on.
    print("Empty Tiles Left:",empty)
    print("Highest Tile:", highestTile)
    print("Score:",score)
    return score

def is_game_ended(board):
    # Check for any empty cell
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return False  # Still empty cells -> game not over

    # Check for possible merges horizontally and vertically
    for row in range(len(board)):
        for col in range(len(board[row])):
            # Check right neighbor
            if col < len(board[row]) - 1:
                if board[row][col] == board[row][col + 1]:
                    return False  # Merge possible -> game not over
            # Check down neighbor
            if row < len(board) - 1:
                if board[row][col] == board[row + 1][col]:
                    return False  # Merge possible -> game not over

    # No empty cells and no merges possible
    return True
    
def Expectimax(board,depth):
    if(depth == 0 and is_game_ended(board)): # add "or game over"
        return Heuristic(board), board
    bestBoard = None
    maxEval = float('-inf')
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] != 0 and ( board[row][col] == board[max(row-1,row)][col] or board[row][col] == board[min(row+1,row)][col] or board[row][col] == board[row][max(col,col-1) or board[row][col] == board[row][min(col,col+1)]])):
                for direction in ["up", "down", "left", "right"]:
                    newBoard = copy.deepcopy(board)
                    if MoveTile(row, col, direction, newBoard) == 1:
                        eval, candidateBoard = Expectimax(newBoard, depth - 1)
                        if eval > maxEval:
                            maxEval = eval
                            bestBoard = candidateBoard
    if maxEval == float('-inf'):
        return Heuristic(board), board
    return maxEval, bestBoard

def Repeater(board):
    score, board = Expectimax(board, 3)
    score2, board2 = Expectimax(board, 3)
    if(board == board2):
        AddTile(board)
        Repeater(board)
    else:
        board2 = board
        Repeater(board)
    global array
    array = board
    ShowBoard(array)
    
ShowBoard(array)
UserController()

# CLEAN THE CODE
