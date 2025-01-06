""" passwd_gen/models.py"""

from .constants import FieldTypes as FT
import tkinter as tk

from . import views as v

import argparse, secrets, random, string

class myPassPhrase():
    fields = {
        "Passphrase": {'req': True, 'type': FT.string}
    }
class myPasswordModel():
    fields = {
        "Password": {'req': True, 'type': FT.string},
    }
class myModel():
    fields = {
        # "Password": {'req': True, 'type': FT.string},
        "Total_lenght": {'req': True, 'type': FT.integer, 'min':8, 'max':30},#, "step":1},#, "tickinterval":10},#, "step":1},#, 'value': 8, "increment":1},
        "Special_characters":{'req':True, 'type': FT.boolean},
        "Include_numbers":{'req':True, 'type': FT.boolean},
        "Use_capital_letters":{'req':True, 'type': FT.boolean},
    }


    def generate(self, data):
        """
        Generate a random password based on the provided data.

        Args:
            data (dict): A dictionary containing parameters for password generation.
                - 'Total_lenght' (int): Desired length of the password (default is 8).
                - 'Special_characters' (bool): Whether to include special characters.
                - 'Include_numbers' (bool): Whether to include numeric digits.
                - 'Use_capital_letters' (bool): Whether to include uppercase letters.

        Returns:
            str: A randomly generated password adhering to the specified parameters.

        Raises:
            ValueError: If no characters are available for password generation.
        """


        total_length = data.get('Total_lenght', 8)

        use_special_chars = data.get("Special_characters", False)
        use_numbers = data.get("Include_numbers", False)
        use_capital_letters = data.get("Use_capital_letters", False)

        # Build the character pool
        char_pool = string.ascii_lowercase  # Always include lowercase letters
        if use_capital_letters:
            char_pool += string.ascii_uppercase
        if use_numbers:
            char_pool += string.digits
        if use_special_chars:
            char_pool += string.punctuation

        # Ensure the password is generated only if a valid character pool exists
        if not char_pool:
            raise ValueError("No characters available for password generation.")

        # Generate the password
        password = ''.join(secrets.choice(char_pool) for _ in range(total_length))

        return password
    
