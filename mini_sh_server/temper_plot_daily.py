from temper_plot import *

# Run at the end of the day
show_allMonths(data_all, datetime.datetime.now().year, save=True)
show_allDays(data_all, datetime.datetime.now().year, save=True)