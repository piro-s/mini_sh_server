import json
import datetime
from calendar import monthrange
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, date2num


# filenames
fn_temp_last = 'temper/temp_last'
fn_temp_lastHour = 'temper/temp_lastHour.png'
fn_temp_lastDay = 'temper/temp_lastDay.png'
fn_temp_lastWeek = 'temper/temp_lastWeek.png'
fn_temp_lastTwoWeeks = 'temper/temp_lastTwoWeeks.png'
fn_temp_last30days = 'temper/temp_last30days.png'
fn_temp_lastAll = 'temper/temp_lastAll.png'
fn_temp_specDay = 'temper/temp_specDay.png'
fn_temp_specMonth = 'temper/temp_specMonth.png'
fn_temp_today = 'temper/temp_today.png'
fn_temp_todayMonth = 'temper/temp_todayMonth.png'



def show_lastTemper(data, show=False, save=False):
    # Return last receive temperature
    last_temper = data_all['values'][-1]['temperature'] # Last receive temp
    last_datetime = data_all['values'][-1]['datetime'] # Last receive temp


    if show:
        print(str(last_temper))
        print(str(last_datetime))
    if save:
        with open(fn_temp_last, 'w') as file:
            file.write(str(last_temper) + '\n')
            file.write(str(last_datetime))

    return last_temper


def show_lastHour(data, show=False, save=False):
    # Show temperature graph for the last hour
    start_date = datetime.datetime.now() - datetime.timedelta(hours = 1) # Last hour

    data_x = []
    data_y = []
    for item in data['values']:
        if(start_date < datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f')):
            data_x.append(item['datetime'])
            data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter = DateFormatter('%H:%M')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Last hour")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 10, 20, 30, 40, 50]))
    axes.xaxis.set_minor_locator(mdates.MinuteLocator(byminute=[5, 15, 25, 35, 45, 55]))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_lastHour)


def show_lastDay(data, show=False, save=False):
    # Show temperature graph for the last day
    start_date = datetime.datetime.now() - datetime.timedelta(days = 1) # Last day

    data_x = []
    data_y = []
    for item in data['values']:
        if(start_date < datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f')):
            data_x.append(item['datetime'])
            data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter = DateFormatter('%H:%M')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Last day")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    axes.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_lastDay)


def show_lastWeek(data, show=False, save=False):
    # Show temperature graph for the last week
    start_date = datetime.datetime.now() - datetime.timedelta(weeks = 1) # Last week

    data_x = []
    data_y = []
    for item in data['values']:
        if(start_date < datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f')):
            data_x.append(item['datetime'])
            data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter_major = DateFormatter('%m-%d')
    formatter_minor = DateFormatter('%H:%M')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Last week")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter_major)
    axes.xaxis.set_minor_formatter(formatter_minor)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    axes.xaxis.set_minor_locator(mdates.HourLocator(byhour=12))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_lastWeek)


def show_lastTwoWeek(data, show=False, save=False):
    # Show temperature graph for the last two weeks
    start_date = datetime.datetime.now() - datetime.timedelta(weeks = 2) # Last two weeks

    data_x = []
    data_y = []
    for item in data['values']:
        if(start_date < datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f')):
            data_x.append(item['datetime'])
            data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter_major = DateFormatter('%m-%d')
    formatter_minor = DateFormatter('%m-%d')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Last two weeks")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter_major)
    axes.xaxis.set_minor_formatter(formatter_minor)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    axes.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_lastTwoWeeks)


def show_last30days(data, show=False, save=False):
    # Show temperature graph for the last 30 days
    start_date = datetime.datetime.now() - datetime.timedelta(days = 30) # Last 30 days

    data_x = []
    data_y = []
    for item in data['values']:
        if(start_date < datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f')):
            data_x.append(item['datetime'])
            data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter_major = DateFormatter('%m-%d')
    formatter_minor = DateFormatter('%m-%d')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Last month")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter_major)
    axes.xaxis.set_minor_formatter(formatter_minor)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=6))
    axes.xaxis.set_minor_locator(mdates.DayLocator(interval=3))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_last30days)


def show_all(data, show=False, save=False):
    # Show temperature graph for all data
    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title("Outside temperature")
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    x_list = []
    y_list = []
    for item in data['values']:
        x_list.append(item['datetime'])
        y_list.append(item['temperature'])

    x_form = date2num(x_list)
    formatter = DateFormatter('%H:%M')

    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    axes.xaxis.set_minor_locator(mdates.MinuteLocator(byminute=30))
      
    axes.plot(x_form, y_list, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_lastAll)


def show_allMonths(data, year, show=False, save=False):
    # Show temperature graph all month in data
    for month in range(1, 13):
        spec_date = datetime.datetime.strptime(str(month), '%m')
        data_x = []
        data_y = []

        for item in data['values']:
            compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
            if(year == compare_date.year):
                if(spec_date.month == compare_date.month):
                    data_x.append(item['datetime'])
                    data_y.append(item['temperature'])

        if not data_x :
            continue

        data_x_form = date2num(data_x)
        formatter_major = DateFormatter('%m-%d')
        formatter_minor = DateFormatter('%m-%d')

        # Plot
        figure = plt.figure()
        axes = figure.add_subplot(1, 1, 1)
        plt.title(spec_date.strftime("%B"))
        plt.xlabel('Time')
        plt.ylabel('Temperature')

        axes.xaxis.set_major_formatter(formatter_major)
        axes.xaxis.set_minor_formatter(formatter_minor)
        axes.xaxis.set_tick_params(rotation=45)
        axes.xaxis.set_major_locator(mdates.DayLocator(interval=6))
        axes.xaxis.set_minor_locator(mdates.DayLocator(interval=3))
          
        axes.plot(data_x_form, data_y, label='outside')

        plt.grid(which='major', linestyle='-')
        plt.grid(which='minor', linestyle='--')
        plt.legend()

        if show:
            plt.show()
        if save:
            plt.savefig('temper/allMonth/{}/allMonth_{}.png'.format(year, spec_date.strftime("%m")))


def show_allDays(data, year, show=False, save=False):
    # Show temperature graph all days in month
    for month in range(1, 13):
        for day in range(1, monthrange(year, month)[1] + 1):
            spec_date = datetime.datetime.strptime(str(month) + '-' + str(day), '%m-%d')
            data_x = []
            data_y = []
            for item in data['values']:
                compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
                if(year == compare_date.year):
                    if(spec_date.month == compare_date.month):
                        if(spec_date.day == compare_date.day):
                            data_x.append(item['datetime'])
                            data_y.append(item['temperature'])

            if not data_x:
                continue

            data_x_form = date2num(data_x)
            formatter = DateFormatter('%H:%M')

            # Plot
            figure = plt.figure()
            axes = figure.add_subplot(1, 1, 1)
            plt.title(spec_date.strftime("%B") + ' ' + str(spec_date.day))
            plt.xlabel('Time')
            plt.ylabel('Temperature')

            axes.xaxis.set_major_formatter(formatter)
            axes.xaxis.set_tick_params(rotation=45)
            axes.xaxis.set_major_locator(mdates.HourLocator(interval=2))
            axes.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
              
            axes.plot(data_x_form, data_y, label='outside')

            plt.grid(which='major', linestyle='-')
            plt.grid(which='minor', linestyle='--')
            plt.legend()

            if show:
                plt.show()
            if save:
                plt.savefig('temper/allDays/{}/{}/allDay_{}.png'.format(year, spec_date.strftime("%m"), spec_date.strftime("%d")))


def show_specDay(data, day, show=False, save=False):
    # Show temperature graph for the specific day
    spec_date = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S.%f') # Specific date

    data_x = []
    data_y = []
    for item in data['values']:
        compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
        if(spec_date.year == compare_date.year):
            if(spec_date.month == compare_date.month):
                if(spec_date.day == compare_date.day):
                    data_x.append(item['datetime'])
                    data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter = DateFormatter('%H:%M')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title(spec_date.strftime("%B") + ' ' + str(spec_date.day))
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    axes.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_specDay)


def show_specMonth(data, month, show=False, save=False):
    # Show temperature graph for today
    spec_date = datetime.datetime.strptime(month, '%Y-%m-%d %H:%M:%S.%f') # Specific date

    data_x = []
    data_y = []
    for item in data['values']:
        compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
        if(spec_date.year == compare_date.year):
            if(spec_date.month == compare_date.month):
                data_x.append(item['datetime'])
                data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter_major = DateFormatter('%m-%d')
    formatter_minor = DateFormatter('%m-%d')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title(spec_date.strftime("%B"))
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter_major)
    axes.xaxis.set_minor_formatter(formatter_minor)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=6))
    axes.xaxis.set_minor_locator(mdates.DayLocator(interval=3))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_specMonth)


def show_today(data, show=False, save=False):
    # Show temperature graph for the specific day
    spec_date = datetime.datetime.now() # Today date

    data_x = []
    data_y = []
    for item in data['values']:
        compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
        if(spec_date.year == compare_date.year):
            if(spec_date.month == compare_date.month):
                if(spec_date.day == compare_date.day):
                    data_x.append(item['datetime'])
                    data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter = DateFormatter('%H:%M')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title(spec_date.strftime("%B") + ' ' + str(spec_date.day))
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    axes.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_today)


def show_todayMonth(data, show=False, save=False):
    # Show temperature graph for today's month
    spec_date = datetime.datetime.now() # Today's month

    data_x = []
    data_y = []
    for item in data['values']:
        compare_date = datetime.datetime.strptime(item['datetime'], '%Y-%m-%d %H:%M:%S.%f') # Compared date
        if(spec_date.year == compare_date.year):
            if(spec_date.month == compare_date.month):
                data_x.append(item['datetime'])
                data_y.append(item['temperature'])

    data_x_form = date2num(data_x)
    formatter_major = DateFormatter('%m-%d')
    formatter_minor = DateFormatter('%m-%d')

    # Plot
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    plt.title(spec_date.strftime("%B"))
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    axes.xaxis.set_major_formatter(formatter_major)
    axes.xaxis.set_minor_formatter(formatter_minor)
    axes.xaxis.set_tick_params(rotation=45)
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=6))
    axes.xaxis.set_minor_locator(mdates.DayLocator(interval=3))
      
    axes.plot(data_x_form, data_y, label='outside')

    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle='--')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig(fn_temp_todayMonth)



#JSON
filename_all = 'temper/temper_all'

with open(filename_all) as file:
    data_all = json.load(file)


# show_all(data_all)

# Show all
# show_allMonths(data_all, datetime.datetime.now().year, save=True)
# show_allDays(data_all, datetime.datetime.now().year, save=True)


# Show last
# show_lastTemper(data_all, save=True)
# show_lastHour(data_all, save=True)
# show_lastDay(data_all, save=True)
# show_lastWeek(data_all, save=True)
# show_lastTwoWeek(data_all, save=True)
# show_last30days(data_all, save=True)


# Show today
# show_today(data_all, save=True)
# show_todayMonth(data_all, save=True)


# show_specDay(data_all, data_all['values'][-1]['datetime'], save=True)
# show_specMonth(data_all, data_all['values'][-1]['datetime'], save=True)

# monthrange(datetime.date.today().year, datetime.date.today().month)[1] # Days in month