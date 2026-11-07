import tkinter as tk

class MenuBar(tk.Menu):

    def __init__(self, app):
        super().__init__(app.root)

        self.app = app

        self.file_menu = tk.Menu(self, tearoff=0)

        self.file_menu.add_command(label="New")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Save")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=app.root.destroy)

        self.add_cascade(label="File", menu=self.file_menu)

        app.root.config(menu=self)