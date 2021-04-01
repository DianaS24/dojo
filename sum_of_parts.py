ls = [0, 1, 3, 6, 10]
ls2 = []
for x in range(len(ls)):
    sum1 = 0
    for y in range(len(ls)):
        if y >= x:
            sum1 = sum1 + ls[y]
    ls2.append(sum1)
print(ls2)
