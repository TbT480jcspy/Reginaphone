import tkinter as tk
from classes.MenuBar import MenuBar
from classes.Toolbar import Toolbar
from classes.TonePlayer import TonePlayer


class Application:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Reginaphone")
        self.root.geometry("1200x800")
        self.root.minsize(900, 600)

        self.menu_bar = MenuBar(self)
        self.toolbar = Toolbar(self)

        

    def run(self):
        player = TonePlayer()
        
        player.play_frequency(500)

        self.root.mainloop()