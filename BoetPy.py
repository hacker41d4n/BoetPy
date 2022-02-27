## Modules
from tkinter import *



## Window
win = Tk()
win.title("BoetPy")
win.minsize(width=400, height=400)
win["bg"]="#d70751"
f = ("Times bold", 14)



## Center Title
Label (
    win,
    text="BoetPy",
    padx=20,
    pady=20,
    bg="#d70751",
    font=f,
).pack(expand=True, fill=BOTH)




## Program Button
def nextPage():
    win.destroy()
    import programs

Button(
    win, 
    text="Programs", 
    font=f,
    bg="#2496ed",
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)


win.mainloop()