import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Canvas
gui = tk.Tk()
gui.geometry("800x500")
gui.title("RM Beam Calculator")
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

var.set(0)
test = ['test1', 'test2', 'test3']

def changeState1():
    if var.get() !=0:

       label5.config(state="disabled")
       lenght2.config(state="disabled")

def changeState2():
    if var.get() !=0:

       label5.config(state="disabled")
       lenght2.config(state="disabled")


def changeState3():
    if var.get() !=0:

       label5.config(state="normal")
       lenght2.config(state="normal")

radio1 = tk.Radiobutton(gui, text="bracket", command=changeState1, variable = var, value=1)
radio1.place(x=90, y=40)
radio2 = tk.Radiobutton(gui, text="simply supported beam", command=changeState2, variable = var, value=2)
radio2.place(x=90, y=98)
radio3 = tk.Radiobutton(gui, text="beam with overhang", command=changeState3, variable = var, value=3)
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
x=tk.Entry(gui)
x.place(x=520,y=90)

label4=tk.Label(gui,text="Value of evenly distrib. load in kNm :")
label4.place(x=280,y=120)
load=tk.Entry(gui)
load.place(x=520,y=120)

label5=tk.Label(gui,text="Value of lenght overhang :")
label5.place(x=280,y=150)
lenght2=tk.Entry(gui)
lenght2.place(x=520,y=150)



Moment_label=tk.Label(gui,text="Maximum Value of moment: ")
Moment_label.place(x=280,y=200)

Shearforce_label=tk.Label(gui,text="Maximum Value of shear force: ")
Shearforce_label.place(x=280,y=220)

def moment_bracket(F,q,x,L):
    if x>L or x<L:
        F=0
        x=0
    M=-q*L*L/2 - F*x
    Moment_label.config(text="Maximum Value of moment: " +str(M))

def shearforce_bracket(F,q,x,L):
    if x>L or x<0:
        F=0
        x=0
    V=q*L+F
    Shearforce_label.config(text="Maximum Value of shear force: " +str(V))

def shear_force_fs(F,q,X,L):
    Rb = (F*X + L*0.5*L*q) / L
#     Ra = (-F*(L-X) - q*L*0.5*L) / L       #(!!!! ZWERYFIKOWAC !!!!)
    Ra = (F*(L-X) + q*L*0.5*L) / L          #(!!!! ZWERYFIKOWAC !!!!)

    print(Ra, Rb)
    B_Rb = abs(Rb)
    B_Ra = abs(Ra)

    if B_Rb > B_Ra:
        Max_Shear_force_fs_ = Rb
        Min_Shear_force_fs_ = Ra
        Shearforce_label.config(text="Maximum Value of shear force: " +str(Rb))
#         print("Max =", Max_Shear_force_fs_)
#         print("Min =",Min_Shear_force_fs_)
    else:
        Max_Shear_force_fs_ = Ra
        Min_Shear_force_fs_ = Rb
        Shearforce_label.config(text="Maximum Value of shear force: " +str(Ra))
#         print("Max =", Max_Shear_force_fs_)
#         print("Min =",Min_Shear_force_fs_)

def bending_moment_fs(F,q,X,L):
#     Ra = (-F*(L-X) - q*L*0.5*L) / L       #(!!!! ZWERYFIKOWAC !!!!)
    Ra = (F*(L-X) + q*L*0.5*L) / L          #(!!!! ZWERYFIKOWAC !!!!)

    if Ra > 0:
        M_max = (Ra*X-X*q*X*0.5)
        Moment_label.config(text="Maximum Value of moment: " +str(M_max))
    else:

        M_max = (abs(Ra)*X-X*q*X*0.5)
        M_max = -M_max
        Moment_label.config(text="Maximum Value of moment: " +str(M_max))

def check():

    try:
        F=int(force.get())
    except ValueError:
        F=0

    try:
        L=float(lenght.get())
    except ValueError:
        L=0

    try:
        X=float(x.get())
    except ValueError:
        X=0

    try:
        q=float(load.get())
    except ValueError:
        q=0

    if var.get() == 1:
        moment_bracket(F,q,X,L)
        shearforce_bracket(F,q,X,L)
        wspornik_wykres(F,q,X,L)

    elif var.get() == 2:
        shear_force_fs(F,q,X,L)
        bending_moment_fs(F,q,X,L)
        fs_wykres(F,q,X,L)
    elif var.get() == 3:
        print("opcja 3")


def wspornik_wykres(F,q,x,L):

    if x>L or x<0:
        F=0
        x=0

    RM=-q*L*L/2 - F*x
    l = np.linspace(0, L, 1000)
    X = []
    SF = []
    M = []

    # Spr??bowa?? zapisa?? za pomoc?? list comprehension

    for e in l:
        R=F+q*L
        if (e <= x and x != 0) or x == 0 :
            m =RM+R*e-q*e*e/2
            sf = R-q*e
        elif e > x and x != 0:
            m =RM+R*e-q*e*e/2-F*(e-x)
            sf = R-q*e-F
        M.append(m)
        X.append(e)
        SF.append(sf)


    plt.subplot(1,2,1) # poziomy,piony,index
    plt.plot(X, SF)
    plt.plot([0, L], [0, 0],linewidth=5)
    if x == L:
        plt.plot( [L, L], [0, F],[0,0],[0,R])
    elif x != L:
        plt.plot([0,0],[0,R])
    plt.title("SFD")
    plt.xlabel("Length in m")
    plt.ylabel("Shear Force")


    plt.subplot(1,2,2)
    plt.plot(X, M)
    plt.plot([0, L], [0, 0],linewidth=5)
    plt.plot([0,0],[0,RM])
    plt.title("BMD")
    plt.xlabel("Length in m")
    plt.ylabel("Bending Moment")
    plt.show()

def fs_wykres(F,q,x,L):


    if x>L or x<0:
        F=0
        x=0
    Rb = (F*x + L*0.5*L*q) / L
    Ra= (F*(L-x) + q*L*0.5*L) / L


    l = np.linspace(0, L, 1000)
    X = []
    SF = []
    M = []

    # Spr??bowa?? zapisa?? za pomoc?? list comprehension

    for e in l:

        if (e <= x and x != 0) or x == 0 :
            m =Ra*e-q*e*e/2
            sf = Ra-q*e
        elif e > x and x != 0:
            m =Ra*e-q*e*e/2-F*(e-x)
            sf = Ra-q*e-F
        M.append(m)
        X.append(e)
        SF.append(sf)


    plt.subplot(1,2,1) # poziomy,piony,index
    plt.plot(X, SF)
    plt.plot([0, L], [0, 0],linewidth=5)

    plt.plot( [L, L], [0, -Rb],[0,0],[0,Ra])

    plt.title("SFD")
    plt.xlabel("Length in m")
    plt.ylabel("Shear Force")


    plt.subplot(1,2,2)
    plt.plot(X, M)
    plt.plot([0, L], [0, 0],linewidth=5)
    plt.title("BMD")
    plt.xlabel("Length in m")
    plt.ylabel("Bending Moment")
    plt.show()


button=tk.Button(gui,text="Button",command=check)
button.place(x=5,y=220)

