import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([[10,50], [20,30], [25,30], [20,60], [15,70], [40,40], [30,45], [20,45], [40,30], [7,35]])
y_train = np.array([-1,1,1,-1,-1,1,1,-1,1,-1])

n_train = len(x_train)      # размер обучающей выборки
w = [0,-1]                  # начальное значение вектора w
a = lambda x: np.sign(x[0] * w[0] + x[1] * w[1])    # решающее правило
N = 50                      # число итераций
L = 0.1                     # шаг изменения веса
e = 0.1                     # небольшая добавка для w0 чтобы был зазор между разделяющей линией и образом

last_error_index = -1       # вспомогательная переменная, индекс последнего ошибочного наблюдения

for n in range(N):
    for i in range(n_train):
        if y_train[i] * a(x_train[i]) < 0: # если ошибка классификации
            w[0] = w[0] + L * y_train[i]   # корректируем вес w0 на шаг
            last_error_index = i

    Q = sum([1 for i in range(n_train) if y_train[i] * a(x_train[i]) < 0])
    if Q == 0:              # кол во ошибок
        break

if last_error_index > -1:
    w[0] = w[0] + e * y_train[last_error_index]

print(w)

# формируем график разделяющей линии

line_x = list(range(max(x_train[:, 0])))
line_y = [w[0] * x for x in line_x]

# точки для классов
x_0 = x_train[y_train == 1]
x_1 = x_train[y_train == -1]

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='green')
plt.plot(line_x, line_y, color='blue')

plt.xlim([0,45])
plt.ylim([0,75])
plt.ylabel("длина")
plt.xlabel("ширина")
plt.grid(True)
plt.show()