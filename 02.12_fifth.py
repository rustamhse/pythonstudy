l = ["Yurii Grinkov 18", "Maxim Grinkov 22", "Elizaveta Grinkova 17", "Natalia Grinkova 45"]
print(sorted(l, key = lambda x: int(x[-2:])))
print(sorted(l, key = lambda x: int(x[-2:]))[0])
