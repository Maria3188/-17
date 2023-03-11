price = 0
ticket = int (input("Введите кол-во билетов:"))
age = int (input("Введите возраст:"))

if age <= 18:
    price = 0
    print ("Билет бесплатный")
elif 18 < age < 25:
        price = 990
else:
    age >= 25
    price = 1390

if ticket > 3:
    price = price - ((price / 100) * 10)
    print ("Сумма к оплате:", price*ticket, "руб., с учетом скидки 10%, т.к. Вы зарегистрировали больше 3-х человек")

print ( "Итого к оплате:", price*ticket, "руб.")