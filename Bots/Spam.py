import pyautogui
from pyautogui import *
import time
senti = 0
loop = 0
print("///RED TOOLBOX")
text = input("What message would you like to send")
loop = int(input("how many times"))

sentloop = str(senti)
stringloop = str(loop)

time.sleep(5)

def spam():
    sentloop = str(senti)
    pyautogui.typewrite(text)
    time.sleep(0.1)
    pyautogui.typewrite(sentloop)
    time.sleep(0.1)
    pyautogui.typewrite("/")
    time.sleep(0.1)
    pyautogui.typewrite(stringloop)
    time.sleep(0.1)
    pyautogui.press("enter")

while senti < loop:
    senti = senti + 1
    spam()