from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time
import keyboard


seferFirst = None
i = 0
while True:
    if keyboard.is_pressed("esc"):
        break

    sefer = imagesearch("sefer.png")
    reload = imagesearch("reload.png")
    open = imagesearch("open.png")

    if sefer[0] == -1:
        pyautogui.leftClick(reload[0] + 10, reload[1] + 10)
        time.sleep(0.5)
    elif sefer[0] != -1:
        if seferFirst == sefer[0] or seferFirst == None and i != 4:
             pyautogui.leftClick(open[0] + 10, open[1] + 10)
             seferFirst = sefer[0]
             i + 1
             time.sleep(5)
        else:
            pyautogui.leftClick(reload[0] + 10, reload[1] + 10)
            seferFirst = None
            i = 0
            time.sleep(0.5)