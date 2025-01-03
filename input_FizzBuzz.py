# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Module input_FizzBuzz.py
# Author:      Štefan Masič
# Date:        1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# Libraries:
import keyboard
# -------------------------------------------------

# -------------------------------------------------
# A function to retrieve a value with user input
# -------------------------------------------------
def get_input():
    # Default values
    start_default = 1
    end_default = 100

    # Start value
    start_input = input(f'Enter the initial value (default {start_default}): ')
    if start_input == '':  # Če uporabnik pritisne Enter brez vnosa, uporabimo privzeto vrednost
        start = start_default
    else:
        try:
            start = int(start_input)
        except ValueError:
            print("The value entered is not valid. The default value of {start_default} will be used.")
            start = start_default

    # End value
    end_input = input(f'Enter the final value (default {end_default}): ')
    if end_input == '':  # Če uporabnik pritisne Enter brez vnosa, uporabimo privzeto vrednost
        end = end_default
    else:
        try:
            end = int(end_input)
        except ValueError:
            print("The value entered is not valid. The default value of {end_default} will be used.")
            end = end_default

    # Checking if Start is less than End
    while start >= end:
        print("The initial value must be less than the final value!")
        start_input = input(f'Enter the final value (default {end_default}): ')
        if start_input == '':  # Če uporabnik pritisne Enter brez vnosa, uporabimo privzeto vrednost
            start = start_default
        else:
            try:
                start = int(start_input)
            except ValueError:
                print("The value entered is not valid. The default value of {start_default} will be used.")
                start = start_default

        end_input = input(f'Enter the final value (default {end_default}): ')
        if end_input == '':  # Če uporabnik pritisne Enter brez vnosa, uporabimo privzeto vrednost
            end = end_default
        else:
            try:
                end = int(end_input)
            except ValueError:
                print("The value entered is not valid. The default value of {end_default} will be used.")
                end = end_default

    return start, end
# -------------------------------------------------
