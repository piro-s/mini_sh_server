import requests
import json
from datetime import datetime


filename_all = 'temper/temper_all'


# Datetime and temperature
datetime_now = datetime.now() # Current date and time
date_now = datetime_now.strftime("%Y.%m.%d") # Format date
time_now = datetime_now.strftime("%H:%M:%S") # Format time

temper_response = requests.get("http://192.168.0.221:81/temper") # Current temperature
temper_now = json.loads(temper_response.text)


# JSON
temper_now_json = { 
    'datetime': str(datetime_now),
    'date': date_now,
    'time': time_now,
    'temperature': temper_now['temperature'] }
#print(temper_now_json)

with open(filename_all) as file:
    data_all = json.load(file)

data_all['values'].append(dict(temper_now_json))
data_all['total'] = len(data_all['values'])

with open(filename_all, 'w') as file:
    json.dump(data_all, file, indent=4)

