import calendar
import datetime
import locale

locale.setlocale(locale.LC_ALL, "uk_UA")

date_entry = input('Введіть дату в форматі :  YYYY-MM-DD ') 

year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day) 

date1 = calendar.weekday(year,month,day)

dt_stamp = datetime.datetime(year, month, day)
trDate = dt_stamp.strftime('%d.%m.%Y' )

monthName =  dt_stamp.strftime("%B")
countDays = calendar.monthrange(year, month)[1]

print(monthName, year ,"рік","-", countDays, "день")

if date1 == 5 or date1 == 6:
    
    print(trDate,"- вихідний ")
else:
    print(trDate,"- робочий")  


