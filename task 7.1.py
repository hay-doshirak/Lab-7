import random
a=[random.randrange(1,11) for i in range(5)]
x = int(input("Введите число от 1 до 10: "))
if x in a:
    print(a)
    print("Поздравляю, Вы угадали, число есть в списке!")
else:
    print(a)
    print("Числа нет в списке.")
