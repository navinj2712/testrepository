from tkinter import *
from PIL import ImageTk,Image
import requests
import json

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=2589AF6E-5605-47D1-B2E0-44875DBD07BC

root = Tk()
root.title("Air Quality")
root.iconbitmap("C:/Users/LENOVO/Designbolts-Handstitch-Social-Cloud.ico")
root.geometry("600x100")

def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)
    
    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=2589AF6E-5605-47D1-B2E0-44875DBD07BC")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "orange"
        elif category == "Unhealthy":
            weather_color = "red"
        elif category == "Very Unhealthy":
            weather_color = "purple"
        elif category == "Hazardous":
            weather_color = "maroon"
            
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica",15), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)

        root.configure(background=weather_color)
    
    except Exception as e:
        api = "IntelGraphicsProfiles"

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()
