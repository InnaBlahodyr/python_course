# ліпше arrEn -> letters
# також можна використати list(string.ascii_lowercase) і ми отримаємо той самий масив з латинських символів
arrEn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# insertData -> letter
# insertData звучить як заклик до дії і гарна назва для функції
# однак ми маємо змінну, тому можна просто вказати, що це letter
insertData = input("Введіть букву ")

for i, data in enumerate(arrEn):
    if data == insertData:
        prewItem = i-1 #prevItem
        nextItem = i+1
        print("Попередня буква: ", arrEn[prewItem])
        print("Введена буква", data)
        print("Наступна буква: ",arrEn[nextItem])