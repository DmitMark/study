num = int(input('Введите количество билетов '))
item = 1
price = 0
while item <= num:
    year = int(input(f'Введите возраст {item} посетителя '))
    if year >= 18:
        if year < 25:
            price += 990
        elif year >= 25:
            price += 1390
    item += 1
if num > 3:
    print('Сумма к оплате, с учетом 10% скидки ', price * 0.9, 'руб')
else:
    print('Сумма к оплате', price, 'руб')
