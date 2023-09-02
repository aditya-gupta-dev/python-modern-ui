from listPanel import ListPanel
from window import Window
from inputPanel import InputPanel

def main():
    window = Window(width=850, height=450)

    listPanel = ListPanel(window)
    inputPanel = InputPanel(window, listPanel)
    
    inputPanel.add()
    listPanel.add()
    window.show()
main()
