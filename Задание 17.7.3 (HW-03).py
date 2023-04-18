per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую Вы хотите положить под проценты ' ))
deposit = []
for bank in per_cent:
    deposit.append(int(money*per_cent.get(bank)/100))
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))