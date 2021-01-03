import pyautogui
import subprocess
import time

p = subprocess.call(["C:\Program Files\AutoHotkey\AutoHotkey.exe", "bt.ahk"])
time.sleep(1/2)
pyautogui.press("tab")
time.sleep(1/2)
pyautogui.press("space")
pyautogui.hotkey('alt', 'f4')
p.kill()
