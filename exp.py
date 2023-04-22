from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time
import keyboard


expFirst = None
i = 0
while True:
    if keyboard.is_pressed("esc"):
        break

    exp = imagesearch("exp.png")
    reload = imagesearch("reload.png")
    open = imagesearch("open.png")

    if exp[0] == -1:
        pyautogui.leftClick(reload[0] + 10, reload[1] + 10)
        time.sleep(0.5)
    elif exp[0] != -1:
        if expFirst == exp[0] or expFirst == None and i != 4:
            pyautogui.leftClick(open[0] + 10, open[1] + 10)
            expFirst = exp[0]
            i + 1
            time.sleep(5)
        else:
            pyautogui.leftClick(reload[0] + 10, reload[1] + 10)
            expFirst = None
            i = 0
            time.sleep(0.5)