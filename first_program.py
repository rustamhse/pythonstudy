A = int(input('Введите A >> '))
B = int(input('Введите B >> '))
if A < B:
    for i in range(A, B + 1):
        print(i)
if A > B:
    for i in range(A, B-1,-1):
        print(i)
if A == B:
    print(A)     
