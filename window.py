from customtkinter import CTk
import customtkinter

class Window:
    def __init__(self, width=850, height=450) -> None:
        customtkinter.set_appearance_mode('Dark')
        self.root = CTk()
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}')

    def get_width(self):
        return self.root._current_width 
    
    def get_height(self):
        return self.root._current_height

    def show(self):
        self.root.mainloop()

    def get(self):
        return self.root

