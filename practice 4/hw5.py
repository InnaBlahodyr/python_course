#  Круто було б додати userfriendly перевірку
# з гарним повідомленням про помилки (користувач може ввести стрічку, пробіл і т.д)
enterData = input("Введіть число: ")

sumNum = 0
for i in enterData:
    sumNum += int(i)

print("Сумма цифр: ", sumNum)
print("Кількість: ", len(enterData))