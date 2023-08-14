import customtkinter
from window import Window

class ListPanel:
    def __init__(self, window: Window):
        self.frame = customtkinter.CTkFrame(window.get(), width=window.get_width()-20, height=340)

        ListPanelItem(self, "ospnop").add(y_pos=10)
        y = 80
        for x in range(10):
            ListPanelItem(self, "poasda").add(y_pos=y)
            y = y + 70
        
    def add(self, location = [10,100]):
        self.frame.place(x=location[0],y=location[1])

class ListPanelItem:
    def __init__(self, listPanel: ListPanel, song: str):
        self.frame = customtkinter.CTkFrame(listPanel.frame, width=810, height=50)

        self.text = customtkinter.CTkLabel(self.frame, text=song)
        self.button = customtkinter.CTkButton(self.frame, text="Download")
        
        self.text.place(x=20,y=10)
        self.button.place(x=650,y=10)

    def add(self, y_pos=10):
        self.frame.place(x=10,y=y_pos)

    def set_song_name(self, song_name: str):
        self.text._text = song_name    

