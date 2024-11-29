import pyautogui
import time
import keyboard
import threading

pyautogui.FAILSAFE = False

click_interval = 0.1 #speed
running = False 

def auto_click():
    while running:
        pyautogui.click()  
        time.sleep(click_interval)  

def key_listener():
    global running
    print("Press ` to start/stop the auto clicker. Press Esc to exit.")
    while True:
        if keyboard.is_pressed('`'): #hotkey
            time.sleep(0.3) 
            running = not running  
            if running:
                print("Auto clicker started!")
                threading.Thread(target=auto_click).start() 
            else:
                print("Auto clicker stopped!")

        if keyboard.is_pressed('esc'):  
            print("Exiting auto clicker.")
            break  

key_listener()
