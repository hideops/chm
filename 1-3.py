from tt1 import read_file, lu, solve_system
eps = 0.000001
error = eps + 1
def simple(A, b, eps):
    n = len(A)
    x = [0] * n
    x_1 = x.copy()
    iter = 0
    while error > eps:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += A[i][j] * x_1[j]
            x[i] = (b[i] - sum) / A[i][i]
        error = 0
        for i in range(n):
            if abs(x[i] - x_1[i]) > error:
                error = abs(x[i] - x_1[i])
        iter += 1
    return x, iter

def zendel(A, b, eps):
    n = len(A)
    x = [0] * n
    error = eps + 1
    iter = 0
    while error > eps:
        x_1 = x.copy()
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]
        error = 0
        for i in range(n):
            if abs(x[i] - x_1[i]) > error:
                error = abs(x[i] - x_1[i])
        iter += 1
    return x, iter


