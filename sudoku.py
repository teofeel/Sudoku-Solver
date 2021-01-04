import numpy as np

grid = [[0,7,0,0,0,5,0,0,0],
        [0,0,4,0,0,0,8,0,0],
        [0,5,0,0,7,0,0,2,1],
        [9,0,1,0,0,2,0,0,0],
        [0,0,0,4,3,6,0,0,0],
        [0,0,0,9,0,0,6,0,5],
        [6,2,0,0,9,0,0,7,0],
        [0,0,3,0,0,0,1,0,0],
        [0,0,0,7,0,0,0,6,0]]

def set_grid():
    global grid
    for i in range(9):
        for j in range(9):
            n = int(input("Set "+ str(i) + ", " + str(j) + " "))
            grid[i][j] = n
    return


def possible_num(x,y,n):
    global grid
    for i in range(0,9):
        if grid[x][i]==n:
            return False

    for i in range(0,9):
        if grid[i][y]==n:
            return False

    x1 = (x//3)*3
    y1 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x1+i][y1+j] == n:
                return False 

    return True
 
def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if possible_num(x,y,n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
                    
    print(np.matrix(grid))                 

set_grid()
solve()

    
                    