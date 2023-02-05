import requests
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# create object
app = Tk()
app.title("World Weather App")
app.geometry("450x475")

# necessary repeated values
degree_sign = u'\N{DEGREE SIGN}'
api_key = 'd47ed13876e8b3d65f2c105017e69d4b'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'

# function to get weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        # icon
        icon = json['weather'][0]['icon']

        # city and country
        city = json['name']
        country = json['sys']['country']

        # min max temp
        min_temp = round(json['main']['temp_min'])
        max_temp = round(json['main']['temp_max'])

        # temp in C and F
        temp_fh = round(json['main']['temp'])
        temp_celsius = round((5 / 9) * (temp_fh - 32))

        # sunrise/sunset
        sunrise = (json['sys']['sunrise'])
        sunset = (json['sys']['sunset'])

        # temp in C and F
        weather1 = json['weather'][0]['main']

        final = [city, country, temp_fh,
                 temp_celsius, weather1, icon, sunrise, sunset, min_temp, max_temp]
        return final
    else:
        print("NO Content Found")


# explicit function to search city
def search():
    global img
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        sunrise_label['text'] = "{}".format(
            'Sunrise: ' + datetime.utcfromtimestamp(weather[6]).strftime('%H:%M' + ' A.M'))
        sunset_label['text'] = "{}".format(
            'Sunset: ' + datetime.utcfromtimestamp(weather[7]).strftime('%H:%M' + ' P.M'))

        temperature_label['text'] = str(weather[2]) + degree_sign + " F"
        temperature_label.pack()

        weather_l['text'] = weather[4]
        img["file"] = 'weather_icons\\{}.png'.format(weather[5])

        high_label['text'] = "{}".format('High: ' + str(weather[9]) + degree_sign)
        low_label['text'] = "{}".format('Low: ' + str(weather[8]) + degree_sign)
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

# add labels, buttons and text
topLabel = Label(text='WORLD   WEATHER   APP', font=("Arial", 23))
topLabel.pack()

secLabel = Label(text='Look up a city!', font=('Arial', 10))
secLabel.pack()

# weather type icon
result2 = requests.get(url.format('London', api_key))
weather = getweather("London")
if result2:
    json2 = result2.json()

    city_text = StringVar()
    city_entry = Entry(app, textvariable=city_text, width=25)
    city_entry.pack()

    Search_btn = Button(app, text="Search City",
                        width=15, height=2, command=search)
    Search_btn.pack()

    # icon
    icon = json2['weather'][0]['icon']
    img = PhotoImage(file='')
    img["file"] = 'weather_icons\\{}.png'.format(weather[5])

    Image = Label(app, image=img, width=150, height=125)
    Image.config(bg='gray')
    Image.pack()

    weather1 = json2['weather'][0]['main']
    weather_l = Label(app, text=weather1, font=('Arial', 10))
    weather_l.pack()

    # city and country
    city2 = json2['name']
    country = json2['sys']['country']

    # temp in C and F
    temp_fh = round(json2['main']['temp'])
    temp_celsius = round((5 / 9) * (temp_fh - 32))
    temperature_label = Label(app, text=temp_fh, font=('Arial', 35))
    temperature_label.pack()

    weather = getweather("London")
    if weather:
        location_lbl = Label(app, text=weather[0] + ', ' + weather[1], font=('Arial', 16))
        location_lbl.pack()
        sunrise = (json2['sys']['sunrise'])
        sunset = (json2['sys']['sunset'])
        min_temp = round(json2['main']['temp_min'])
        max_temp = round(json2['main']['temp_max'])
        temperature_label['text'] = str(weather[2]) + degree_sign + " F"
        weather_l['text'] = weather[4]
        img["file"] = 'weather_icons\\{}.png'.format(weather[5])

high_label = Label(app, text='High: ' + str(max_temp) + degree_sign, font=('Arial', 10))
high_label.pack()

low_label = Label(app, text='Low: ' + str(min_temp) + degree_sign, font=('Arial', 10))
low_label.pack()

sunrise_label = Label(app, text='Sunrise: ' + datetime.utcfromtimestamp(sunrise).strftime('%H:%M' + ' A.M'),
                      font=('Arial', 10))
sunrise_label.pack()

sunset_label = Label(app, text='Sunset: ' + datetime.utcfromtimestamp(sunset).strftime('%H:%M' + ' P.M'),
                     font=('Arial', 10))
sunset_label.pack()

app.mainloop()