import pyautogui
import time
f = "0"
a = int(input("Ile mam wypisac liczb:"))
b = int(input("Od jeakiej liczby zaczanc:"))
c = int(input("Jaki jest cooldawn:"))
if c < 0:
    c = 0
time.sleep(10)
for x in range(b, a+b+1):
    f = str(x)
    pyautogui.typewrite(f)
    pyautogui.press("enter")
    time.sleep(c+0.75)
pyautogui.typewrite("to koniec xdddd. To byl program autorstwa emotikon90elo5.https://github.com/emotikon90elo5/sdsdsd")
pyautogui.press("enter")