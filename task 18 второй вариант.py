price = 0
ticket = int (input("Введите кол-во билетов:"))
for i in range(ticket):
    i += 1
    age = int(input(f"Введите возраст для билета № {i}:"))
    if age <= 18:
        print ("Билет бесплатный")
    elif 18 < age < 25:
        price += 990
        print('Стоимость билета - 990 руб.')
    else:
        price += 1390
        print('Стоимость билета - 1390 руб.')
if ticket >= 3:
    price = price - ((price / 100) * 10)
    print (f'Сумма к оплате:", {price}, "руб., с учетом скидки 10%, т.к. Вы зарегистрировали больше 3-х человек')
else:
    print( f'Итого к оплате:,{price}, "руб.')