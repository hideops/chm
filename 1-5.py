import math
import cmath
import numpy as np
from tt1 import multiplicate
eps = 0.01
max_iteration = 1000

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
    A = matrix
    return A

def transponate(A):
    n = len(A)
    A_t = []
    for i in range(n):
        A_t.append([0] * n)
    for i in range(n):
        for j in range(n):
            A_t[i][j] = A[j][i]
    return A_t

def get_q(A):
    u1 = []
    ln_u1 = 0
    for i in range(len(A)):
        u1.append(A[i][0])
        ln_u1 += u1[i] * u1[i]
    ln_u1 = math.sqrt(ln_u1)
    for i in range(len(A)):
        u1[i] /= ln_u1
    q = []
    for i in range(len(A)):
        q.append([0] * len(A))
    q[0] = (u1)
    q_t = []
    for i in range(len(A)):
        q_t.append([0] * len(A))
    A_t = transponate(A)
    for j in range(1, len(A)):
        sm_proection = [0] * len(A)
        for i in range(j):
            sm = 0
            for k in range(len(A)):
                sm += q[i][k] * A_t[j][k]
            for k in range(len(A)):
                sm_proection[k] += sm * q[i][k]
        q[j] = A_t[j].copy()
        for k in range(len(A)):
            q[j][k] -= sm_proection[k]
        sm = 0
        for i in range(len(q[j])):
            sm = sm + q[j][i]*q[j][i]
        sm = math.sqrt(sm)
        for i in range(len(q[j])):
            q[j][i] = q[j][i] / sm
    return transponate(q)

def get_r(q, A):
    q_t_new = transponate(q)
    r = multiplicate(q_t_new, A)
    return r

def qr(q, r):
    return multiplicate(q,r)

def check_qr(q, r, A):
    QR = qr(q, r)
    for i in range(len(A)):
        for j in range(len(A)):
            if abs(QR[i][j] - A[i][j]) > eps:
                return "проверка qr не верная"
    return "проверка qr верная"

def diagonal_sum(A):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(i):
            result += abs(A[i][j])
    return result

def below_subdiagonal_sum(A):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(i - 1):
            result += abs(A[i][j])
    return result

def is_converged(A):
    n = len(A)
    if below_subdiagonal_sum(A) > eps:
        return False
    for i in range(n - 2):
        if abs(A[i + 1][i]) > eps and abs(A[i + 2][i + 1]) > eps:
            return False
    return True

def get_eigenvalues(A):
    n = len(A)
    values = []
    i = 0
    while i < n:
        if i < n - 1 and abs(A[i + 1][i]) > eps:
            a, b = A[i][i], A[i][i + 1]
            c, d = A[i + 1][i], A[i + 1][i + 1]
            tr = a + d
            det = a * d - b * c
            d2 = tr * tr / 4 - det
            if d2 >= 0:
                disc = math.sqrt(d2)
            else:
                disc = cmath.sqrt(d2)
            values.append(tr / 2 + disc)
            values.append(tr / 2 - disc)
            i += 2
        else:
            values.append(A[i][i])
            i += 1
    return values

def qr_find(A):
    A_prev = [row.copy() for row in A]
    iteration = 0
    while not is_converged(A_prev) and iteration < max_iteration:
        Q = get_q(A_prev)
        R = get_r(Q, A_prev)
        A_new = multiplicate(R, Q)
        A_prev = A_new
        iteration += 1
    if not is_converged(A_prev):
        print("алгоритм не работает")
    for row in A_prev:
        print(row)
    self_value = get_eigenvalues(A_prev)
    return self_value

def complex_example():
    A = [[1.0, -2.0, 1.0],
         [2.0, 1.0, 3.0],
         [0.0, 0.0, 3.0]]
    print("A:")
    for row in A:
        print(row)
    Q = get_q(A)
    R = get_r(Q, A)
    print("Q:")
    for row in Q:
        print(row)
    print("R:")
    for row in R:
        print(row)
    print("Q*R:")
    for row in qr(Q, R):
        print(row)
    print(check_qr(Q, R, A))
    values = qr_find(A)
    print(values)
    np_values = np.linalg.eigvals(np.array(A))
    print(np_values)


def main():
    A = read_file()
    Q = get_q(A)
    R = get_r(Q, A)
    print("A:")
    for row in A:
        print(row)
    print("Q:")
    for row in Q:
        print(row)
    print("R:")
    for row in R:
        print(row)
    print("Q * R:")
    for row in qr(Q, R):
        print(row)
    print(check_qr(Q, R, A))
    eigenvalues = qr_find(A)
    print("сз:")
    print(eigenvalues)
    complex_example()

main()
