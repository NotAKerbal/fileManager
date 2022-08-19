import os

def clear():
    #for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    #for Mac and Linux
    else:
        _ = os.system('clear')

def convToHidden(fileNameFull):
    fileSplit = fileNameFull.split("/")
    fileName = fileSplit.pop(-1)
    return "/".join(fileSplit) + "/." + fileName + ".fch"