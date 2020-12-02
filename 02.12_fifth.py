a = ["Yurii Grinkov 18", "Maxim Grinkov 22", "Elizaveta Grinkova 17", "Natalia Grinkova 45"]
a = sorted(a, key = lambda x: int(x[-2]))
answer = a[0]
for i in range(0, len(a) - 1):
  if a[i] < answer:
    answer = a[i]
print(answer)
