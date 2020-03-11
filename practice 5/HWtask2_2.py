from num2words import num2words
#ModuleNotFoundError: No module named 'num2words'
# гадаю треба явно додати модуль 'num2words', або зробити власну реалізацію
enterNum = input("Введіть число : ")
print(num2words(enterNum, lang='uk'))