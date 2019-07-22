import pyowm
location=input("What is your location?")
owm = pyowm.OWM('a890f86bdf5ad37ff9800f966a10ac2f')
observation = owm.weather_at_place(location)
w = observation.get_weather()
t=w.get_temperature()
cloud=w.get_status()
#clouds= input("Enter a condition")
condition=w.get_status()
print(w)
print(t)
print(cloud)
print(condition)

marie=w.get_wind()
print(marie["speed"])
print(w.get_humidity())
print(w.get_status())
print(w.get_detailed_status())

from gpiozero import LED
from signal import pause
from time import sleep

Red=LED(18)
Green=LED(2)

if w.get_status()==cloud:
    Red.off()
    sleep(15)
    Green.on()
    Red.off()
else:
    Green.off()
    sleep(15)
    Red.on()
    Green.off()