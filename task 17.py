per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = list(per_cent.values())
money = int(input("Введите сумму: "))
D = []
D.append(L[0] * money/100)
D.append(L[1] * money/100)
D.append(L[2] * money/100)
D.append(L[3] * money/100)
print("deposit =", D)
print("Максимальная сумма, которую вы можете заработать -", max(D))
