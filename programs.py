## Modules
from tkinter import *
import os

## Window
win = Tk()
win.title("BoetPy Programs")
win.minsize(width=400, height=400)
win["bg"]="#d70751"
f = ("Times bold", 14)

class Master:
    def btn1():
        os.system("apt update -y")

    def btn2():
        os.system("apt upgrade -y")

class Buttons:
    Button1 = Button (
        win,
        text="Update",
        command=Master.btn1
        
    )


class Packs:
    Buttons.Button1.grid()


win.mainloop()