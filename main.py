from pynput.mouse import Button, Listener
from time import sleep

counter_left = 0
counter_right = 0
counter_middle = 0


def on_click(x, y, button, pressed):
    global counter_left
    global counter_right
    global counter_middle

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


listener = Listener(
    on_click=on_click,
)

listener.start()
while True:
    listener.wait()
    sleep(0.0001)
