from machine import Pin, PWM
from time import sleep

servoPin = 28
secondPin = 27
servo = PWM(Pin(servoPin))
secondServo = PWM(Pin(secondPin))
servo.freq(50)
secondServo.freq(50)

while True:
    angle = 50
    writeVal = 6553/180*angle+1638
    servo.duty_u16(int(writeVal))
    angle = 90
    writeVal = 6553/180*angle+1638
    secondServo.duty_u16(int(writeVal))
    sleep(.02)
