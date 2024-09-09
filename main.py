from pynput.mouse import Button, Listener
from time import sleep
from datetime import datetime

counter_left, counter_right, counter_middle = 0, 0, 0
start_time = datetime.now()

def on_click(x, y, button, pressed):
    global counter_left
    global counter_right
    global counter_middle
    global start_time
    cur_time = datetime.now()

    if pressed:
        if button == Button.left:
            counter_left += 1
            return True

        elif button == Button.right:
            counter_right += 1
            return True

        elif button == Button.middle:
            counter_middle += 1
            return True

    print(f'Left clicks count = {counter_left}')
    print(f'Right clicks count = {counter_right}')
    print(f'Middle clicks count = {counter_middle}')
    print(f'CLicker works for {cur_time - start_time} now!')

listener = Listener(
    on_click=on_click,
)

listener.start()

while True:
    listener.wait()
    sleep(0.001)
