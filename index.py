from helper import *
from console_explorer import *
from explorer import explore
def addCon(fileNameFull,connectionPath,connection):
    f = open(convToHidden(fileNameFull), "a")
    f.write(connectionPath + "; " + connection + '\n')
    f.close()

def defineConnection(fileNameFull):
    clear()
    fileName = fileNameFull.split("/")[-1]
    print("What connections does the file",fileName,"have?")
    fileNameFull2 = browse_for_file(existence_required=True,cancel_enabled=True)
    if fileNameFull2 != None:
        fileName2 = fileNameFull2.split("/")[-1]
        clear()
        print("What connection does the file",fileName2,"have with",fileName + "?")
        connection = input()
        addCon(fileNameFull,fileNameFull2,connection)
        addCon(fileNameFull2,fileNameFull,connection)
        print("Would you like to keep adding connections?")
        answer = input()
        if answer is 'y':
            defineConnection(fileNameFull)
        else:
            explore(fileNameFull)
def index():
    clear()
    print("File Indexing UI")
    fileNameFull = browse_for_file(existence_required=True)
    if fileNameFull != None:
        fileName = fileNameFull.split("/")[-1]
        print("Selected", fileName)
        defineConnection(fileNameFull)