#Neelansh Mathur
# Run this script and keep it open. When playing a game,
# press n to autorun with the UP arrow key and m to stop.
# You can also stop by pressing the UP key again :)

# I originally made this for the online MMO game Tankionline,
# but it can be used for any game using arrow keys. You can also
# change the keys :)

import pyautogui as g
import keyboard as k

while True:
    if k.is_pressed('n'):
        g.keyDown('up')
    if k.is_pressed('m'):
        g.keyUp('up')