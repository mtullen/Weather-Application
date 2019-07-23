import Tkinter as tk
import requests
from PIL import ImageTk, Image

# Constants
HEIGHT = 800
WIDTH = 1280


# Searches through api_key
def weatherSearch(city_id):
    api_key = '0415eba1c09aad342b5b1529000ff9f0'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'appid': api_key, 'q': city_id, 'units': 'imperial'}
    response = requests.get(url, params=parameters)
    weather = response.json()

    label['text'] = formatInfo(weather)

    return 0


# JSON Formatting
def formatInfo(weather):

    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        description = weather['weather'][0]['description']

        result = 'City:  %s\nCountry:  %s\nTemperature:  %s Degrees Fahrenheit\nDescription:  %s' % (city, country, temp, description.title())

    except:
        result = 'There was a problem in retrieving the information.  Please try again.'

    return result


# Creating the widgets
window = tk.Tk()
window.title("Mark's Weather Application")

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('bg.jpg'))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

top_frame = tk.Frame(window, bg='#3d3d3d', bd=5)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(top_frame, font=12)
entry.place(relwidth=0.69, relheight=1)

button = tk.Button(top_frame, text='Enter', font=12, command=lambda: weatherSearch(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

bottom_frame = tk.Frame(window, bg='#3d3d3d', bd=10)
bottom_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(bottom_frame, text='Enter the name of an city.', bg='white', fg='black')
label.place(relwidth=1, relheight=1)

window.mainloop()