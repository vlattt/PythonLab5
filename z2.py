import numpy as np

def choose():
    a = int(input("введите номер задачи в задании №2:"))
    if a == 1:
        one()
    elif a == 2:
        two()
    elif a == 3:
        three()
    elif a == 4:
        four()
    elif a == 5:
        five()
    elif a == 6:
        six()
    elif a == 7:
        seven()
    elif a == 8:
        eight()
    elif a == 9:
        nine()
    else:
        print("введите задание от 1 до 10")
def one():
    mas = np.arange(1,11)
    print(mas)

def two():
    mas = np.random.rand(3,3)
    print(mas)

def three():
    mas1 = np.zeros(10)
    b = mas1[2]
    b = 5
    print(mas1)

def four():
    mas1 = np.arange(1,13)
    mas2 = mas1.reshape(3, 4)
    print(mas2)

def five():
    mas = np.random.randint(1, 10, (5, 5))
    sum = sum(mas)
    print(sum)

def six():
    mas = np.random.randint(1, 11, (4, 4))
    max = np.max(mas, axis=1)
    for i in max:
        print(i)

def seven():
    mas = np.random.randint(1, 10, (3, 3))
    res = mas * 2
    print(res)

def eight():
    mas1 = np.arange(9).reshape(3, 3)
    mas2 = np.arange(9).reshape(3, 3)
    res = np.dot(mas1, mas2)
    print(res)

def nine():
    mas = np.random.randint(0, 6, (3, 3))

    print("Массив:")
    print(mas)

    det = np.linalg.det(mas)

    print("Определитель матрицы:")
    print(det)












