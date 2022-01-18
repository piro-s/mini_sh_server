#!/usr/bin/python3
import cgi
import os
from pathlib import Path
import datetime


relativePath = "../temper/"
filepath = Path(__file__).parent / relativePath
content = os.listdir(filepath.resolve())


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Outside main</title>
        </head>
        <body>

        <h2>Последние данные с esp32cam_outside:</h2>""")


# Last value
with open('temper/temp_last', 'r') as file:
        last_temper = file.readline()
        last_datetime = datetime.datetime.strptime((file.readline()), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')

        print("<h3>Последние данные:</h3>")
        print("<p>Температура: {}&#8451.</p>".format(last_temper))
        print("<p>Время обновления: {}.</p>".format(last_datetime))


# Links
print("<hr><br><a href=\"../../index.html\">Главная</a><br>")
print("<a href=\"outside_spec_month.py\">Температура за определенный месяц</a><br>")
print("<a href=\"outside_spec_day.py\">Температура за определенный день</a><br>")


# Last hour
print("<br><hr><h3>Данные за последний час:</h3>")
print("<img src=\"../temper/temp_lastHour.png\" alt=last_hour>")


# Last day
print("<br><hr><h3>Данные за последний день:</h3>")
print("<img src=\"../temper/temp_lastDay.png\" alt=last_day>")


# Last week
print("<br><hr><h3>Данные за последнюю неделю:</h3>")
print("<img src=\"../temper/temp_lastWeek.png\" alt=last_week>")


# Last two weeks
print("<br><hr><h3>Данные за последние две недели:</h3>")
print("<img src=\"../temper/temp_lastTwoWeeks.png\" alt=last_twoWeeks>")


# Last 30 days
print("<br><hr><h3>Данные за последние 30 дней:</h3>")
print("<img src=\"../temper/temp_last30days.png\" alt=last_30days>")


# for it in content:
#         print("<p>Dir: {}</p>".format(it))

#         with open(relativePath + it) as file:
#                 print("<img src=\"../temper/{}\" alt={}>".format(it, it))


# <a href="#section2">Go to Section 2</a>
# <img src="img_girl.jpg" alt="Girl in a jacket">


print("""</body>
        </html>""")