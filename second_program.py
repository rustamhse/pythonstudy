A = int(input('Введите A >> '))
B = int(input('Введите B >> '))
for i in range(A, B + 1):
    if (i // 1000) == i % 10 and (i // 100) % 10 == (i // 10) % 10:
        print(i)
