from glob import glob
from tkinter import *
from bs4 import BeautifulSoup
import requests ,json

def wea(c):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
    CITY = c

    # Your API key
    API_KEY = "--------"

    # updating the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    # Sending HTTP request
    response = requests.get(URL)

    # checking the status code of the request
    if response.status_code == 200:
        
    # retrieving data in the json format
        data = response.json()
    
    # take the main dict block
        main = data['main']
    
    # getting temperature
        temperature = main['temp']
    # getting feel like
        temp_feel_like = main['feels_like']  
    # getting the humidity
        humidity = main['humidity']
    # getting the pressure
        pressure = main['pressure']
    
    # weather report
        weather_report = data['weather']
    # wind report
        wind_report = data['wind']
        
        b=Label(text='city='+c)
        b.place(x=30,y=100)
        b1=Label(text="Temperature="+str(temperature))
        b1.place(x=30,y=120)
        b2=Label(text="Feels Like="+str(temp_feel_like))
        b2.place(x=30,y=140)
        b3=Label(text="Humidity="+str(humidity))
        b3.place(x=30,y=160)
        b4=Label(text="pressure="+str(pressure))
        b4.place(x=30,y=180)
        b5=Label(text="Weather report="+str(weather_report[0]['description']))
        b5.place(x=30,y=200)
        b6=Label(text="Wind speed="+str(wind_report['speed']))
        b6.place(x=30,y=220)
        
    else:
    # showing the error message
        print("Error in the HTTP request")



app=Tk()
app.geometry("500x500")
app.title("Weather")
h=Label(text="Weather")
h.pack()

city_name=Label(text="City :")
city_name.place(x=30,y=30)

city=StringVar()

name=Entry(textvariable=city,width='30')
name.place(x=130,y=30)

button=Button(app,text="Find",command=lambda: wea(city.get()),width='15',height='1',bg='grey')
button.place(x=150,y=70)

mainloop()
