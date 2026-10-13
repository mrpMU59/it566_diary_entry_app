""" Functions for reading, writing, and managing dated diary entries from user input. 
    Each entry is stored as one line in a text file in the format: YYYY-MM-DD | entry text """

from datetime import date  # https://docs.python.org/3/library/datetime.html#datetime.date

date_format = "%Y-%m-%d"


""" Returns True if the text is a valid date in YYYY-MM-DD format. """
def is_valid_date(entry_date):
    try:
        date.strptime(entry_date, date_format) # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        return True
    except ValueError:
        return False


""" Add one entry as a new line in the file. """ # Computer Scripting Techniques with Python (1st ed.), Ch 16.1.1
def add_entry(filename, entry_text, entry_date): 
    with open(filename, "a") as file: 
        file.write(f"{entry_date} | {entry_text}\n")


""" Return all entries from the diary file as a list of lines. """
def read_entries(filename):
    entries = []
    try:
        with open(filename, "r") as file: # Computer Scripting Techniques with Python (1st ed.), Ch 16.1.1
            for line in file:
                line = line.strip() # https://docs.python.org/3/builtins/stdtypes.html#str.strip
                if line != "":
                    entries.append(line)

    except FileNotFoundError:
        pass
    
    return entries

