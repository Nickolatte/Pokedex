import tkinter as tk
from tkinter import PhotoImage
window =tk.Tk(className=" Nicholas' Pokedex")
window.geometry("900x675")

backgroundimage = PhotoImage(file="pokedexbackground.png")
image_label = tk.Label(window, image=backgroundimage)
image_label.place(x=0,y=0)

login_lbl = tk.Label(text="Login", bg="#ee5351", fg="white" ,width="20")
login_lbl.grid(row=0, column=0,sticky="nsew", padx=10, pady=10 )

name_lbl =tk.Label(text="Name", bg="#ee5351", fg="white" ,width="20")
name_lbl.grid(row=0, column=1,sticky="nsew", padx=10, pady= 10)

name_ent =tk.Entry()
name_ent.grid(row=0, column=2,sticky="nsew", padx=10, pady= 10)

password_lbl = tk.Label(text="Password", bg="#ee5351", fg="white" ,width="20")
password_lbl.grid(row=1, column=1,sticky="nsew", padx=10, pady= 10)

password_ent = tk.Entry()
password_ent.grid(row=1, column=2,sticky="nsew", padx=10, pady= 10)

window.mainloop()