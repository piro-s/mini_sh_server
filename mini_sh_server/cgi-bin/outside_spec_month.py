#!/usr/bin/python3
import cgi
import os
from pathlib import Path
import datetime
import calendar


relativePath = "../temper/allMonth"
filepath = Path(__file__).parent / relativePath
content = os.listdir(filepath.resolve())


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Monthly temperatures</title>
    </head>
    <body>

    <h2>Ежемесячные данные с esp32cam_outside:</h2>""")


# Last value
with open('temper/temp_last', 'r') as file:
    last_temper = file.readline()
    last_datetime = datetime.datetime.strptime((file.readline()), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')

    print("<h3>Последние данные:</h3>")
    print("<p>Температура: {}&#8451.</p>".format(last_temper))
    print("<p>Время обновления: {}.</p>".format(last_datetime))


# All month list
print("<hr><p>Year:</p>")
for it in content:
    print("<a href=\"#{}\">{}</a>".format(it, it))
    print("<p>Months:</p>")
    for month in os.listdir(filepath.resolve() / it):
        month_number = month.replace("allMonth_", "")
        month_number = month_number.replace(".png", "")
        print("<a href=\"#{}\">{}</a><br>".format(month, calendar.month_name[int(month_number)]))


# Links
print("<br><hr><br><a href=\"../../index.html\">Главная</a><br>")
print("<a href=\"outside_main.py\">Последние значения</a><br>")
print("<a href=\"outside_spec_day.py\">Температура за определенный день</a><br>")


# Today
print("<br><hr><h3>Данные за сегодня:</h3>")
print("<img src=\"../temper/temp_today.png\" alt=today>")


# Today's month
print("<br><hr><h3>Данные за текущий месяц:</h3>")
print("<img src=\"../temper/temp_todayMonth.png\" alt=todayMonth>")


# All month
# calendar.month_name[int(month_number)] # Month name
print("<br><hr><p>Year:</p>")
for it in content:
    print("<a name=\"{}\">{}</a>".format(it, it))
    print("<br><hr><p>Months:</p>")
    for month in os.listdir(filepath.resolve() / it):
        month_number = month.replace("allMonth_", "")
        month_number = month_number.replace(".png", "")
        print("<a name=\"{}\"></a><br>".format(month))
        print("<img src=\"../temper/allMonth/{}/{}\" alt={}>".format(it, month, month))


print("""</body>
        </html>""")