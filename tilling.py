import numpy as np

n = int(input('enter n: '))
x, y = map(int, input('enter forbidden tile position:').split(','))
x-=1
y-=1
matrix = np.zeros((n, n), dtype=int)
matrix[x][y] = -1

count = 1

def position(matrix, low_i, low_j, high_i, high_j):
    for i in range(low_i,high_i+1):
        for j in range(low_j,high_j+1):
            if matrix[i][j]!=0:
                return [i,j]
    return [0,0]
    

def T(matrix, low_i, low_j, high_i, high_j,pos):
    global count
    x=pos[0]
    y=pos[1]
    if high_i - low_i == 1:
        for i in range(low_i, high_i + 1):
            for j in range(low_j, high_j + 1):
                if matrix[i][j] == 0:
                    matrix[i][j] = count
        count += 1
    else:
        mid_i = (high_i - low_i) // 2 + low_i
        mid_j = (high_j - low_j) // 2 + low_j

        if x <= mid_i and y <= mid_j:
            matrix[mid_i + 1][mid_j + 1] = count
            matrix[mid_i][mid_j + 1] = count
            matrix[mid_i + 1][mid_j] = count
            
            
        elif x <= mid_i and y > mid_j:
            matrix[mid_i + 1][mid_j + 1] = count
            matrix[mid_i][mid_j] = count
            matrix[mid_i + 1][mid_j] = count
            
        elif x > mid_i and y <= mid_j:
            matrix[mid_i][mid_j + 1] = count
            matrix[mid_i][mid_j] = count
            matrix[mid_i + 1][mid_j + 1] = count
            
        elif x > mid_i and y > mid_j:
            matrix[mid_i][mid_j] = count
            matrix[mid_i + 1][mid_j] = count
            matrix[mid_i][mid_j + 1] = count
            
            
        count += 1
        T(matrix, low_i, low_j, mid_i, mid_j,pos=position(matrix, low_i, low_j, mid_i, mid_j))
        T(matrix, low_i, mid_j + 1, mid_i, high_j,pos=position(matrix, low_i, mid_j + 1, mid_i, high_j))
        T(matrix, mid_i + 1, low_j, high_i, mid_j,pos=position(matrix, mid_i + 1, low_j, high_i, mid_j))
        T(matrix, mid_i + 1, mid_j + 1, high_i, high_j,pos=position(matrix, mid_i + 1, mid_j + 1, high_i, high_j))

T(matrix, 0, 0, n - 1, n - 1,[x,y])
print(matrix)
print(f'number of total tile:{count-1}')
