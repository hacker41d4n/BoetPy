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

    def btn3():
        os.system("")

    def btn4():
        os.system("")
    
    def btn5():
        os.system("")

    def btn6():
        os.system("")

    def btn7():
        os.system("")

    def btn8():
        os.system("")

    def btn9():
        os.system("")

    def btn10():
        os.system("")
    
    def btn11():
        os.system("")

    def btn12():
        os.system("")

    def btn13():
        os.system("")
    
    def btn14():
        os.system("")

    def btn15():
        os.system("")
    
    def btn16():
        os.system("")
    
    def btn17():
        os.system("")
    





class Buttons:
    Button1 = Button (
        win,
        text="Update",
        command=Master.btn1
        
    )

    Button2 = Button (
        win,
        text="Upgrade",
        command=Master.btn2

    )

    Button3 = Button (
        win,
        text="Snapd",
        command=Master.btn3

    )

    Button4 = Button (
        win,
        text="",
        command=Master.btn4

    )

    Button5 = Button (
        win, 
        text="",
        command=Master.btn5

    )

    Button6 = Button (
        win,
        text="",
        command=Master.btn6

    )

    Button7 = Button (
        win,
        text="",
        command=Master.btn7

    )

    Button8 = Button (
        win,
        text="",
        command=Master.btn8

    )

    Button9 = Button (
        win,
        text="",
        command=Master.btn9

    )
    
    Button10 = Button (
        win,
        text="",
        command=Master.btn10

    )

    Button11 = Button (
        win, 
        text="",
        command=Master.btn11

    )

    Button12 = Button (
        win,
        text="",
        command=Master.btn12

    )

    Button13 = Button (
        win,
        text="",
        command=Master.btn13

    )

    Button14 = Button (
        win,
        text="",
        command=Master.btn14

    )

    Button15 = Button (
        win,
        text="",
        command=Master.btn15

    )
class Packs:
    Buttons.Button1.grid()

    Buttons.Button2.grid()

    Buttons.Button3.grid()

    Buttons.Button4.grid()

    Buttons.Button5.grid()

    Buttons.Button6.grid()

    Buttons.Button7.grid()

    Buttons.Button8.grid()

    Buttons.Button9.grid()

    Buttons.Button10.grid()

    Buttons.Button11.grid()

    Buttons.Button12.grid()

    Buttons.Button13.grid()

    Buttons.Button14.grid()
    
    Buttons.Button15.grid()

win.mainloop()