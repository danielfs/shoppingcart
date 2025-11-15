import os
from constants import DISPLAY_LENGTH, OPERATIONS

def display_menu():
    print("\n" + "-" * DISPLAY_LENGTH)
    print("Choose an operation:")
    for operation in OPERATIONS:
        print(f"{operation[0]}. {operation[1]}")
    print("-" * DISPLAY_LENGTH)
    print("Enter your choice: ", end="")

def clear_terminal():
    # Check if the operating system is Windows ('nt')
    if os.name == 'nt':
        _ = os.system('cls')
    # Otherwise, assume it's a Unix-like system (Linux, macOS)
    else:
        _ = os.system('clear')

def wait_enter():
    input("Press Enter to continue...")