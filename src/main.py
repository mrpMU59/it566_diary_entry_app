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

