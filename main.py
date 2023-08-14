from listPanel import ListPanel
from window import Window
from inputPanel import InputPanel

def main():
    window = Window()

    listPanel = ListPanel(window)
    inputPanel = InputPanel(window, listPanel)
    
    inputPanel.add()
    listPanel.add()
    window.show()
main()
