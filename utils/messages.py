"""
This module have somes
funtions for show messages
in case of errors or others, in the interface.
"""

from tkinter.messagebox import showinfo, showerror
from models.message import Message

title = 'URL Client'

def show_error(message:str) -> None:
    """
    Show the message passed for parameter in case
    the connection is bad. Or others.
    """

    # creating a message
    message = Message(message)
    showerror(title, message.content) # showing

def show_about() -> None:
    """
    Show the message for the about.
    """

    # showing
    showinfo(title, 'This is a application for make request GET, POST, PUT and DELETE quiclky. Maked with python and your module tkinter. Error or bugs email to eduarygp@gmail.com')
