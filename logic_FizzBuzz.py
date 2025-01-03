# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Module input_FizzBuzz.py
# Author:      Štefan Masič
# Date:        1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# Function to run the FizzBuzz game.
# Input: Start, End
# Output: result array
# -------------------------------------------------
def fizz_buzz(Start, End):
    # Initialization.
    result = []

    # Loop from Start to End.
    for i in range(Start, End + 1):
        # Check if i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        
        # Check if i is only divisible by 3
        elif i % 3 == 0:
            result.append("Fizz")
        
        # Check if i is only divisible by 5
        elif i % 5 == 0:
            result.append("Buzz")
        
        # If none of the conditions apply, print i
        else:
            result.append(i)
        
    return result
# -------------------------------------------------