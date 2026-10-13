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


""" Show numbered entries and delete the one the user picks. """
def delete_entry(filename):
    entries = diary.read_entries(filename) #reference read_entries from diary.py
    
    if not entries:
        print("No entries to delete.")
        return

    for entry_number, entry in enumerate(entries, start=1): # https://docs.python.org/3/builtins/functions.html#enumerate
        print(f"{entry_number}. {entry}")

    choice = input("Enter the number of the entry to delete: ")
    if choice.isdigit() and 1 <= int(choice) <= len(entries):
        diary.delete_entry(filename, int(choice)) # reference delete_entry from diary.py
        print("Entry deleted.")

    else:
        print("Invalid number.")


