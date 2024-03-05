#! python3
# looking_busy.py - will slightly nudge the cursor to prevent from looking idle
"""
Many instant messaging programs determine whether you are idle, or away from your
computer, by detecting a lack of mouse movement over some period of time—say,
ten minutes. Maybe you’d like to sneak away from your desk for a while but don’t
want others to see your instant messenger status go into idle mode. Write a script
to nudge your mouse cursor slightly every ten seconds. The nudge should be small
enough so that it won’t get in the way if you do happen to need to use your computer
 while the script is running.
"""
import pyautogui
import random
import time

random_movements = [
    (0, 1),     # up
    (0, -1),    # down
    (-1, 0),    # left
    (1, 0)      # right
]

# time.sleep(10) seconds will allow it to randomly move every 10 secons until
# the user ends the program themselves.
try:
    while True:
        time.sleep(10)
        pyautogui.moveRel(random.choice(random_movements))
except (KeyboardInterrupt, pyautogui.FailSafeException):
    print('Program finished.')
    