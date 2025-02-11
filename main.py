import tkinter as tk
from tkinter import PhotoImage
import pandas as  pd


window =tk.Tk(className=" Nicholas' Pokedex")
window.geometry("910x910")
backgroundimage = PhotoImage(file="./pokedexbackground.png")
image_label = tk.Label(window, image=backgroundimage)
image_label.place()

frm_reg_or_log = tk.Frame(window, width=910, height=910)

btn_register= tk.Button(frm_reg_or_log, text="Register", fg="Black",height=6,width=12,  )
btn_register.place(x=265, y=135)
frm_reg_or_log.pack()






window.mainloop()