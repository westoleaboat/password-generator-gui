"""
passwd_gen/views.py: form containing widgets
"""

import tkinter as tk
from tkinter import ttk

from . import widgets as w
from .constants import FieldTypes as FT

import customtkinter

class MyPassPhrase(tk.Frame):
    """Input Form for widgets

    - self._vars = Create a dictionary to hold all out variable objects 
    - _add_frame = instance method that add a new label frame. Pass in 
                   label text and optionally a number of columns.

    """

    var_types = {
        FT.string: tk.StringVar,
        FT.string_list: tk.StringVar,
        FT.short_string_list: tk.StringVar,
        FT.iso_date_string: tk.StringVar,
        FT.long_string: tk.StringVar,
        FT.decimal: tk.DoubleVar,
        FT.integer: tk.IntVar,
        FT.integer2: tk.IntVar,
        FT.boolean: tk.BooleanVar
    }

    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, parent, model, *args, **kwargs):
        """
        Initialize the form.

        This method creates all the widgets and sets up the layout.

        :param parent: The parent widget.
        :param model: The model containing the data and field specs.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.model = model
        #self.settings = settings
        fields = self.model.fields

        self._vars = {  # hold all variable objects
            key: self.var_types[spec['type']]()
            for key, spec in fields.items()
        }

        # for var_name, var_instance in self._vars.items():
        #     var_instance.trace("w", lambda *args, name=var_name: self._on_change(name))

        # disable var for Output field
        self._disable_var = tk.BooleanVar()

        
        # build the form
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        label = ttk.Label(self, text='Coming Soon')
        label.grid(sticky=tk.W + tk.E, columnspan=3, row=0, column=0)
        

        self._disable_var.set(True)

        # text to display data from form
        self.output_var = tk.StringVar()


class MyPassword(tk.Frame):
    """Input Form for widgets

    - self._vars = Create a dictionary to hold all out variable objects 
    - _add_frame = instance method that add a new label frame. Pass in 
                   label text and optionally a number of columns.

    """

    var_types = {
        FT.string: tk.StringVar,
        FT.string_list: tk.StringVar,
        FT.short_string_list: tk.StringVar,
        FT.iso_date_string: tk.StringVar,
        FT.long_string: tk.StringVar,
        FT.decimal: tk.DoubleVar,
        FT.integer: tk.IntVar,
        FT.integer2: tk.IntVar,
        FT.boolean: tk.BooleanVar
    }

    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, parent, model, *args, **kwargs):
        """
        Initialize the form.

        This method creates all the widgets and sets up the layout.

        :param parent: The parent widget.
        :param model: The model containing the data and field specs.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.model = model
        #self.settings = settings
        fields = self.model.fields

        self._vars = {  # hold all variable objects
            key: self.var_types[spec['type']]()
            for key, spec in fields.items()
        }

        # for var_name, var_instance in self._vars.items():
        #     var_instance.trace("w", lambda *args, name=var_name: self._on_change(name))

        # disable var for Output field
        self._disable_var = tk.BooleanVar()

        
        # build the form
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        # passwd_frame = self._add_frame('')

        w.LabelInput(
            self,
            label=None,
            field_spec=fields['Password'],
            var=self._vars['Password'],
            input_class=w.BoundText,
            disable_var=self._disable_var,
            input_args={'height': 1, 'width': 30,}    
        ).grid(sticky=tk.W + tk.E, row=0, column=0)

        self._disable_var.set(True)

        # text to display data from form
        self.output_var = tk.StringVar()

        ###########
        # buttons #
        ###########

        buttons = ttk.Frame(self)  # add on a frame
        buttons.grid(sticky=tk.W + tk.E, row=0, column=1, padx=10, pady=(0, 17))
        # pass instance methods as callback commands

        self.copybutton = ttk.Button(
            buttons, text="Copy", command=self._on_copy,width=5)
        self.copybutton.grid(row=0, column=1)#, padx=(10,0))#, pady=(0, 17))

        self.generatebutton = ttk.Button(
            buttons, text="New", command=self._on_generate, width=5)
        self.generatebutton.grid(row=0, column=2)#, padx=(0,10))#, pady=(0, 17))

    def _on_copy(self):
        self.event_generate('<<CopyPassword>>')

    def _on_generate(self):
        self.event_generate('<<GeneratePassword>>')

class MyForm(tk.Frame):
    """Input Form for widgets

    - self._vars = Create a dictionary to hold all out variable objects 
    - _add_frame = instance method that add a new label frame. Pass in 
                   label text and optionally a number of columns.

    """

    var_types = {
        FT.string: tk.StringVar,
        FT.string_list: tk.StringVar,
        FT.short_string_list: tk.StringVar,
        FT.iso_date_string: tk.StringVar,
        FT.long_string: tk.StringVar,
        FT.decimal: tk.DoubleVar,
        FT.integer: tk.IntVar,
        FT.integer2: tk.IntVar,
        FT.boolean: tk.BooleanVar
    }

    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E, columnspan=2, padx=10, pady=(0,10))
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, parent, model, *args, **kwargs):
        """
        Initialize the form.

        This method creates all the widgets and sets up the layout.

        :param parent: The parent widget.
        :param model: The model containing the data and field specs.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """
        super().__init__(parent, *args, **kwargs)

        self.model = model
        #self.settings = settings
        fields = self.model.fields

        self._vars = {  # hold all variable objects
            key: self.var_types[spec['type']]()
            for key, spec in fields.items()
        }

        for var_name, var_instance in self._vars.items():
            var_instance.trace("w", lambda *args, name=var_name: self._on_change(name))

        # disable var for Output field
        self._disable_var = tk.BooleanVar()

        
        # build the form
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        options_frame = self._add_frame('Options')

        w.LabelInput(
            self,
            '',
            field_spec=fields['Total_lenght'], # Spinbox
            var=self._vars['Total_lenght'],
            input_args={'from_': 8, 'to': 30, "width": 2}
        ).grid(sticky=tk.W + tk.E, row=0, column=1, padx=(0,10), pady=(10,0))

        self._vars['Total_lenght'].set(12)

        w.LabelInput(
            self,
            "Lenght",
            var=self._vars['Total_lenght'],
            # input_class=customtkinter.CTkSlider,
            input_class=tk.Scale,
            input_args={'from_': 8, 'to': 30, 'orient':'horizontal', 'tickinterval':2},
            # field_spec=fields['Total_lenght'],
        ).grid( row=0, column=0, pady=(10,0), padx=(10,0))#, padx=10, pady=(10,0))

        options_frame = self._add_frame('Character Types')

        w.LabelInput(
            options_frame,
            "Capital Letters (A-Z)",
            field_spec=fields['Use_capital_letters'],
            var=self._vars['Use_capital_letters'],
        ).grid(sticky=tk.W + tk.E, row=3, column=0, padx=10,pady=(10,0))
        
        w.LabelInput(
            options_frame,
            "Include Numbers (0-9)",
            field_spec=fields['Include_numbers'],
            var=self._vars['Include_numbers'],
        ).grid(sticky=tk.W + tk.E, row=4, column=0, padx=10)

        w.LabelInput(
            options_frame,
            "Special Characters (/ * + & ...)",
            field_spec=fields['Special_characters'],
            var=self._vars['Special_characters'],
        ).grid(sticky=tk.W + tk.E, row=5, column=0, padx=10)
        


        self._disable_var.set(True)

        # text to display data from form
        self.output_var = tk.StringVar()

        ###########
        # buttons #
        ###########

        buttons = ttk.Frame(self)  # add on a frame
        buttons.grid(sticky=tk.W + tk.E, row=4)
        # pass instance methods as callback commands

    def reset(self):
        """Reset entries. Set all variables to empty string"""
        # activate widget
        self._disable_var.set(False)
        # self.set_output_state(tk.NORMAL)

        # reset data
        for var in self._vars.values():
            if isinstance(var, tk.BooleanVar):
                # uncheck checkbox
                var.set(False)
            else:
                # set inputs to empty string
                var.set('')
                # set data label to empty string
                # self.output_var.set('')
        # disable widget
        self._disable_var.set(True)
        # self.set_output_state(tk.DISABLED)

    def get(self):
        """Retrieve data from the form so it can be saved or used"""
        # data = {}
        data = dict()
        for key, variable in self._vars.items():
            try:
                # retrieve from ._vars
                data[key] = variable.get()
            except tk.TclError as e:
                # create error message
                message = f'Error in field: {key}. Data not saved!'
                raise ValueError(message) from e
        # return the data
        return data


    def _on_change(self, var_name, *args):
        """
        Triggered when the slider value changes. Updates the password length and
        regenerates the password in real time.
        """
        # value = self._vars['Total_lenght'].get()
        self.event_generate('<<GeneratePassword>>')

    def on_scale_change(value, var, step=1):
        # Round the scale value to the nearest multiple of the step
        rounded_value = round(float(value) / step) * step
        var.set(rounded_value)

    #########################################
    # Disable widget if disable_var not used:
    #
    # def set_output_state(self, state):
    #     output_widget = self._get_widget_by_var(self._vars['Output'])
    #     if output_widget:
    #         output_widget.input.configure(state=state)

    # def _get_widget_by_var(self, var):
    #     """Return the widget associated with a given variable."""
    #     for widget in self.winfo_children():
    #         if isinstance(widget, w.LabelInput) and widget.variable == var:
    #             return widget
    #     return None
    #########################################
