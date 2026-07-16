import numpy as np

x_test = np.array([(-5, 2), (-4, 6), (3, 2), (3, -3), (5, 5), (5, 2), (-1, 3)])
y_test = np.array([1, 1, 1, -1, -1, -1, -1])
w = np.array([-8/3, -2/3, 1])
new_x_test = np.insert(x_test, 0, 1, axis=1)
print(new_x_test)
# здесь продолжайте программу
