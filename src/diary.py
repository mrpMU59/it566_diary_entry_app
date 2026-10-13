""" Functions for reading, writing, and managing dated diary entries from user input. 
    Each entry is stored as one line in a text file in the format: YYYY-MM-DD | entry text """

from datetime import date  # https://docs.python.org/3/library/datetime.html#datetime.date

date_format = "%Y-%m-%d"


""" Returns True of the text is a valid date in YYYY-MM-DD format."""
def is_valid_date(entry_date):
    try:
        date.strptime(entry_date, date_format) # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        return True
    except ValueError:
        return False


