import tkinter as tk
gui = tk.Tk()
gui.title("Beam Calculator")
var = tk.IntVar()

radio1 = tk.Radiobutton(gui, text="bracket",variable = var, value=1)
radio1.place(x=5, y=30)
radio2 = tk.Radiobutton(gui, text="simply supported beam", variable = var, value=2)
radio2.place(x=5, y=60)
radio3 = tk.Radiobutton(gui, text="beam with overhang", variable = var, value=3)
radio3.place(x=5, y=90)

label1=tk.Label(gui,text="Lenght of beam/bracket in meters:")
label1.place(x=200,y=30)
lenght=tk.Entry(gui)
lenght.place(x=400,y=30)

label2=tk.Label(gui,text="value of concentrated force in kN")
label2.place(x=200,y=60)
force=tk.Entry(gui)
force.place(x=450,y=60)

label3=tk.Label(gui,text="localization of force in meter from left")
label3.place(x=200,y=90)
force=tk.Entry(gui)
force.place(x=450,y=90)

label4=tk.Label(gui,text="value of evenly distributed load in kNm")
label4.place(x=200,y=120)
load=tk.Entry(gui)
load.place(x=450,y=120)

# def moment_bracket(F,q,x):

def check():
    if var.get() == 1:
        print("opcja 1")
    elif var.get() == 2:
        print("opcja 2")
    elif var.get() == 3:
        print("opcja 3")





button=tk.Button(gui,text="Button",command=check)
button.place(x=5,y=120)
