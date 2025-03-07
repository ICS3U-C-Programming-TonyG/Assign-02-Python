#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-02-19

# Calculates the surface area and the volume of any given tetrahedron

# Displays the user a system menu, allowing the user to choose which calculator they want.

# Imports math
import math

# Displays a welcoming message and the 3 calculator options. 
def main():
    print("Hello, This program will allow you to calculate the surface area as well as the volume, by inputting the edge length of a tetrahedron!")
    print("available options:")
    print("1. Volume calculator")
    print("2. Surface area calculator")
    print("3. Edge length calculator")

# Will display any of the 3 choices depending on the user's choice. 
    choice = input("Please select an option: ")

# 1st choice, calculates the volume from the edge length, displays units and formats answer to 2 decimals.
    if choice == "1":
        edge = float(input("Please enter edge length (cm): "))
        volume = (edge ** 3 / (6 * math.sqrt(2)))
        print("Volume is {:.2f} cm³.".format(volume))

# 2nd choice, calculates the surface area from edge length, displays units and formats answer to 2 decimals.
    elif choice == "2":
        edge = float(input("Please enter edge length (cm): "))
        surface_area = (math.sqrt(3) * (edge ** 2))
        print("Surface area is {:.2f} cm².".format(surface_area))

# 3rd choice, calculates the edge length from surface area, displays units and formats answer to 2 decimals.
    elif choice == "3":
        surface_area = float(input("Please enter surface area (cm²): "))
        edge_length = (((1 / 3) * 3 ** (3 / 4)) * math.sqrt(surface_area))
        print("Edge length is {:.2f} cm.".format(edge_length))

# If the user does not choose between 1 2 or 3, it will indicate that you must.
    else:
        print("Invalid option! Please choose between 1, 2 or 3")

if __name__ == "__main__":
    main()