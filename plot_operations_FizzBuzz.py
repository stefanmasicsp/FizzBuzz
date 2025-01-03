# -------------------------------------------------
# Seminar:     Data Steward, 2024-2025, Module 2.7
# Description: Module plot_operations_FizzBuzz.py
# Author:      Štefan Masič
# Date:        1.1.2025
# Changes:
# -------------------------------------------------

# -------------------------------------------------
# Libraries:
import matplotlib.pyplot as plt
import numpy as np
# -------------------------------------------------

# -------------------------------------------------
# Test function to plot graph.
# -------------------------------------------------
def plot_graph(results):
    # Seznam točk, ki jih bomo uporabili za x-osi
    x_values = list(range(1, len(results) + 1))

    # Hide numbers (for testing)
    hide_numbers = True

    # List of colors for points
    colors = []

    # Pretvorba rezultatov v številčne vrednosti in določanje barv
    numeric_results = []  # Tukaj bomo shranili numerične vrednosti za Y-os

    # Definition of colors for Y-axis.
    for i, result in enumerate(results):
        if result == "Fizz":
            numeric_results.append(i + 1)   # Keep numeric value (3, 6, 9...)
            colors.append("blue")            # Blue color for Fizz
        elif result == "Buzz":
            numeric_results.append(i + 1)
            colors.append("green")          # Green color for Buzz
        elif result == "FizzBuzz":
            numeric_results.append(i + 1) 
            colors.append("red")            # Red color FizzBuzz
        else:
            if hide_numbers:
                numeric_results.append(np.nan)  # Do not plot points for numbers
                colors.append("none")           
            else:
                numeric_results.append(result)  
                colors.append("gray")           # Grey color for numbers


    # Creating a graph (X axis is wider than Y)
    plt.figure(figsize=(15, 6))

    # Plotting points. If there are many points, point size decreases.
    point_size = 50         # Default point size.
    if len(results) > 300:
        point_size = 20
    else:
        point_size = 50

    scatter = plt.scatter(x_values, numeric_results, c=colors, s=point_size, edgecolor="none", alpha=0.7)

    # Create a manual legend based on the colors we use in the diagram
    plt.legend(handles=[
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Fizz'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Buzz'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='FizzBuzz'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=10, label='Others')
        ], loc="upper left", title="Legend")
    
    # Setting x, y labels and title
    plt.xlabel("Place in sequence")
    plt.ylabel("Result")
    plt.title("FizzBuzz Diagram")

    # Plotting graph
    plt.grid(True)
    plt.show()
# -------------------------------------------------