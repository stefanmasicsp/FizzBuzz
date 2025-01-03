# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Module tests_FizzBuzz.py
# Author:      Štefan Masič
# Date:        1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# FizzBuzz modules:
import init_FizzBuzz
import logic_FizzBuzz

from init_FizzBuzz import GREEN, RED, BLUE, RESET
from logic_FizzBuzz import fizz_buzz
# -------------------------------------------------

# -------------------------------------------------
# Test function to compare results with test results
# -------------------------------------------------
def run_test(start, end, expected_result):
    
    
    # Call function fizz_buzz
    actual_result = fizz_buzz(start, end)
    
    # Compare both arrays
    if actual_result == expected_result:
        print(f"{GREEN}Test is successful.{RESET}")
        print(f"Result are: {BLUE}{actual_result}.{RESET}")
        print()
    else:
        # Loop through each index and compare values
        for i in range(len(actual_result)):
            if actual_result[i] != expected_result[i]:
                print(f"{GREEN}Error on index {i + 1}: excpected {expected_result[i]}, actual {actual_result[i]}.{RESET}")

    print("\n" * 2)  # 2 additional lines
# -------------------------------------------------