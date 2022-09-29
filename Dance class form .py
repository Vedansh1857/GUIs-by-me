from tkinter import *

root = Tk()
root.geometry("455x333")

label = Label(root, text="!!!___Vedansh Dance Classes___!!!", font=50, fg="red", bg="black")
label.grid()

def details():
    with open('data.txt', 'w') as f:
        f.write(f"Name is --> {nameval.get()}\n")
        # f.write('/n')
        f.write(f"Age is --> {ageval.get()}\n")
        # f.write("/n")
        f.write(f"Adress is --> {adressval.get()}\n")
        # f.write("/n")
        f.write(f"Contact No. is --> {phoneval.get()}")
        # f.write("/n")

l1 = Label(root, text="Name")
l1.grid(row=7, column=0)
l2 = Label(root, text="Age")
l2.grid(row=8, column=0)
l3 = Label(root, text="Address")
l3.grid(row=9, column=0)
l4 = Label(root, text="Phone No.")
l4.grid(row=10, column=0)

nameval = StringVar()
ageval = IntVar()
adressval = StringVar()
phoneval = IntVar()

Entry(root, textvariable=nameval, bg="blue", fg="white").grid(row=7, column=1)
Entry(root, textvariable=ageval, bg="blue", fg="white").grid(row=8, column=1)
Entry(root, textvariable=adressval, bg="blue", fg="white").grid(row=9, column=1)
Entry(root, textvariable=phoneval, bg="blue", fg="white").grid(row=10, column=1)

b = Button(root, text="Submit", font=20, bg="green", fg="yellow", command=details)
b.grid(pady=10, padx=50)
# On clicking the submit button thye details will be get written down on a text file data.txt

root.mainloop()