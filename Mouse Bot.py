import pyautogui as pag
import random
import time

while True:
    y= random.randint(200,600)
    x= random.randint(500,700)

    pag.moveTo(x,y,0.5)
    time.sleep(2)
 