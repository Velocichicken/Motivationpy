import os 
import time
import sys

if sys.platform == 'win32':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

wait = lambda t: time.sleep(t)

def main():
    menuoptions = ["welcome user,", "need some motivation? I understand.", "Press 1 for random motivation", "Press 2 for random motivational images"]
    clear()
    for viewmenu in menuoptions:
        print(viewmenu)



if __name__ == '__main__':
    main()