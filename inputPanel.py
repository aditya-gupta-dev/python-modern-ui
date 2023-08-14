import customtkinter
from window import Window
from listPanel import ListPanel

class InputPanel:

    def click_listener_for_search_button(self):
        print("clicked")

    def __init__(self, window: Window, listPanel: ListPanel):
        self.listPanel = listPanel
        self.panel = customtkinter.CTkFrame(window.get(), width=window.get_width()-20, height=70)
        self.search_button = customtkinter.CTkButton(self.panel, text="search", width=90, height=50, command=self.click_listener_for_search_button)
        self.textField = customtkinter.CTkEntry(self.panel, width=700, height=50)
        
        self.search_button.place(x=self.textField._current_width+30, y=10)
        self.textField.place(x=10,y=10)

    def add(self,x_pos=10,y_pos=10):
        self.panel.place(x=x_pos,y=y_pos)


