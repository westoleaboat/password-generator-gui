"""
passwd_gen/application.py: root window class
"""
import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m

import string

class Application(tk.Tk):  # subclase from Tk instead of Frame
    """Application root window. 
    Initialize the application window and set up the main interface.

    It needs to contain:
        - A title label
        - An instance of MyForm class (call and place form in GUI)

    """

    def __init__(self, *args, **kwargs):
        
        """
        creates an instance of the `myModel` class for managing the data model 
        and an instance of the `MyForm` class for the input form. 
        The form is placed on the window and event bindings for generating and 
        copying passwords are established.
        """

        super().__init__(*args, **kwargs)

        self.model = m.myModel()
        self.myform = v.MyForm(self, self.model)

        # window title
        self.title('Password Generator')
        self.geometry('350x320')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # header
        ttk.Label(  # parent is self. self is our Tk instance inside this class
            self, text='Header',
            font=("TkDefaultFont, 18")
        # ).grid(row=0
        )

        # Add form with widgets
        self.myform = v.MyForm(self, self.model)

        # place form
        self.myform.grid(row=1, padx=10, sticky=tk.W + tk.E)
        self.myform.bind('<<GeneratePassword>>', self._on_generate)
        self.myform.bind('<<CopyPassword>>', self._on_copy)


        self._on_generate() # trigger password generation when app starts

    def _on_copy(self, *_):
        """Copy password to clipboard"""
        string = self.myform._vars['Password'].get()
        self.clipboard_clear()
        self.clipboard_append(string)
        self.update()
        
    def _on_generate(self, *_):
        """
        Generate a password based on form input and update the display.

        This method retrieves data from the form, generates a password using the
        model, and updates the 'Password' field in the form with the generated
        password. The output field is temporarily activated to allow setting the 
        generated password and then disabled again.
        """

        # retrieve input
        data = self.myform.get()
        # get generated password from models.py
        output = self.model.generate(data)
        # activate output
        self.myform._disable_var.set(False)

        # set the password to the text widget
        self.myform._vars['Password'].set(output)

        # disable output
        self.myform._disable_var.set(True)
        # self.myform.set_output_state(tk.DISABLED)


if __name__ == "__main__":
    # create instance of our application and start its mainloop
    app = Application()
    app.mainloop()
