import sqlite3
from contextlib import closing
import tkinter as tk
from jogo_da_forca import *
from banco_login import *

name_jogo = 'HANGMAN GAME'

class main(tk.Frame):
        
        def __init__(self, *args, **kwargs):
                tk.Frame.__init__(self, *args, **kwargs)

                self.img = tk.PhotoImage(file="imgs/image2.png")
                self.img = self.img.subsample(4, 4)

                self.background = tk.Label(image=self.img, bd=0)
                self.background.place(x=0, y=0)
                self.background.image = self.img
                
                self.login = Login(self)
                self.login.place(x=274, y=220)

if __name__ == '__main__':
        jogar = main()
        jogar.master.title(f"{name_jogo}")
        jogar.master.resizable(0, 0)
        jogar.master.geometry("800x572")
        jogar.master.mainloop()
 
