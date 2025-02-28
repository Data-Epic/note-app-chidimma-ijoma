from datetime import datetime

class Note:
    """
    Base class for a note, storing content and creation timestamp.
    """

    note_counter = 0  # Assign unique IDs to notes

    def __init__(self, content):
        """
        Initializes a Note instance.

        Args:
            content (str): The text content of the note.
        """
        self.id = Note.note_counter + 1
        Note.note_counter += 1
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self):
        """
        Displays note details.

        Returns:
            str: Formatted string containing note details.
        """
        return f"ID: {self.id}\nCreated: {self.created_at}\nContent: {self.content}"

class TextNote(Note):
    """
    A simple text-based note.
    """

    def __init__(self, content):
        """
        Initializes a TextNote instance.

        Args:
            content (str): The text content of the note.
        """
        super().__init__(content)

    def display(self):
        """
        Displays text note details.

        Returns:
            str: Formatted string with note type included.
        """
        return f"[Text Note]\n{super().display()}"

class ReminderNote(Note):
    """
    A reminder note with an additional reminder time.
    """

    def __init__(self, content, reminder_time):
        """
        Initializes a ReminderNote instance.

        Args:
            content (str): The text content of the note.
            reminder_time (str): The reminder time in "YYYY-MM-DD HH:MM" format.
        """
        super().__init__(content)
        self.reminder_time = reminder_time

    def display(self):
        """
        Displays reminder note details.

        Returns:
            str: Formatted string with note type and reminder time.
        """
        return f"[Reminder Note]\n{super().display()}\nReminder Time: {self.reminder_time}"

class NotesManager:
    """
    Manages a collection of notes with functionalities to add, delete, search, and display.
    """

    def __init__(self):
        """
        Initializes the NotesManager with an empty list of notes.
        """
        self.notes = [] # Creates an empty list to store notes.

    def add_note(self, note_type, content, reminder_time=None):
        """
        Adds a new note of the specified type.

        Args:
            note_type (str): Type of note ("text" or "reminder").
            content (str): The text content of the note.
            reminder_time (str, optional): The reminder time (only for ReminderNote).

        Returns:
            int: The ID of the newly created note.
        """
        if note_type.lower() == "text":
            note = TextNote(content)
        elif note_type.lower() == "reminder":
            if not reminder_time:
                raise ValueError("ReminderNote requires a reminder_time.")
            note = ReminderNote(content, reminder_time)
        else:
            print("Invalid note type! Use 'text' or 'reminder'.")
            return

        self.notes.append(note)
        print(f"Note added successfully! (ID: {note.id})")
        return note.id

    def delete_note(self, note_id):
        """
        Removes a note by its ID.

        Args:
            note_id (int): The ID of the note to be removed.

        Returns:
            bool: True if the note was deleted, False if not found.
        """
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                print(f"Note with ID {note_id} deleted.")
                return True
        print("Note not found.")
        return False

    def show_notes(self):
        """
        Displays all stored notes.
        """
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(note.display())
                print("-" * 40) # A separator between notes

    def search_notes(self, keyword):
        """
        Finds and displays notes containing a specific keyword.

        Args:
            keyword (str): The keyword to search for.
        """
        found_notes = [note for note in self.notes if keyword.lower() in note.content.lower()]
        if not found_notes:
            print(f"No notes found containing '{keyword}'.")
        else:
            for note in found_notes:
                print(note.display())
                print("-" * 30)

def main():
    """
    Main function to interact with the Notes Manager.
    """
    notes_manager = NotesManager()

    while True:
        print("\nSmart Notes Manager")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ").strip()
            reminder_time = None
            if note_type == "reminder":
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ").strip()
            notes_manager.add_note(note_type, content, reminder_time)

        elif choice == "2":
            notes_manager.show_notes()

        elif choice == "3":
            keyword = input("Enter keyword to search: ").strip()
            notes_manager.search_notes(keyword)

        elif choice == "4":
            try:
                note_id = int(input("Enter note ID to delete: "))
                notes_manager.delete_note(note_id)
            except ValueError:
                print("Invalid input. Please enter a valid note ID.")

        elif choice == "5":
            print("Exiting Smart Notes Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()