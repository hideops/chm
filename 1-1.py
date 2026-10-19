def read_file(file = "input.txt"):
    with open(file, 'r', encoding="utf-8") as f:
        lines = []
        for i in f:
            if i.strip():
                lines.append(i.strip())
    n = int(lines[0])
    matrix = []
    for i in range(1, n + 1):
        matrix.append(list(map(float, lines[i].split())))
    A = []
    b = []
    for i in range(n):
        A.append(matrix[i][:-1])
        b.append(matrix[i][-1])
    return A, b

def multiplicate(A, B):
    rowA = len(A)
    rowB = len(B)
    colA = len(A[0])
    colB = len(B[0])
    C = []
    for i in range(rowA):
        C.append([0] * colB)
    for i in range(rowA):
        for j in range(colB):
            for z in range(colA):
                C[i][j] += A[i][z] * B[z][j]
    return C

def identity(n):
    E = []
    for i in range(n):
        E.append([0] * n)
    for i in range(n):
        for j in range(n):
            if i == j:
                E[i][j] = 1
            else:
                E[i][j] = 0
    return E
def lu(A):
    swap = 0
    n = len(A)
    L = identity(n)
    colA = len(A[0])
    P = identity(n)
    U = A.copy().tolist()
    for i in range(n):
        mx = i
        for j in range(i + 1, n):
            if A[i][j] > mx:
                mx = A[i][j]
        if mx != i:
            P[i], P[mx] = P[mx], P[i]
            U[i], U[mx] = U[mx], U[i]
            swap += 1
            for k in range(i):
                L[i][k], L[mx][k] = L[mx][k], L[i][k]
        for j in range(i + 1, n):
            main = U[j][i] / U[i][i]
            L[j][i] = main
            for k in range(i, n):
                U[j][k] = U[j][k] - main * U[i][k]
    return L, U, P, swap

def test_lu(L, U, P, A):
    LU = multiplicate(L, U)
    PA = multiplicate(P, A)
    if LU == PA:
        return "проверка верная"
    else:
        return "проверка не прошла"

def LB_solution(L, b):
    n = len(L)
    y = [0] * len(L)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= y[j] * L[i][j]
        y[i] /= L[i][i]
    return y

def UY_solution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def vec_multiplication(A, b):
    rows = len(A)
    cols = len(A[0])
    result = [0] * rows
    for i in range(rows):
        for j in range(cols):
            result[i] = result[i] + A[i][j] * b[j]
    return result

def solve_system(L, U, P, b):
    Pb = vec_multiplication(P, b)
    y = LB_solution(L, Pb)
    x = UY_solution(U, y)
    return x

def determinant(U, swaping):
    n = len(U)
    det = 1
    for i in range(n):
        det = det * U[i][i]
    if swaping % 2 != 0:
        det = -det
    return det

def inverse_matrix(L, U, P):
    n = len(L)
    inverse = [[0] * n for i in range(n)]
    for i in range(n):
        e = [0] * n
        e[i] = 1
        x = solve_system(L, U, P, e)
        for j in range(n):
            inverse[j][i] = x[j]
    return inverse

def check_inverse(A, inverse):
    return multiplicate(A, inverse)

print(identity(5))
