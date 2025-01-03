# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Main program for game FizzBuzz
# Start:       python .\FizzBuzz.py
# Author:      Štefan Masič
# Date:        30.12.2024, 1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# Libraries:
import keyboard
import matplotlib.pyplot as plt
import numpy as np
import csv
# -------------------------------------------------

# -------------------------------------------------
# FizzBuzz modules:
import init_FizzBuzz
import logic_FizzBuzz
import input_FizzBuzz
import file_operations_FizzBuzz
import plot_operations_FizzBuzz
import tests_FizzBuzz

from init_FizzBuzz import GREEN, RED, BLUE, RESET
from input_FizzBuzz import get_input
from logic_FizzBuzz import fizz_buzz
from plot_operations_FizzBuzz import plot_graph
from file_operations_FizzBuzz import generate_csv_file_with_interface
from file_operations_FizzBuzz import load_numbers_from_csv
from tests_FizzBuzz import run_test
# -------------------------------------------------


# -------------------------------------------------
# Main program
# -------------------------------------------------
if __name__ == "__main__":
    # -------------------------------------------------
    # 1.1 Call FizzBuzz. Input from the user.
    print("1. STARTUP PART")
    print("1.1 Input from the user")

    Start, End = get_input()

    fizz_buzz_result = fizz_buzz(Start, End)
    
    print("\n" * 1)  # 2 additional lines
    print(f"Result are: {GREEN}{fizz_buzz_result}.{RESET}")
    print("\n" * 1)  # 2 additional lines

    # Plotting graph.
    test_choice = input(f"Do you want to plot graph? (Y/N): ").strip().upper()
    
    if test_choice == 'Y':
         plot_graph(fizz_buzz_result)
    else:
        print("Plotting graph was not performed.")
    # -------------------------------------------------

    test_choice = input(f"Do you want to run FizzBuzz with data from file? (Y/N): ").strip().upper()

    if test_choice == 'Y':
        # -------------------------------------------------
        # 1.2 Call FizzBuzz. Input from the file.
        print(f"1.1 Input from file. First we create file with range from {Start} to {End}.")

        testing_file = "Test01.csv"
        generate_csv_file_with_interface(start=Start, end=End, filename=testing_file)
    
        input_array = load_numbers_from_csv(testing_file)

        # Start value is at position 0. End value is at last position (-1).
        Start = input_array[0]
        End = input_array[-1]

        fizz_buzz_result = fizz_buzz(Start, End)

        print("\n" * 1)  # 2 additional lines
        print(f"Input values from file {testing_file} is: {GREEN}{input_array}.{RESET}")
        print()
        print(f"Results are: {GREEN}{fizz_buzz_result}.{RESET}")
        print("\n" * 1)  # 2 additional lines
        # -------------------------------------------------
    else:
        print("Running FizzBuzz with data from file was canceled.")


    # -------------------------------------------------
    # TESTING PART
    # -------------------------------------------------

    # Testing part no 1.
    print("2. MAIN PART")
    Start = 1
    End = 17
    test_choice = input(f"Do you want to run the first test (start, end) = ({Start}, {End}) (Y/N): ").strip().upper()
    
    if test_choice == 'Y':
        # Test execution if user presses "Y"
        test_correct_results = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17]
        run_test(Start, End, test_correct_results)
    else:
        print("The test was not performed.")


    # Testing part no 2.
    Start = 1
    End = 77
    test_choice = input(f"Do you want to run the second test (start, end) = ({Start}, {End}) (Y/N): ").strip().upper()
    
    if test_choice == 'Y':
        # Test execution if user presses "Y"
        test_correct_results = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
            "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz",
            "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, 
            "FizzBuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "FizzBuzz", 76, 77]

        run_test(Start, End, test_correct_results)
    else:
        print("The test was not performed.")


    print(f"{RED}END of program. Thanks for using.{RESET}")
# -------------------------------------------------

