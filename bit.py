from microbit import *

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
pos = 0

display.show(ascii_lowercase[pos])

while True:
    if button_a.is_pressed():
        pos += 1
        display.show(ascii_lowercase[pos])
        sleep(500)
    if button_b.is_pressed():
        pos -= 1
        display.show(ascii_lowercase[pos])
        sleep(500)
