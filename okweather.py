import pyowm
from gpiozero import LED
from signal import pause
from time import sleep

location=input("What is your location?")
owm = pyowm.OWM('a890f86bdf5ad37ff9800f966a10ac2f')
observation = owm.weather_at_place(location)
w = observation.get_weather()
t=w.get_temperature()
condition = ["Sunny", "Clouds", "Haze", "Clear", "Rain", "Sunshine"]
print(w)
print(t)

marie=w.get_wind()
print(marie["speed"])
print(w.get_humidity())
print(w.get_status())
print(w.get_detailed_status())



Red=LED(17)
Green=LED(27)

if w.get_status()==condition[1]:
    Green.off()
    Red.on()
    print("Be cautious! Take a raincoat or Umbrella.")
    sleep(7)
    Red.off()
elif w.get_status()==condition[0]:
    Red.off()
    Green.on()
    print("Looks bright. Have a wonderful day!")
    sleep(7)
    Green.off()
elif w.get_status()==condition[2]:
    Red.off()
    Green.on()
    print("Not bad. Have a nice day!")
    sleep(7)
    Green.off()
elif w.get_status()==condition[3]:
    Red.off()
    Green.on()
    print("Seems clear. Enjoy your day!") 
    sleep(7)
    Green.off()
elif w.get_status()==condition[4]:
    Green.off()
    Red.on()
    print("Oops.It's raining.Take your umbrella or raincoat.")
    sleep(7)
    Red.off()
elif w.get_status()==condition[5]:
    Red.off()
    Green.on()
    print("It's sunny! Have a blissful day!")
    sleep(7)
    Green.off()
    
