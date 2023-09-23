import numpy as np
from tabulate import tabulate

def format_polynomial(coefficients):
    # Определение степени многочлена
    degree = len(coefficients) - 1

    # Создание пустой строки для форматирования
    polynomial_str = ""

    # Перебор коэффициентов, начиная с самой высокой степени
    for i, coeff in enumerate(coefficients):
        # Пропускаем нулевые коэффициенты
        if coeff == 0:
            continue

        # Определение знака перед слагаемым
        if coeff > 0 and i != 0:
            polynomial_str += " + "
        elif coeff < 0:
            polynomial_str += " - "

        # Если коэффициент не равен 1, добавляем его
        if abs(coeff) != 1 or (i == 0 and coeff == -1):
            polynomial_str += str(abs(coeff))

        # Добавляем переменную (x) и степень (если степень не равна нулю)
        if i < degree:
            polynomial_str += "x"

        if i < degree - 1:
            polynomial_str += "^" + str(degree - i)

    return polynomial_str


n = 4
f = np.array([[-2, -8], [-1, -1], [0, 0], [2, 8]])
headers = ["x", "f(x)"]
table = tabulate(f, headers, tablefmt="pretty")
print("Исходные данные:")
print(table)

# создаём матрицу 4x4
d = np.zeros((n, n))
# заполняем матрицу
for i in range(0, n):
    for j in range(n - 1, -1, -1):
        d[i][n - j - 1] = f[i][0] ** j

# Присоединяем новый столбец к матрице
result_matrix = np.column_stack((d, f[:, [1]]))
row_headers = ["x0", "x1", "x2", "x3"]
headers = ["a3*x^3", "a2*x^2", "a1*x", "a0", "f(x)"]
table = tabulate(result_matrix, headers, tablefmt="pretty", showindex=row_headers)
print("Матрица:")
print(table)

# Решаем СЛАУ
ans = np.linalg.solve(d, f[:, [1]])
row_headers = ["a0", "a1", "a2", "a3"]
table = tabulate(ans, tablefmt="pretty", showindex=row_headers)
print("Полученные коэффициенты:")
print(table)

# Интерполяционный многочлен:
coef = [ans[0][0], ans[1][0], ans[2][0], ans[3][0]]
polinomial_str = format_polynomial(coef)
print("Интерполяционный многочлен:")
print(f"P(x) = " + polinomial_str)

# Получаем:
result_matrix = []
for i in range(0, n):
    result_matrix.append([f[i][0], f[i][1]])
    if i != n - 1:
        # Вычисляем значение в промежуточных точках
        x = (f[i][0] + f[i + 1][0]) / 2
        y = ans[0][0] * (x ** 3) + ans[1][0] * (x ** 2) + ans[2][0] * x + ans[3][0]
        result_matrix.append([x, y])

print("Полученные значения в интерполяционном многочлене:")
headers = ["x", "f(x)"]
table = tabulate(result_matrix, headers, tablefmt="pretty")
print(table)