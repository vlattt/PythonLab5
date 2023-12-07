import matplotlib.pyplot as plt
import random
import numpy as np

x = list(range(0, 24))
y = [random.randint(17, 22) for i in range(24)]

plt.xlabel("Время")
plt.ylabel("Температура")
plt.title("Прогноз погоды")
plt.plot(x, y)
plt.show()



x = ["Курица", "Свинина", "Говядина", "Баранина", "Индейка"]
y = [random.randint(600, 1000) for i in range(5)]
plt.bar(x, y)
plt.xlabel("Товар")
plt.ylabel("Количество продаж")
plt.title("Мясной отдел")
plt.show()



x = list(range(175, 200))
y = []
for i in x:
    y.append(i**2 * 24 / 10000)


plt.xlabel("Рост")
plt.ylabel("Вес")
plt.title("Пропорции мужчины в пределах нормы")
plt.plot(x, y, marker='o', markersize=7)
plt.show()

data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Оценка')
plt.ylabel('Количество учеников')
plt.title('Таблица успеваемости')
plt.show()


x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
[X, Y] = np.meshgrid(x,y)
def f(x, y):
    return np.sin(x) * np.cos(y)

Z = f(X, Y)
plt.plot(Z)
plt.show()











    
