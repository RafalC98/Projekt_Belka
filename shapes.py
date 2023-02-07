import tkinter as tk
from tkinter import Canvas

gui = tk.Tk()
gui.title("Canvas")
gui.geometry("500x500")



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
