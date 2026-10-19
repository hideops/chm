import math
from tt1 import multiplicate
eps = 0.000001
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
    for i in range(n):
        A.append(matrix[i][:-1])
    return A

def jacobi(A, eps):
    n = len(A)
    V = []
    for i in range(n):
        V.append([0] * n)
    for i in range(n):
        for j in range(n):
            if i == j:
                V[i][j] = 1
    mx = eps + 1
    while (mx > eps):
        for i in range(n):
            for j in range(i + 1, n):
                if (A[i][j]) > mx:
                    mx = A[i][j]
                    p = i
                    q = j
        if mx <= eps:
            break
        app = A[p][p]
        aqq = A[q][q]
        apq = A[p][q]
        phi = 0.5 * math.atan(2 * apq / (app - aqq))
        c = math.cos(phi)
        s = math.sin(phi)
        A[p][p] = c * c * app + 2 * c * s * apq + s * s * aqq
        A[q][q] = s * s * app - 2 * c * s * apq + c * c * aqq
        A[p][q] = 0
        A[q][p] = 0
        for k in range(n):
            if k != p and k != q:
                apk = A[p][k]
                aqk = A[q][k]
                A[p][k] = c * apk + s * aqk
                A[k][p] = A[p][k]
                A[q][k] = -s * apk + c * aqk
                A[k][q] = A[q][k]
        for k in range(n):
            vkp = V[k][p]
            vkq = V[k][q]
            V[k][p] = c * vkp + s * vkq
            V[k][q] = -s * vkp + c * vkq

    sz = []
    for i in range(n):
        sz.append(A[i][i])
    return sz, V

def make_l(sz):
    n = len(sz)
    L = []
    for i in range(n):
        L.append([0] * n)
    for i in range(n):
        L[i][i] = sz[i]
    return L

def check(A, V, L, eps):
    AV = multiplicate(A, V)
    VL = multiplicate(V, L)
    max_diff = 0
    for i in range(len(A)):
        for j in range(len(A)):
            diff = abs(AV[i][j] - VL[i][j])
            if diff > max_diff:
                max_diff = diff
    print("A * V:")
    for i in range(len(AV)):
        print(AV[i])
    print("V * L:")
    for i in range(len(VL)):
        print(VL[i])
    print("Максимальная разница:")
    print(max_diff)
    if max_diff < eps:
        print("Проверка пройдена")
    else:
        print("Проверка не пройдена")
