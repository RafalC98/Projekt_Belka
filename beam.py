import tkinter as tk
from tkinter import Canvas
gui = tk.Tk()
gui.geometry("800x500")
gui.title("Beam Calculator")
var = tk.IntVar()

support = Canvas(gui)
fs_beam = Canvas(gui)
ovh_beam = Canvas(gui)
ln_beam = Canvas(gui)

#support
support.create_line(5, 5, 5, 50, 75, 50, 75, 5, 5, 5) #kwadrat
support.create_line(15, 30, 70, 30, width=2) #pozioma
support.create_line(15, 15, 15, 45, width=4) #pionowa
support.place(x = 10, y = 20)

#freely supported
fs_beam.create_line(5, 5, 5, 50, 75, 50, 75, 5, 5, 5) #kwadrat
fs_beam.create_line(15, 30, 65, 30, width=2) #pozioma
fs_beam.create_line(10, 40, 20, 40, 15, 30, 10, 40) #trojkat_l
fs_beam.create_line(60, 40, 70, 40, 65, 30, 60, 40) #trojkat_p
fs_beam.create_line(8, 40, 24, 40, width=2) #pozioma_m1
fs_beam.create_line(58, 44, 72, 44, width=2) #pozioma_m2
fs_beam.place(x = 10, y = 80)

#overhanging
ovh_beam.create_line(5, 5, 5, 50, 75, 50, 75, 5, 5, 5) #kwadrat
ovh_beam.create_line(15, 30, 70, 30, width=2) #pozioma
ovh_beam.create_line(10, 40, 20, 40, 15, 30, 10, 40) #trojkat_l
ovh_beam.create_line(45, 40, 55, 40, 50, 30, 45, 40) #trojkat_p
ovh_beam.create_line(8, 40, 24, 40, width=2) #pozioma_m1
ovh_beam.create_line(43, 44, 57, 44, width=2) #pozioma_m2
ovh_beam.place(x = 10, y = 140)

#line
ln_beam.create_line(15, 15, 15, 350, width=0.5) #pionowa
ln_beam.place(x = 260, y = 0)

radio1 = tk.Radiobutton(gui, text="bracket",variable = var, value=1)
radio1.place(x=90, y=40)
radio2 = tk.Radiobutton(gui, text="simply supported beam", variable = var, value=2)
radio2.place(x=90, y=98)
radio3 = tk.Radiobutton(gui, text="beam with overhang", variable = var, value=3)
radio3.place(x=90, y=156)

label1=tk.Label(gui,text="Lenght of beam/bracket in meters :")
label1.place(x=280,y=30)
lenght=tk.Entry(gui)
lenght.place(x=520,y=30)

label2=tk.Label(gui,text="Value of concentrated force in kN :")
label2.place(x=280,y=60)
force=tk.Entry(gui)
force.place(x=520,y=60)

label3=tk.Label(gui,text="Localization of force in m from left :")
label3.place(x=280,y=90)
force=tk.Entry(gui)
force.place(x=520,y=90)

label4=tk.Label(gui,text="Value of evenly distrib. load in kNm :")
label4.place(x=280,y=120)
load=tk.Entry(gui)
load.place(x=520,y=120)

# def moment_bracket(F,q,x,L):

def check():
    if var.get() == 1:
        print("opcja 1")
    elif var.get() == 2:
        print("opcja 2")
    elif var.get() == 3:
        print("opcja 3")





button=tk.Button(gui,text="Button",command=check)
button.place(x=5,y=220)
