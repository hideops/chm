def read_file(file = "input12.txt"):
    with open(file, 'r', encoding="utf-8") as f:
        lines = []
        for i in f:
            if i.strip():
                lines.append(i.strip())
        b = list(map(int, lines[0].split()))
        c = list(map(int, lines[1].split()))
        a = list(map(int, lines[2].split()))
        d = list(map(int, lines[3].split()))
    return b, c, a, d

def race(d, b, c, a):
    n = len(b)
    alpha = [0] * n
    beta = [0] * n
    alpha[0] = -c[0] / b[0]
    beta[0] = d[0] / b[0]
    for i in range(1, n):
        alpha[i] = -c[i] / (b[i] + a[i] * alpha[i - 1])
        beta[i] = (d[i] - a[i] * beta[i - 1]) / (b[i] + a[i] * alpha[i - 1])
    x = [0] * n
    x[n - 1] = beta[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    return alpha, beta, x




