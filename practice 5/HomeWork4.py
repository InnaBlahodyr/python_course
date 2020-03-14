# Створити програму для генерації випадкового масиву чисел. 
# Масив має бути створений випадковими числами (розмір 20 елементів). 
# Визначити скільки елементів масиву дорівнюють числу введеному користувачем. 



import random

data = int(input("Введіть число : "))
counter = 0
arr = []
for i in range(20):
    arrItem= random.randint(1,20)
    if i % 2 != 0 :
        arr.append(arrItem * -1)
    else:
        arr.append(arrItem)
print(arr)

for i in arr :
    if data == i:
        counter = counter + 1

print(counter)      