#coding:utf-8
for x in range(10):
    if x == 0:
        continue
    for y in range(10):
        if y == 0:
            continue
        print(x * y, end="\t")
    print()
