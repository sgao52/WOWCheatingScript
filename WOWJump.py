import pyautogui
import time

for num in range (0, 1000):
    print('Prepare to Jump')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print('Pressed space')
    time.sleep(30)
