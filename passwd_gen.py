""" passwd_gen.py: Password Generator GUI

The code is organized in the following classes:

    -BoundText: Text widget with a bound variable
    -LabelInput: Widget containing a label and input together
    -MyForm: Input form for widgets
    -Application: Application root window


Author: Tomas C. 
"""


from passwd_gen.application import Application

app = Application()
app.mainloop()
