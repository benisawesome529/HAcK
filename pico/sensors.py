from hcsr04 import HCSR04
from dht import DHT11
from machine import Pin
from time import sleep

ultrasonic = HCSR04(trigger_pin=15, echo_pin=16, echo_timeout_us=10000)
tempHumidity = DHT11(Pin(17, Pin.IN, Pin.PULL_UP))

def getDistance():

    distance = ultrasonic.distance_cm()
    print(distance)
    return distance

def getTemperatureAndHumidity():

    tempHumidity.measure()
    temperature = tempHumidity.temperature()
    print("Temperature in C: ", temperature)
    humid = tempHumidity.humidity()
    print("Humidity: ", humid)
    return temperature, humid
    

#