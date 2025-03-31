import random
a = [random.randrange(11) for i in range(8)]
a_dub = []
k=0
for i in range(len(a)):
    if a.count(a[i]) > 1:
        k+=1
        if a[i] not in a_dub:
            a_dub.append(a[i])

if k != 0:
    print(a)
    print("Повторяющиеся значения: ", a_dub)
else:
    print(a, " - повторов нет.")
