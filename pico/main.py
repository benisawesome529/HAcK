from connections import connect_mqtt, connect_internet
from time import sleep
from movement import move_forward, move_backward, turn_left, turn_right, stop
from sensors import getDistance , getTemperatureAndHumidity
# from constants import ssid, mqtt_server, mqtt_user, mqtt_pass


# Function to handle an incoming message

def cb(topic, msg):
    print(f"Topic: {topic}, Message: {msg}")
    
    if topic == b"direction":
        
        if msg == b"forward":
            move_forward()
            
        elif msg == b"right":
            turn_right()            
            
        elif msg == b"left":
            turn_left()
            
        elif msg == b"reverse":
            move_backward()
                    
        else:
            
            stop()
            
def main():
    
    try:
        connect_internet("HAcK-Project-WiFi-2", "UCLA.HAcK.2024.Summer")
        client = connect_mqtt("ec7eab46cd244886b9fb27d09c5e58b8.s1.eu.hivemq.cloud", "HAcKProject", "HAcKTeam2")
        
        
        
        client.set_callback(cb)
        client.subscribe("direction")
        client.subscribe("claw")
        print("here")
        
        
        
        
        while True:
            x = getDistance()
            #hum = getHumidity()
            temperature, hum = getTemperatureAndHumidity() 
            client.publish(b"ultrasonic", str(x).encode('utf-8'))
            client.publish(b"temp", str(temperature))               
            client.publish(b"humidity", str(hum))
            client.check_msg()
            sleep(3)
        



    except KeyboardInterrupt:
        print('keyboard interrupt')

        
        
        
if __name__ == "__main__":
    main()


