# Тут в цілому все добре
# Теоретично можна було б додати use friendly перевірки
# з гарним повідомленням про помилку
n = int(input("Введіть початок проміжку ")) 
m = int(input("Введіть кінець проміжку "))

evenItems = []
oddItems = [] 
for number in range(n,m+1):
    if number % 2 == 0:
        evenItems.append(number)
    else:
        oddItems.append(number)

print("Проміжок ", n, " - ", m)
print("Парні - ", evenItems)
print("Непарні - ", oddItems)