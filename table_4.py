#coding:utf-8
D1 = {}
for x in range(10):
    if x == 0:
        continue
    L1 = []
    for y in range(10):
        if y == 0:
            continue
        L1.append(x * y)
    D1[x] = L1

for x in range(10):
    if x == 0:
        continue
    for y in D1[x]:
        print(y, end = '\t')
    print()
