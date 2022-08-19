from tkinter import *
import os
def mainMenu():
    mainMenu = MainMenu(master=root)
    mainMenu.mainloop()

class Explorer(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        exitBtn = Button(master = self, text="Exit", width=25,command=self.exitUI)
        exitBtn.pack()
        self.master.title("File Manager Connections | Explorer")
        self.pack()
    def exitUI(self):
        self.destroy()
        mainMenu()

def filterFiles(fileList):
    filteredFiles = []
    for file in fileList:
        if file.split(".")[-1]!="fch":
            filteredFiles.append(file)
    return filteredFiles

class IndexBtn(Button):
    def __init__(self, master=None, file=None):
        Button.__init__(self, master=master,text=file,width=25,command=lambda:master.fileSelected(file))
        self.pack()

class Index(Frame):
    def __init__(self, master=None, file1Name = None):
        Frame.__init__(self, master)
        upBtn = Button(master = self, text="Up one folder", width = 25, command=self.upFolder)
        upBtn.pack()
        fileList = filterFiles(os.listdir())
        for fileItem in fileList:
            indexBtn = IndexBtn(master = self, file = fileItem)
        exitBtn = Button(master = self, text="Exit", width=25,command=self.exitUI)
        exitBtn.pack()
        self.master.title("File Manager Connections | Index")
        self.pack()
    def exitUI(self):
        self.destroy()
        mainMenu()
    def fileSelected(self,file):
        if len(file.split(".")) == 1:
            os.chdir("./"+file)
            self.destroy()
            indexUI = Index(master=root)
            indexUI.mainloop()
        else:
            if(self.file1Name != None):
                self.destroy()
            else:
                self.destroy()
            indexUI = Index(master=root,file1Name = file)
            indexUI.mainloop()
    def upFolder(self):
        os.chdir("..")
        self.destroy()
        indexUI = Index(master=root)
        indexUI.mainloop()

class MainMenu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        exploreBtn = Button(master = self, text="Explorer", width=25,command=self.exploreUIInit)
        exploreBtn.pack()
        indexBtn = Button(master = self, text="Index a File", width=25,command=self.indexUIInit)
        indexBtn.pack()
        self.master.title("File Manager Connections | Main Menu")
        self.pack()
    def exploreUIInit(self):
        self.pack_forget()
        explorerUI = Explorer(master=root)
        explorerUI.mainloop()
        self.pack()
    def indexUIInit(self):
        self.pack_forget()
        indexUI = Index(master=root)
        indexUI.mainloop()
        self.pack()

root = Tk()
root.geometry("600x400")
mainMenu()
root.destroy()