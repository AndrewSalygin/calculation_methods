# Интерполяционный многочлен в форме Лагранжа
def L(x, f, n):
    result = 0
    for i in range(0, n):
        up_proizv = 1
        down_proizv = 1
        for j in range(0, n):
            if j != i:
                up_proizv *= x - f[j][0]
        for j in range(0, n):
            if j != i:
                down_proizv *= f[i][0] - f[j][0]
        result += f[i][1] * (up_proizv / down_proizv)
    return result

headers = ["x", "f(x)"]
table = tabulate(f, headers, tablefmt="pretty")
print("Исходные данные:")
print(table)

f = np.array([[-2, -8], [-1, -1], [0, 0], [2, 8], [3, 27]])
n = 5
result = []
for i in range(0, n):
    result.append([f[i][0], f[i][1]])
    if (i != n - 1):
        result.append([(f[i][0] + f[i + 1][0]) / 2, L((f[i][0] + f[i + 1][0]) / 2, f, n)])
        
headers = ["x", "f(x)"]
table = tabulate(result, headers, tablefmt="pretty")
print(table)
