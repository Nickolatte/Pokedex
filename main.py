# imports for the start
import customtkinter as ctk # pip install customtkinter
from tkinter import PhotoImage

from PIL import Image, ImageTk , ImageFont #pip install Pillow
import pyglet,tkinter

pyglet.font.add_file('PokemonGb-RAeo.ttf')

# Class for the main menu
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nicholas' Pokedex")
        self.geometry("900x900")




        # background image 
        self.background_image = Image.open("pokdexmainbg.png")
        self.tk_image = ImageTk.PhotoImage(self.background_image)
        background_label = ctk.CTkLabel(self, image=self.tk_image, text="")
        background_label.pack(pady=20)

        # title text
        #self.image1 = Image.open("pokemon-gb.png")
        #self.tk_image1 = ImageTk.PhotoImage(self.image1)
        label1 = ctk.CTkLabel ( self,text="test", width=150, height= 100 ,fg_color="#ee5351", font =('PokemonGb-RAeo', 20))

    
        label1.pack(pady=10)
        label1.place(relx=0.5, rely=0.1, anchor='center')




# Initialize and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()


















