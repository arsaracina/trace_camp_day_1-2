import requests
import pprint
from datetime import datetime
from datetime import timedelta
from datetime import date
from time import sleep

pp = pprint.PrettyPrinter(indent=4)
# https://api.nasa.gov/api.html#apod
# This is a parameter
api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"

# We are doing a get request
start_date = date(2017,4,1)
print(start_date)

for day_increment in range(1, 10, 1):
    date = start_date + timedelta(days = day_increment)
    print(date)
    r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
    print(r.status_code)
    pp.pprint(r.json())
    url = r.json()["url"]
    from IPython.display import Image
    from IPython.display import display,clear_output
    img = Image(url = url)
    display(img)
    sleep(5)
    clear_output()
