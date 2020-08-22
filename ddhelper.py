import sys
import os, time
from signal import signal, SIGINT

'''
   ___  __        __   __     ___
  / _ )/ /__  ___/ /__/ /_ __/ _ \___  ___ ___ 
 / _  / / _ \/ _  / _  / // / , _/ _ \(_-</ -_)
/____/_/\___/\_,_/\_,_/\_, /_/|_|\___/___/\__/ 
                      /___/

'''

"""
Copyright 2020 BloddyRose
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""
def handler(signal_received, frame):
    # Handle any cleanup here
    print("-" * 100)
    print("*" * 100)
    print('\tCTRL-C detected. Exiting gracefully')
    print("*" * 100)
    print("-" * 100)
    exit(0)


def run_dd():
    signal(SIGINT, handler)
    print("Starting lsblk -l ...")
    os.system("lsblk -l")
    device = str(input("Enter you usb name like (sdb, sdc): "))

    command = "/dev/"+device

    in_file = str(input("Enter path of iso file (/home/user/linux.iso): "))

    status = 'progress'
    cmd = f'xterm sudo dd if={in_file} of={command} status={status} & Xterm=$!'
    print("Running dd in xterm wait...")
    try:
        os.system(cmd)
        # os.system('kill $Xterm')
    except:
        print("Please type correct!! ")
    print("To stop please type (stop)!")
    response = str(input(">> "))
    if response == 'stop':
        os.system('kill $Xterm')

def help_menu():
    signal(SIGINT, handler)
    os.system("cat ./about/help_en.txt")
    print("*" * 100)
    ans = input("\nIf you have done reading press Enter to go back!!")
    if ans == "":
        os.system("clear")
        main_en()
    else:
        print("Only Enter accepts!!")
        os.system("clear")
        help_menu()

def main_en():
    signal(SIGINT, handler)
    print("Hello User this is simple python script to help with dd command on linux...")
    print("This script can make any linux os bootable for usb...")
    print("\n")
    print("Type (help) for how to use!")
    print("Write (start) to go!")
    print("Write (back) to go to main menu!")
    ans = str(input(">? "))
    if ans == 'start':
        os.system("clear")
        run_dd()
    elif ans == 'help': 
        os.system("clear")
        help_menu()
    elif ans == 'back':
        os.system("clear")
        main()
    else:
        print("Don\'t know that command")
        time.sleep(2)
        os.system("clear")
        main_en()





def run_dd_ro():
    signal(SIGINT, handler)
    print("Afisam unitatile de stocare cu lsblk -l ...")
    os.system("lsblk -l")
    device = str(input("Scrie numele usb (sdb, sdc): "))

    command = "/dev/"+device

    in_file = str(input("Scrie calea pana la imaginea iso(/home/user/linux.iso): "))

    status = 'progress'
    cmd = f'xterm sudo dd if={in_file} of={command} status={status} & Xterm=$!'
    print("Deschid un xterm cu dd ...")
    try:
        os.system(cmd)
        # os.system('kill $Xterm')
    except:
        print("Verifica de doua ori")
    print("Pentru a opri scrie (stop)!")
    response = str(input(">> "))
    if response == 'stop':
        os.system('kill $Xterm')

def help_menu_ro():
    signal(SIGINT, handler)
    os.system("cat ./about/help_ro.txt")
    print("*" * 100)
    ans = input("\nDaca ai terminat de citit apasa Enter!")
    if ans == "":
        os.system("clear")
        main_ro()
    else:
        print("Only Enter accepts!!")
        time.sleep(2)
        os.system("clear")
        help_menu_ro()

def main_ro():
    signal(SIGINT, handler)
    print("Buna utilizatorule acest script este scris pentru dd ")
    print("Script-ul poate face imagini linux bootable..")
    print("\n")
    print("Scrie (ajutor) pentru ajutor!")
    print("Scrie (incepe) pentru a incepe!")
    print("Scrie (inapoi) pentru a te intoarce inapoi!")
    ans = str(input(">? "))
    if ans == 'incepe':
        os.system("clear")
        run_dd_ro()
    elif ans == 'ajutor': 
        os.system("clear")
        help_menu_ro()
    elif ans == 'inapoi':
        os.system("clear")
        main()
    else:
        print("Nu stiu acesata comanda!")
        os.system("clear")
        main_ro()




        

def main():
    signal(SIGINT, handler)
    print("Select you language: 1. En or 2. Ro")


    ans = input(">> ")

    if ans == '1':
        os.system("cat ./about/intro_en.txt")
        ans = input("If you have done reading press Enter to go continue!! : ")
        if ans == "":
            os.system("clear")
            main_en()
        else:
            print("Only Enter accepts!!")

    elif ans == '2':
        os.system("cat ./about/intro_ro.txt")
        ans = input("Daca ai citit apasa Enter!! : ")
        if ans == "":
            os.system("clear")
            main_ro()
        else:
            print("Doar Enter!!")

        

main()
