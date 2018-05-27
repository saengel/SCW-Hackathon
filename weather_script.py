#!/usr/bin/python

from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer
import webbrowser

sense = SenseHat()
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="7atqMMXyfwEQRXB83dmGJmVtpn12oKUr")
sense.clear()

try:
    while True:
        temp = sense.get_temperature()
        print("Celsius temperature: ",round(temp, 1),"C")
        temp = 1.8 * round(temp, 1) + 32
        logger.log("Temperature:", round(temp,1),"F")
        lightMessage = sense.show_message(str(int(temp)) + " F", scroll_speed = (0.08))

        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        logger.log("Humidity:", humidity)

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        logger.log("Pressure:", pressure)
        
        # Rain factor checked first
        if humidity >= 90 and temp > 32:
            #webbrowser.open_new_tab('rain.html')
            print("Oh no, it may rain. May sure you have boots and a rain jacket.")
            
        elif humidity >= 90 and temp <= 32:
            print("Chance of snow! DO a snow dance and pray for no school, but..")
            print("if school isn't cancelled, make sure to bring boots and waterproof gear.")

        # A series of temperature checks at our desired intervals
        if temp <= 25:
            #webbrowser.open_new_tab('winter.html')
            print("It';s freezing out! Bundle up!")
        elif temp <= 40:
            #webbrowser.open_new_tab('fall.html')
            print("It's cold. Leggings and boots are a good call right now.")
        elif temp <= 50:
            #webbrowser.open_new_tab('spring.html')
            print("Haha. No one knows what to wear when it's 50 degrees. Good luck!")
        elif temp <= 60:
            #webbrowser.open_new_tab('spring.html')
            print("Too warm for a sweatshirt, I think we need T-shirts.")
        elif temp <= 75:
            #webbrowser.open_new_tab('summer.html')
            print("Time to break out the flowy skirts and stuff")
        else:
            #webbrowser.open_new_tab('summer.html')
            print("It's so hot! Jump in a pool before doing anything else today.") 
        
        time.sleep(30)
		
except KeyboardInterrupt:
	pass
    
sense.clear()


