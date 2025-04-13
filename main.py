from pynput import keyboard

text = []

def on_press(key):
    try:
        text.append(key.char)
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

with open('log.txt', 'w') as f:
    for i in text:
        f.write(f"{i}\n")