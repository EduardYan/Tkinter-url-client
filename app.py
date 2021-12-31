"""
This is the principal for execute
the interface of the program.
"""

from tkinter import Tk
from models.ui import UI


if __name__ == '__main__':
    window = Tk()
    ui = UI(window)
    window.mainloop()
