#!/usr/bin/python3
import cgi
import os
from pathlib import Path
import datetime
import calendar


relativePath = "../temper/allDays"
filepath = Path(__file__).parent / relativePath
content = os.listdir(filepath.resolve())


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Daily temperatures</title>
    </head>
    <body>

    <h2>Ежедневные данные с esp32cam_outside:</h2>""")


# Last value
with open('temper/temp_last', 'r') as file:
    last_temper = file.readline()
    last_datetime = datetime.datetime.strptime((file.readline()), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')

    print("<h3>Последние данные:</h3>")
    print("<p>Температура: {}&#8451.</p>".format(last_temper))
    print("<p>Время обновления: {}.</p>".format(last_datetime))


# All month list
print("<hr><p>Year:</p>")
for year in content:
    print("<p>{}:</p>".format(year))
    print("<hr align=\"left\"width=\"20%\"><p>Months:</p>")
    months = [] # for sort to alphabetic
    for month in os.listdir(filepath.resolve() / year):
        months.append(month)

    months.sort()
    for month in months:
        month_number = month.replace("allDay_", "")
        month_number = month_number.replace(".png", "")

        print("<a href=\"../temper/allDays/{}/{}/{}.html\">{}</a><br>".format(str(year), month, month, calendar.month_name[int(month_number)]))

        # Create new web pages for all days in specific month
        with open('temper/allDays/' + str(year) + '/' + month + '/' + month + '.html', 'w') as html:
            html.write("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>{} {}</title>
                </head>
                <body>""".format(str(year), calendar.month_name[int(month_number)]))


            # Links
            html.write("<a href=\"../../../../index.html\">Главная</a><br>")
            html.write("<a href=\"../../../../cgi-bin/outside_main.py\">Последние значения</a><br>")
            html.write("<a href=\"../../../../cgi-bin/outside_spec_month.py\">Температура за определенный месяц</a><br>")
            html.write("<a href=\"../../../../cgi-bin/outside_spec_day.py\">Температура за определенный день</a><br>")


            html.write("<br><hr><br><h3>Данные за {} {}</h3>".format(str(year), calendar.month_name[int(month_number)]))

            days = [] # for sort
            for day in os.listdir(filepath.resolve() / year / month):
                if day == month + '.html':
                    continue
                days.append(day)

            days.sort()
            for day in days: # hyperlinks
                day_number = day.replace("allDay_", "")
                day_number = day_number.replace(".png", "")
                html.write("<a href=\"#{}\">{}</a><br>".format(day, day_number))

            for day in days: # data
                html.write("<a name=\"{}\"></a><br>".format(day))
                html.write("<img src=\"{}\" alt={}_{}><br>".format(day, month, day))

            html.write("""</body>
                    </html>""")


# Links
print("<br><hr><br><a href=\"../../index.html\">Главная</a><br>")
print("<a href=\"outside_main.py\">Последние значения</a><br>")
print("<a href=\"outside_spec_month.py\">Температура за определенный месяц</a><br>")


# Today
print("<br><hr><h3>Данные за сегодня:</h3>")
print("<img src=\"../temper/temp_today.png\" alt=today>")


# Today's month
print("<br><hr><h3>Данные за текущий месяц:</h3>")
print("<img src=\"../temper/temp_todayMonth.png\" alt=todayMonth>")


print("""</body>
        </html>""")