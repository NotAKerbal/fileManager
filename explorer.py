from helper import *

def cexplore(filePath):
    hFilePath = convToHidden(filePath)
    f = open(hFilePath, "r")
    line = f.readline()
    lines = []
    i = 2
    print("[1] Add Connection")
    print("[2] Open File")
    while line != "":
        lines.append(line)
        i = i + 1
        sLine = line.split("; ")
        print("[" + str(i) + "]",sLine[0].split("/")[-1], "--", sLine[1], end="")
        line = f.readline()
    f.close()
    print('\n' + "[0] EXIT")
    print('\n' + "Respnose:", end="")
    selStr = input()
    clear()
    if selStr.isnumeric():
        selInt = int(selStr)
        selInt2 = selInt - 3
        if selInt2 >= 0:
            if selInt2 < len(lines):
                print("Explorer -",lines[selInt2].split("; ")[0].split("/")[-1])
                cexplore(lines[selInt2].split("; ")[0])
            else:
                print("Number not Valid")
                explore(filePath)
        elif selInt == 1:
            from index import defineConnection
            defineConnection(filePath)
        elif selInt == 2:
            import webbrowser
            print('\n' + "Opening in external application")
            if platform == "darwin":  # check if on OSX
                filePath = "file:///" + file_location
            webbrowser.open(filePath)
            explore(filePath)
    else:
        explore(filePath)
def explore(filePath):
    clear()
    print("Explorer -",filePath.split("/")[-1])
    cexplore(filePath)