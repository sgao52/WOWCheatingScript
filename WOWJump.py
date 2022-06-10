import pyautogui
import time

# Retrieved from Bilibili
# Have to activate your WOW main interface to keep your character jumping per 30 seconds
for num in range (0, 1000):
    print('Prepare to Jump')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print('Pressed space')
    time.sleep(30)
