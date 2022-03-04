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
        os.system("apt install snapd -y")

    def btn4():
        os.system("snap install snap-store")
    
    def btn5():
        os.system("snap install spotify")

    def btn6():
        os.system("snap install audacity")

    def btn7():
        os.system("snap install VLC")

    def btn8():
        os.system("snap install obs-studio")

    def btn9():
        os.system("apt install simplescreenrecorder")

    def btn10():
        os.system("apt install libreoffice")
    
    def btn11():
        os.system("snap install teams")

    def btn12():
        os.system("apt install thunderbird")

    def btn13():
        os.system("snap install code --classic")
    
    def btn14():
        os.system("snap install gimp")

    def btn15():
        os.system("snap install telegram-desktop")
    
    def btn16():
        os.system("snap install discord")
    
    def btn17():
        os.system("snap install brave")
    
    def btn18():
        os.system("reboot")




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
        text="Snap-Store",
        command=Master.btn4

    )

    Button5 = Button (
        win, 
        text="Spotify",
        command=Master.btn5

    )

    Button6 = Button (
        win,
        text="Audacity",
        command=Master.btn6

    )

    Button7 = Button (
        win,
        text="VLC",
        command=Master.btn7

    )

    Button8 = Button (
        win,
        text="OBS",
        command=Master.btn8

    )

    Button9 = Button (
        win,
        text="SSR",
        command=Master.btn9

    )
    
    Button10 = Button (
        win,
        text="Office",
        command=Master.btn10

    )

    Button11 = Button (
        win, 
        text="Teams",
        command=Master.btn11

    )

    Button12 = Button (
        win,
        text="E-Mail",
        command=Master.btn12

    )

    Button13 = Button (
        win,
        text="VScode",
        command=Master.btn13

    )

    Button14 = Button (
        win,
        text="GIMP",
        command=Master.btn14

    )

    Button15 = Button (
        win,
        text="Telegram",
        command=Master.btn15

    )

    Button16 = Button (
        win,
        text="Discord",
        command=Master.btn16

    )

    Button17 = Button (
        win,
        text="Brave",
        command=Master.btn17

    )

    Button18 = Button (
        win,
        text="Reboot",
        command=Master.btn18

    )



class Packs:
    Buttons.Button1.grid(row=0, column=1,)

    Buttons.Button2.grid(row=0, column=2)

    Buttons.Button3.grid(row=0, column=3)

    Buttons.Button4.grid(row=0, column=4)

    Buttons.Button5.grid(row=0, column=5)

    Buttons.Button6.grid(row=1, column=1)

    Buttons.Button7.grid(row=1, column=2)

    Buttons.Button8.grid(row=1, column=3)

    Buttons.Button9.grid(row=1, column=4)

    Buttons.Button10.grid(row=1, column=5)

    Buttons.Button11.grid(row=2, column=1)

    Buttons.Button12.grid(row=2, column=2)

    Buttons.Button13.grid(row=2, column=3)

    Buttons.Button14.grid(row=2, column=4)
    
    Buttons.Button15.grid(row=2, column=5)

    Buttons.Button16.grid(row=3, column=1)

    Buttons.Button17.grid(row=3, column=2)

    Buttons.Button18.grid(row=3, column=3)

win.mainloop()