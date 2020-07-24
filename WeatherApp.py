import tkinter as tk
from tkinter import messagebox
import requests

HEIGHT = 500
WIDTH = 600


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def get_weather(city):
	weather_key = '399bb597a55bd3bf2f94315e0eb16ccd'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		humidity = weather['main']['humidity']
		label['text'] = 'City: %s \nConditions: %s \nTemperature (°F): %s \nHumidity (%): %s' % (name, desc, temp, humidity)
	except:
		messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name") 
  


root = tk.Tk()
root.title('Weather Application')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#ff8080', bd=12)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,bg='#99ccff', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#ff8080', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame,font=40,bg='#ffff99',anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()