from datetime import datetime #Import the library that inputs a timestamp
import pandas as pd #Import library to manage note entries into a dataframe for ease


class Notes:
    """
    A class to represent a note with content and an automatic timestamp.
    """

    def __init__(self, content):
        """
        Initializes a Note instance.

        Args:
            content (str): The text content of the note.
        """
        self.content = content
        self.created_at = datetime.now()  # Automatically assigns a timestamp

    def display(self):
        """
        Prints the note's timestamp and content.
        """
        print(str(self.created_at) + "\n" + self.content)
class TextNote(Notes):
    """
    A simple text-based note.
    """

    def display(self):
        """
        Displays the note type, timestamp, and content.
        """
        print("Simple Note")
        super().display()  # Reuses the parent class display method

class ReminderNote(Notes):
    """
    A note that includes an additional reminder date and time.
    """

    def __init__(self, content, reminder_date_time=None):
        """
        Initializes a ReminderNote instance.

        Args:
            content (str): The text content of the note.
            reminder_date_time (datetime, optional): The reminder date and time.
        """
        super().__init__(content)
        self.reminder_date_time = reminder_date_time  # Initializes reminder with None by default

    def set_reminder(self, reminder_date_time):
        """
        Sets a reminder date and time.
        
        Args:
            reminder_date_time (datetime): The date and time for the reminder.
        """
        self.reminder_date_time = reminder_date_time

    def display(self):
        """
        Displays the reminder note with its details.
        """
        print("Reminder Note")
        super().display()
        if self.reminder_date_time:
            print("Reminder set for: " + str(self.reminder_date_time))
        else:
            print("No reminder set")

class NotesManager:
    """
    A class to manage notes using a pandas DataFrame.
    """

    def __init__(self):
        """
        Initialize an empty DataFrame to store notes.
        """
        self.notes = pd.DataFrame(columns=["ID", "Type", "Content", "Created_At", "Reminder_Time"])
        self.note_id = 1  # Unique ID for each note
