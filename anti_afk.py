import pydirectinput as pdi
import random
import time

curr_coords = pdi.position()
screen_width, screen_height = pdi.size()
keys = ['w', 'a', 's', 'd', 'space']
afk_counter = 0
afk_threshold = 10 # in seconds

print("Anti-AFK Script Started")
print(f"Screen Resolution: {screen_width}x{screen_height}")
print("Press 'Ctrl + C' to stop the script.\n")

try:
    while True:
        if pdi.position() == curr_coords: # if no mouse movement is detected
            afk_counter += 1
        else:
            afk_counter = 0
            curr_coords = pdi.position()
        
        if afk_counter > afk_threshold:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            pdi.moveTo(x, y, 0.5)
            curr_coords = pdi.position()
            key = random.choice(keys)
            pdi.press(key)
            print(f"[ACTION] Mouse moved to ({x}, {y}) & Key '{key}' pressed.")
        
        print(f"[INFO] Anti-AFK running. Idle time: {afk_counter} seconds.")
        time.sleep(random.uniform(.9, 1.1))

except KeyboardInterrupt:
    print("\n[INFO] Anti-AFK Script Stopped.")
