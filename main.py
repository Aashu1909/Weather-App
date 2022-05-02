from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root =Tk()
root.title('Weather App')
root.geometry('900x500')
root.resizable(False,False)

def getWeather():
    city=textfield.get()
    print('city:',city)
    geoLocation=Nominatim(user_agent='geoapiExercises')
    location=geoLocation.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)
    home=pytz.timezone(result)
    localTime=datetime.now(home)
    currentTime=localTime.strftime('%I:%M %p')
    clock.config(text=currentTime)
    name.config(text="CURRENT WEATHER")

    # Weather
    try:
        api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=b43f10ee28457f4de623661a00c68baf"
        json_data=requests.get(api).json()
        print(json_data)
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temperature=int(json_data['main']['temp']-272.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        # Putting there values in the labels
        temperature_label.config(text=(temperature,'°'))
        condition_label.config(text=f"{condition} Feels like {temperature}°")
        wind_label.config(text=f'{wind}km/hr')
        pressure_label.config(text=f'{pressure}')
        description_label.config(text=f'{description}')
        humidity_label.config(text=f'{humidity}')
    except Exception as e:
        messagebox.showerror('Weather App','invalid entry')

# Search Box
search_image=PhotoImage(file="Images/search.png")
my_image=Label(image=search_image)
my_image.place(x=25,y=25)

textfield=tk.Entry(root,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',border=0,fg="white")

textfield.place(x=60,y=50)
textfield.focus()
# Search_icon
search_icon=PhotoImage(file="Images\search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg='#404040',command=getWeather)
myimage_icon.place(x=400,y=38)

# Logo
logo_image=PhotoImage(file='Images/logo.png')
logo=Label(image=logo_image)
logo.place(x=150,y=100)

# Time
name=Label(root,font=('arial',15,'bold'))
name.place(x=30,y=100)
# Clock
clock=Label(root,font=('helvetica',20))
clock.place(x=30,y=130)
# Bottom BOX
frame_image=PhotoImage(file='Images/box.png')
frame=Label(image=frame_image)
frame.pack(padx=2,pady=5,side=BOTTOM)

# Wind
label1=Label(root,text="WIND",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400) 
#Humidity
label2=Label(root,text="HUMIDITY",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=260,y=400) 
#Description
label3=Label(root,text="PRESSURE",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=450,y=400) 
#Pressure
label4=Label(root,text="DESCRIPTION",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400) 

temperature_label=Label(font=('arial',70,'bold'),fg='#ee666d')
temperature_label.place(x=400,y=150)

# Atomospheric Condition
condition_label=Label(font=('arial',15,'bold'))
condition_label.place(x=400,y=250)

wind_label=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
wind_label.place(x=130,y=430)

humidity_label=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
humidity_label.place(x=290,y=430)

pressure_label=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
pressure_label.place(x=490,y=430)

description_label=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
description_label.place(x=700,y=430)

root.mainloop()
