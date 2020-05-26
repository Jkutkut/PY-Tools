## Prints the sudoku array
def printSudoku(arr):
    print(*["  Y "] + [str(i) + " " for i in range(3)] + ["  "] + [str(3+i) + " " for i in range(3)] + ["  "] + [str(6+i) + " " for i in range(3)], sep = "")
    print(*["X +"] + ["-" for i in range(23)] + ["+"], sep = "")#start

    for i in range(3): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  "]+["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "")#3 by 3 separators

    for i in range(3, 6): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  "]+["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "")#3 by 3 separators

    for i in range(6, 9): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  +"] + ["-" for i in range(23)] + ["+"], sep = "")#end

## Prints the status of the arguments (errors)
def pError(**kwargs):
    print("***ERROR***".center(30))
    print(kwargs)
    print("***END ERROR***".center(30))

## Checks if it is possible to place "value" on the position (x, y) or data[x][y].
def isPossibleVal(x, y, value, arr):
    for i in range(9):
        if data[x][i] == value:
            return False
        if data[i][y] == value:
            return False

    xIndex = (x // 3) * 3
    yIndex = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if data[xIndex + i][yIndex + j] == value:
                return False
    return True

# Given the sudoku as data and an array to store all the solutions 
def sudokuSolution(data, solutions):
    for x in range(9):
        for y in range(9):
            if data[x][y] == 0:
                for val in range(1,10):
                    valid = True
                    for i in range(9):
                        xIndex = (x // 3) * 3
                        yIndex = (y // 3) * 3
                        if data[x][i] == val or data[i][y] == val or data[xIndex + (i // 3)][yIndex + (i % 3)] == val:
                            valid = False
                            break
                    if valid:
                        data[x][y] = val
                        sudokuSolution(data, solutions)
                        data[x][y] = 0 #if here, the path wasn't good => undo move
                return
    ## if here, solution founded
    solutions.append([[ele for ele in row] for row in data])

# Check if the given sudoku is a valid solution
def checkSol(arr):
    for i in range(0, 9, 3):#3 by 3:
        for j in range(0, 9, 3):
            suma = 0
            ele = []
            for k in range(3):
                for l in range(3):
                    suma = suma + arr[k + i][l + j]
                    ele = ele + [arr[k + i][l + j]]
            if(suma != 45):
                # pError(zone="3b3", i=i, j=j, k=k, l=l, ele=ele)
                return False
    for l in range(9):#lines:
        solC = 0
        for i in range(9):
            solC = solC + arr[i][l]
        if sum(arr[l]) != 45 or solC != 45:
            # pError(zone="lines", i=i, l=l)
            return False
    return True

#sort matrix by their value
def sortedMatrix(m, row):
    return sorted(m, key=lambda row: int(row[k]))