from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()

now = datetime.now()
current_time = now.strftime("%H:%M")
try:
    while True:
        print(current_time)
        sense.show_message(str(current_time))
        sleep(0.5)
        if current_time == "06:24":
            r = 17
            g = 255
            b = 0
            sense.clear((r, g, b))
        for event in sense.stick.get_events():
        # Check if the joystick was pressed
            if event.action == "pressed":
                # Check which direction
                if event.direction == "up":
                    temp = sense.get_temperature()
                    sense.show_message(str(round(temp,2)))
                    print(temp)
                elif event.direction == "down":
                    sense.show_letter("D")      # Down arrow
                elif event.direction == "left": 
                    sense.show_letter("L")      # Left arrow
                elif event.direction == "right":
                    sense.show_letter("R")      # Right arrow
                elif event.direction == "middle":
                    sense.clear()
                
                # Wait a while and then clear the screen
                sleep(0.5)
                sense.clear()

except KeyboardInterrupt:
    print("Light Shutdown")
    sense.clear()
