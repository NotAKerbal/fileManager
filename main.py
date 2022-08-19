import platform
from helper import *
from index import index
from explorer import explore
def mainMenu():
    clear()
    print("Connection File Manager - Running On",platform.system())
    print("[1] Explore")
    print("[2] Index a File")
    print("[3] Tags")
    print("")
    print("[0] Exit")
    print("Selection: ", end = "")
    selection = input()
    if selection == "1":
        explore("./main.py")
    if selection == "2":
        index()
    
    if selection == "0":
        exit()

while(True):
    mainMenu()