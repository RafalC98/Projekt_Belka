import tkinter as tk
gui = tk.Tk()
gui.title("Beam Calculator")
var = tk.IntVar()
radio1 = tk.Radiobutton(gui, text="bracket", variable = var, value=1).place(x=5, y=30)
radio2 = tk.Radiobutton(gui, text="Option 2", variable = var, value=2).place(x=5, y=60)
radio3 = tk.Radiobutton(gui, text="Option 3", variable = var, value=3).place(x=5, y=90)

def check():
    if var.get() == 1:
        print("opcja 1")
    elif var.get() == 2:
        print("opcja 2")
    elif var.get() == 3:
        print("opcja 3")

button=tk.Button(gui,text="Button",command=check)
button.place(x=5,y=120)
