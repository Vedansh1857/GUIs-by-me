from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
import os

if __name__ == '__main__':
    root = Tk()
    root.geometry("644x788")
    root.title("Text editor in tkinter")
    root.wm_iconbitmap("1.ico")

    def newFile():
        global file
        root.title("Untitled - Notepad")
        file = None
        mytext.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),("Text documents", "*.txt")])
        if file == "":
            file == None
        else:
            root.title(os.path.basename(file) + "-Notepad")
            mytext.delete(1.0, END)
            f = open(file, "r")
            mytext.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file == None:
            file = asksaveasfile(initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"),("Text documents", "*.txt")])
            
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(mytext.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + "- Notepad")

        else:
            f = open(file, "w")
            f.write(mytext.get(1.0, END))
            f.close()

    def quitApp():
        # quit()
        root.destroy()

    def cut():
        mytext.event_generate(("<<Cut>>"))

    def copy():
        mytext.event_generate(("<<Copy>>"))

    def paste():
        mytext.event_generate(("<<Paste>>"))

    def about():
        showinfo(title="Notepad", message="Notepad by Vedu Bhai")

    mytext = Text(root, font="lucida 13")
    mytext.pack(fill=BOTH, expand=True)

    file = None

    # Creating File menu:
    menu = Menu(root)
    Filemenu = Menu(menu, tearoff=0)

    # Tp open new file
    Filemenu.add_command(label="New", command=newFile)

    # To open already existing file
    Filemenu.add_command(label="Open", command=openFile)

    # To save a current file
    Filemenu.add_command(label="Save", command=saveFile)
    Filemenu.add_separator()

    # To exit from the notepad
    Filemenu.add_command(label="Exit", command=quitApp)
    menu.add_cascade(label="File", menu=Filemenu)

    # Creating a Edit menu:
    Editmenu = Menu(menu, tearoff=0)

    # To cut, copy & paste:
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)
    menu.add_cascade(label="Edit", menu=Editmenu)

    # Creating a Help menu:
    Helpmenu = Menu(menu, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)
    menu.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=menu)

    scroll = Scrollbar(mytext)
    scroll.pack(fill=Y, side=RIGHT)
    scroll.config(command=mytext.yview)
    mytext.config(yscrollcommand=scroll.set)

root.mainloop()