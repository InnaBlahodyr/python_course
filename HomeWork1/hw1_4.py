arrEn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
insertData = input("Введіть букву ")

for i, data in enumerate(arrEn):
    if data == insertData :
        prewItem = i-1
        nextItem = i+1
        print("Попередня буква: ",arrEn[prewItem])
        print("Введена буква", data)
        print("Наступна буква: ",arrEn[nextItem])
