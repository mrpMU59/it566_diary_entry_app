""" Interactive Diary Application. """

from datetime import date

import diary

""" Print a list of entries, or a message if the list is empty. """
def print_entries(entries):
    if not entries:
        print("No entries found.")
        return
    for entry in entries:
        print(entry)


""" Ask the user for a date until a valid one is entered. """
def ask_for_date():
    while True:
        entered_date = input("Enter a date (YYYY-MM-DD): ")
        if diary.is_valid_date(entered_date): #references the is_valid_date function in diary.py
            return entered_date

        print("Invalid date. Please use the format YYYY-MM-DD.")


""" Wait for the user before showing the menu again. """
def return_to_menu():
    input("\nPress Enter to return to the menu.")


