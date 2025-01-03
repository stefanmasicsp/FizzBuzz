# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Module file_operations_FizzBuzz.py
# Author:      Štefan Masič
# Date:        1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# Libraries
import csv
# -------------------------------------------------

# -------------------------------------------------
# Create .csv with numbers.
# -------------------------------------------------
#def generate_csv_file(Start, End, file_name):
#    numbers = list(range(Start, End+1))
#
#    # Open file
#    with open(file_name, mode='w', newline='') as file:
#        writer = csv.writer(file)
#    
#        # Write numbers, separated with comma.
#        writer.writerow(numbers)
# -------------------------------------------------


def generate_csv_file_with_interface(start, end, filename=None):
    # Če ni ime datoteke, uporabimo privzeto
    if filename is None:
        filename = "output.csv"

    numbers = list(range(start, end+1))

    # Open file
    with open(filename, mode='w', newline='') as file:
        # Odpri CSV datoteko za pisanje
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write numbers, separated with comma.
                writer.writerow(numbers)
                print(f"CSV datoteka '{filename}' je bila uspešno ustvarjena!")
        except Exception as e:
            print(f"Prišlo je do napake pri ustvarjanju datoteke: {e}")


# -------------------------------------------------
# Load numbers from csv file
# -------------------------------------------------
def load_numbers_from_csv(file_path):
    input_array = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Poberi številke iz vsake vrstice
            input_array = [int(num) for num in row]  # Ker imamo samo eno vrstico
    return input_array
# -------------------------------------------------