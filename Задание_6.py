# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчёте на одного сотрудника.
#
v = int(input('ввести размер выручки:  '))
p = int(input('ввести размер прибыли:  '))
# Вычисляем рентабельность
r = p / v
print("Рентабельность =", r)
n = int(input('ввести численность сотрудников фирмы:  '))
# Определить прибыль фирмы на одного сотрудника
p1 = p / n
print("Прибыль фирмы на одного сотрудника =", p1)


# результаты вычислений
# ввести размер выручки:  1000
# ввести размер прибыли:  500
# Рентабельность = 0.5
# ввести численность сотрудников фирмы:  30
# Прибыль фирмы на одного сотрудника = 16.666666666666668