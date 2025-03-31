import random
our_group = ["Абраменко", "Григорьева", "Ярошевская", "Гиносян", "Оржаховская", "Добров", "Сажнев", "Юлдашев", "Сухопар", "Малахов"]
not_our_group = ["Кринжов", "Иванов", "Пупкина", "Йегер", "Учиха", "Ягами", "Пастухов", "Липсихаскина", "Поттер", "Бэггинс" ]
team = []
i=0
while i<5:
    member = random.choice(our_group)
    if member not in team:
        team.append(member)
        i+=1
while i<10:
    member = random.choice(not_our_group)
    if member not in team:
        team.append(member)
        i+=1
team.sort()
team_best = tuple(team)

print("Первая группа: ", our_group)
print("Вторая группа: ", not_our_group)
print("Сборная: ", team_best)
print("В команде ", len(team_best)," человек, среди них", team_best.count("Иванов"), "студент(ов) с фамилией Иванов.")