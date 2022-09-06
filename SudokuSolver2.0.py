from copy import deepcopy
import time

startTime = time.time()


############# FUNCTIONS #####################
def getBoard(filename):
    ''' Opens the sudoku file and puts the contents into a 2D array
        0 means the space is not solved for yet '''
    tempBoard = []
    IFS = open(filename, "r")
    for line in IFS:
        line = line.rstrip()    # Removes anything after last number
        if line != '':         # Appends line to board if there are numbers to append
            tempBoard.append(line.split(' '))
    return tempBoard

def printBoard():
    '''Prints the current board''' 
    
    rowCounter = 0
    
    print()
    
    for row in board:
        rowCounter += 1
        columnCounter = 0
        
        for column in row:
            columnCounter += 1
            
            print(' '+column, end = '')
            
            if columnCounter % 3 == 0 and columnCounter != 9:
                print(' |', end = '')
                
        print()
        if rowCounter % 3 == 0 and rowCounter != 9:
            print(' '+'-'*21)
        

def isValid(row,column,value = None):
    ''' Checks to see if value is a valid solution for the cell in row, column '''
    
    if value == None:
        value = board[row][column]
    
    if value == '0': return False
    
    if value in board[row]: return False
    
    for i in range(9):
        if value == board[i][column]: return False
        
    groupValues = []
    
    startRow = (row // 3) * 3
    startCol = (column // 3) * 3
    
    for i in range(3):
        groupValues.append(board[startRow+i][startCol])
        groupValues.append(board[startRow+i][startCol+1])
        groupValues.append(board[startRow+i][startCol+2])
        
    if value in groupValues:
        return False
    
    board[row][column] = value
    
    return True


def getLastEmptyCellOnBoard():
    ''' Gets the last empty cell on the board '''
    
    for row in range (8,-1,-1):
        for col in range (8,-1,-1):
            if board[row][col] == '0':
                return row,col
            
            
def getPreviousEmptyCell(row,column):
    ''' Gets the previous last empty cell '''
    
    board[row][column] = '0'
    
    for col in range (column - 1, -1, -1):
        if initialBoard[row][col] == '0': return row, col
        
    for row in range (row - 1, -1, -1):
        for col in range (8, -1, -1):
            if initialBoard[row][col] == '0': return row, col
            

def getNextEmptyCell(row,column):
    ''' Gets the next cell to be solved '''
    
    for col in range (column, 9):
        if board[row][col] == '0': return row, col
        
    for row in range (row + 1, 9):
        for col in range (9):
            if board[row][col] == '0': return row, col

########### MAIN ###############
initialBoard = getBoard('sudokuInput.txt')

board = deepcopy(initialBoard)

printBoard()

lastCell = getLastEmptyCellOnBoard()

currentCell = getNextEmptyCell(0,0)

while True:
    if isValid(lastCell[0],lastCell[1]):
        break
    
    i = int(board[currentCell[0]][currentCell[1]])
    
    while i < 10:
        
        if isValid(currentCell[0],currentCell[1],str(i)):
            
            if currentCell == lastCell:
                break
            
            currentCell = getNextEmptyCell(currentCell[0],currentCell[1])
            
            i = 1
            
        else:
            i += 1  
            
    if currentCell == lastCell:
        break
    
    currentCell = getPreviousEmptyCell(currentCell[0], currentCell[1])
    
printBoard()

finalTime = time.time()

print('Execution time:',finalTime - startTime)
    