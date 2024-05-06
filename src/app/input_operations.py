from pyautogui import keyUp, keyDown, hotkey
import mouse

def hold_key(key):
    keyDown(key)

def release_key(key):
    keyUp(key)

def single_key_press(key, is_pressed):
    if not is_pressed:
        keyDown(key)
        keyUp(key)

def hold_mb(mb, release):
    if not release:
        mouse.press(button=mb)
    else:
        mouse.release(button=mb)


def single_mb_press(mb, status):
    if not status:
        mouse.click(button=mb)
        mouse.release(button=mb)

# is_left_mb_pressed = False
# is_right_mb_pressed = False
# release_left_mb = False
# release_right_mb = False

# time.sleep(2)

# hold_mb("left", release_left_mb)

# time.sleep(2)

# release_left_mb = True

# hold_mb("left", release_left_mb)