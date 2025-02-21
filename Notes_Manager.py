from datetime import datetime #Import the library that inputs a timestamp

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
