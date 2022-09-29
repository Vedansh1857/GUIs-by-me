from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Sliders quiz")

def rate():
    rates = ratings.get()

    if rates <= 5:
        with open ('rating.txt', 'a') as f:
            f.write(f"Experience shared by the customer is --> {ratings.get()}\n ")

        tmsg.showinfo(title="Rating area", message="Please tell us wht was wrong")
        print("We will surely not give any chance of any complaint next time")
        
    else:
        with open ('rating.txt', 'a') as f:
            f.write(f"Experience shared by the customer is --> {ratings.get()}\n ")
        
        response = tmsg.askyesnocancel(title="Rating area", message="Thanks for ur feedback... Would u like to recommend others also of this restaurant?")
        if response == True:
            tmsg.showinfo(title="We are glad to hear frm you dear customer", message="We will be very grateful to you Sir/Mam")         
        elif response == False:
            tmsg.showinfo(title="We are glad to hear frm you dear customer", message="As you wish Sir/Mam")
        else:
            quit()

Label(root, text="Khana Khazana Restaurant", font="roboto 25 bold").pack()
Label(root, text="Please share ur ratings", font="comicsansms 10 italic").pack()
ratings = Scale(root, from_=0, to=10, orient=HORIZONTAL)
ratings.pack()
Button(root, text="Submit", command=rate).pack(pady=15)

root.mainloop()