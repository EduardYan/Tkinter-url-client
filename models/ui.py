"""
This module have the class UI
for make a interface.
"""

from tkinter import (Tk,
    Frame,
    Label,
    Entry,
    Text,
    Button,
    StringVar,
    END,
    Menu,
    Scrollbar,
    TclError
)

from requests.exceptions import MissingSchema, InvalidSchema, ConnectionError, ConnectTimeout, InvalidURL
from models.request import Request
from utils.messages import show_error, show_about
from utils.format import format_data_post
from errors.requests import DataInvalid


class UI:
    """
    Create a interface for show.
    """

    def __init__(self, window:Tk) -> None:
        # initials values for work
        self.window = window
        self.window.title('URL Client')
        self.window['background'] = '#222'
        # self.window.iconbitmap(r'./icons/icon.ico') # i can not this, jeje

        menu_bar = Menu(self.window, background = '#ccffcc')
        actions_menu = Menu(menu_bar, tearoff = 0, background = '#aaa', activebackground = '#777')
        actions_menu.add_command(label = 'GET', command = self.show_get)
        actions_menu.add_command(label = 'POST', command = self.show_post)
        actions_menu.add_command(label = 'PUT', command = self.show_put)
        actions_menu.add_command(label = 'DELETE', command = self.show_delete)
        actions_menu.add_command(label = 'Exit', command = lambda:self.window.destroy())

        help_bar = Menu(self.window, tearoff = 0, background = '#aaa', activebackground = '#777')
        help_bar.add_command(label = 'About', command = show_about)

        menu_bar.add_cascade(label = 'Actions', menu = actions_menu)
        menu_bar.add_cascade(label = 'Help', menu = help_bar)

        self.window['menu'] = menu_bar
        # frames for set the entries
        self.frame = Frame(width = 600, height = 600, background = '#222')
        self.frame.pack(side = 'left')

        self.frame2 = Frame(width = 600, height = 300, background = '#222')
        self.frame2.pack(side = 'right')

        self.show_get() # showing get for default


    def show_get(self) -> None:
        """
        Show the interface in case be a get request.
        """

        # removing the others
        self.frame.destroy()
        self.frame2.destroy()

        # frames for set the entries
        self.frame = Frame(width = 600, height = 600, background = '#222')
        self.frame.pack(side = 'left')

        self.frame2 = Frame(width = 600, height = 300, background = '#222')
        self.frame2.pack(side = 'right')

        self.title = Label(self.frame, text = 'Get Request', background = '#222')
        self.title['foreground'] = '#dddddd'
        self.title.grid(row = 0, column = 0, pady = 5)

        self.url_value = StringVar()
        entry_request = Entry(self.frame, textvariable = self.url_value)
        entry_request.grid(row = 1, column = 0, pady = 10, padx = 10)
        entry_request.focus() # setting the focus

        self.send_button = Button(self.frame, text = 'Send', cursor = 'hand2')
        self.send_button['command'] = lambda:self.make_request_get()
        self.send_button['background'] = '#777777'
        self.send_button['activebackground'] = '#999999'
        self.send_button.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = 'w')

        self.view_request = Text(self.frame2, width = 55, height = 13)
        self.view_request['insertbackground'] = '#222222'
        self.view_request['background'] = '#dddddd'
        self.view_request['font'] = 'sans-serif'
        self.view_request.grid(row = 0, column = 1, pady = 10, padx = 20)
        scrollVert = Scrollbar(self.frame2, command = self.view_request.yview, background = '#222', activebackground = '#444')
        scrollVert.grid(row = 0, column = 2, sticky = 'nsew')
        self.view_request.config(yscrollcommand = scrollVert.set)

        self.clear_button = Button(self.frame2, text = 'Clear')
        self.clear_button['command'] = lambda:self.clear_input()
        self.clear_button['background'] = '#777777'
        self.clear_button['activebackground'] = '#999999'
        self.clear_button.grid(row = 1, column = 1, pady = 5, padx = 20, sticky = 'w')

    def show_post(self) -> None:
        """
        Show the interface in case be a get request.
        """

        self.frame.destroy()
        self.frame2.destroy()

        # frames for set the entries
        self.frame = Frame(width = 600, height = 600, background = '#222')
        self.frame.pack(side = 'left')

        self.frame2 = Frame(width = 600, height = 300, background = '#222')
        self.frame2.pack(side = 'right')


        self.title = Label(self.frame, text = 'Post Request', background = '#222')
        self.title['foreground'] = '#dddddd'
        self.title.grid(row = 0, column = 0, pady = 5)

        self.url_value = StringVar()
        self.data_value = StringVar()
        self.entry_request = Entry(self.frame, textvariable = self.url_value)
        self.entry_request.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_request.focus() # setting the focus

        self.data_label = Label(self.frame, text = 'Data')
        self.data_label.grid(row = 2, column = 0, pady = 6, padx = 6)
        self.data_label['background'] = '#222222'
        self.data_label['foreground'] = '#dddddd'

        self.data_request = Entry(self.frame, textvariable = self.data_value)
        self.data_request.grid(row = 3, column = 0, pady = 10, padx = 10)


        self.send_button = Button(self.frame, text = 'Send', cursor = 'hand2')
        self.send_button['command'] = lambda:self.make_request_post()
        self.send_button['background'] = '#777777'
        self.send_button['activebackground'] = '#999999'
        self.send_button.grid(row = 4, column = 0, pady = 10, padx = 10, sticky = 'w')

        self.view_request = Text(self.frame2, width = 55, height = 13)
        self.view_request['insertbackground'] = '#222222'
        self.view_request['background'] = '#dddddd'
        self.view_request['font'] = 'sans-serif'
        self.view_request.grid(row = 0, column = 1, pady = 10, padx = 20)
        scrollVert = Scrollbar(self.frame2, command = self.view_request.yview, background = '#222', activebackground = '#444')
        scrollVert.grid(row = 0, column = 2, sticky = 'nsew')
        self.view_request.config(yscrollcommand = scrollVert.set)

        self.clear_button = Button(self.frame2, text = 'Clear')
        self.clear_button['command'] = lambda:self.clear_input()
        self.clear_button['background'] = '#777777'
        self.clear_button['activebackground'] = '#999999'
        self.clear_button.grid(row = 1, column = 1, pady = 5, padx = 20, sticky = 'w')

    def show_put(self) -> None:
        """
        Show the formulary for
        the put request.
        """

        self.frame.destroy()
        self.frame2.destroy()

        # frames for set the entries
        self.frame = Frame(width = 600, height = 600, background = '#222')
        self.frame.pack(side = 'left')

        self.frame2 = Frame(width = 600, height = 300, background = '#222')
        self.frame2.pack(side = 'right')


        self.title = Label(self.frame, text = 'Put Request', background = '#222')
        self.title['foreground'] = '#dddddd'
        self.title.grid(row = 0, column = 0, pady = 5)

        self.url_value = StringVar()
        self.data_value = StringVar()
        self.entry_request = Entry(self.frame, textvariable = self.url_value)
        self.entry_request.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_request.focus() # setting the focus

        self.data_label = Label(self.frame, text = 'Data')
        self.data_label.grid(row = 2, column = 0, pady = 6, padx = 6)
        self.data_label['background'] = '#222222'
        self.data_label['foreground'] = '#dddddd'

        self.data_request = Entry(self.frame, textvariable = self.data_value)
        self.data_request.grid(row = 3, column = 0, pady = 10, padx = 10)


        self.send_button = Button(self.frame, text = 'Send', cursor = 'hand2')
        self.send_button['command'] = lambda:self.make_request_put()
        self.send_button['background'] = '#777777'
        self.send_button['activebackground'] = '#999999'
        self.send_button.grid(row = 4, column = 0, pady = 10, padx = 10, sticky = 'w')

        self.view_request = Text(self.frame2, width = 55, height = 13)
        self.view_request['insertbackground'] = '#222222'
        self.view_request['background'] = '#dddddd'
        self.view_request['font'] = 'sans-serif'
        self.view_request.grid(row = 0, column = 1, pady = 10, padx = 20)
        scrollVert = Scrollbar(self.frame2, command = self.view_request.yview, background = '#222', activebackground = '#444')
        scrollVert.grid(row = 0, column = 2, sticky = 'nsew')
        self.view_request.config(yscrollcommand = scrollVert.set)

        self.clear_button = Button(self.frame2, text = 'Clear')
        self.clear_button['command'] = lambda:self.clear_input()
        self.clear_button['background'] = '#777777'
        self.clear_button['activebackground'] = '#999999'
        self.clear_button.grid(row = 1, column = 1, pady = 5, padx = 20, sticky = 'w')

    def show_delete(self) -> None:
        """
        Show the formulary for
        the delete request.
        """

        # removing the others
        self.frame.destroy()
        self.frame2.destroy()

        # frames for set the entries
        self.frame = Frame(width = 600, height = 600, background = '#222')
        self.frame.pack(side = 'left')

        self.frame2 = Frame(width = 600, height = 300, background = '#222')
        self.frame2.pack(side = 'right')

        self.title = Label(self.frame, text = 'Delete Request', background = '#222')
        self.title['foreground'] = '#dddddd'
        self.title.grid(row = 0, column = 0, pady = 5)

        self.url_value = StringVar()
        entry_request = Entry(self.frame, textvariable = self.url_value)
        entry_request.grid(row = 1, column = 0, pady = 10, padx = 10)
        entry_request.focus() # setting the focus

        self.send_button = Button(self.frame, text = 'Send', cursor = 'hand2')
        self.send_button['command'] = lambda:self.make_request_delete()
        self.send_button['background'] = '#777777'
        self.send_button['activebackground'] = '#999999'
        self.send_button.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = 'w')

        self.view_request = Text(self.frame2, width = 55, height = 13)
        self.view_request['insertbackground'] = '#222222'
        self.view_request['background'] = '#dddddd'
        self.view_request['font'] = 'sans-serif'
        self.view_request.grid(row = 0, column = 1, pady = 10, padx = 20)
        scrollVert = Scrollbar(self.frame2, command = self.view_request.yview, background = '#222', activebackground = '#444')
        scrollVert.grid(row = 0, column = 2, sticky = 'nsew')
        self.view_request.config(yscrollcommand = scrollVert.set)

        self.clear_button = Button(self.frame2, text = 'Clear')
        self.clear_button['command'] = lambda:self.clear_input()
        self.clear_button['background'] = '#777777'
        self.clear_button['activebackground'] = '#999999'
        self.clear_button.grid(row = 1, column = 1, pady = 5, padx = 20, sticky = 'w')


    def make_request_get(self) -> None:
        """
        Make the request getting the value
        of the entry.
        """

        url = self.url_value.get()

        try:
            request = Request(url, 'get')
            output_request = request.make({})

            # deleting the text for the new text
            self.view_request.delete('0.0', END)
            try:
                self.view_request.insert(END, output_request)

            except TclError:
                # in case the request have some specials characeters
                lines = output_request.split()
                for line in lines:
                    self.view_request.insert(END, line)

        # errors for controlling
        except InvalidURL:
            show_error('Invalid url for the request. Try again.')
        except MissingSchema:
            show_error('Missing a schema or protocol for the request. Not found. Verify the url.')

        except InvalidSchema:
            show_error('Schema invalid for the request. Try again and verify the url.')

        except ConnectionError:
            show_error(f'The connection for the url {url} was not made by connection problems. Verify your network or the url.')

        except ConnectTimeout:
            show_error('Request canceled for timeout. Try again.')


    def make_request_post(self) -> None:
        """
        Make the request getting the value
        of the entry.
        """

        url = self.url_value.get()
        data = self.data_value.get()

        try:
            request = Request(url, 'post')
            data = format_data_post(data)
            output_request = request.make(data)

            # deleting the text for the new text
            self.view_request.delete('0.0', END)
            self.view_request.insert(END, output_request)


        # errors for controlling
        except DataInvalid as e:
            show_error(e)

        except TypeError:
            show_error('Data is invalid')

        except InvalidURL:
            show_error('Invalid url for the request. Try again.')
        except MissingSchema:
            show_error('Missing a schema or protocol for the request. Not found. Verify the url.')

        except InvalidSchema:
            show_error('Schema invalid for the request. Try again and verify the url.')

        except ConnectionError:
            show_error(f'The connection for the url {url} was not made by connection problems. Verify your network or the url.')

        except ConnectTimeout:
            show_error('Request canceled for timeout. Try again.')

    def make_request_put(self) -> None:
        """
        Make the request in case be
        a put.
        """

        url = self.url_value.get()
        data = self.data_value.get()

        try:
            request = Request(url, 'put')
            data = format_data_post(data)
            output_request = request.make(data)

            # deleting the text for the new text
            self.view_request.delete('0.0', END)
            self.view_request.insert(END, output_request)


        # errors for controlling
        except DataInvalid as e:
            show_error(e)

        except TypeError:
            show_error('Data is invalid')

        except InvalidURL:
            show_error('Invalid url for the request. Try again.')
        except MissingSchema:
            show_error('Missing a schema or protocol for the request. Not found. Verify the url.')

        except InvalidSchema:
            show_error('Schema invalid for the request. Try again and verify the url.')

        except ConnectionError:
            show_error(f'The connection for the url {url} was not made by connection problems. Verify your network or the url.')

        except ConnectTimeout:
            show_error('Request canceled for timeout. Try again.')

    def make_request_delete(self) -> None:
        """
        Make the request in case be
        a delete.
        """

        url = self.url_value.get()

        try:
            request = Request(url, 'delete')
            output_request = request.make({})

            # deleting the text for the new text
            self.view_request.delete('0.0', END)
            self.view_request.insert(END, output_request)


        except InvalidURL:
            show_error('Invalid url for the request. Try again.')
        except MissingSchema:
            show_error('Missing a schema or protocol for the request. Not found. Verify the url.')

        except InvalidSchema:
            show_error('Schema invalid for the request. Try again and verify the url.')

        except ConnectionError:
            show_error(f'The connection for the url {url} was not made by connection problems. Verify your network or the url.')

        except ConnectTimeout:
            show_error('Request canceled for timeout. Try again.')


    def clear_input(self) -> None:
        """
        Clean the inputs of the entries and text.
        """

        self.view_request.delete('1.0', END)
