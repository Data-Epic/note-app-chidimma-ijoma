import pytest
from smart_notes import NotesManager  # Import your NotesManager class

@pytest.fixture
def setup_notes_manager():
    """
Create a fresh NotesManager for each test.
"""
    return NotesManager()

def test_add_text_note(setup_notes_manager):
    """
Test adding a simple text note.
"""
    notes_manager = setup_notes_manager
    note_id = notes_manager.add_note("text", "Hello World!")
    
    assert len(notes_manager.notes) == 1
    assert notes_manager.notes[0].id == note_id

def test_add_reminder_note(setup_notes_manager):
    """
Test adding a reminder note.
"""
    notes_manager = setup_notes_manager
    note_id = notes_manager.add_note("reminder", "Doctor's appointment", "2025-03-10 10:00 AM")
    
    assert len(notes_manager.notes) == 1
    assert notes_manager.notes[0].id == note_id
    assert notes_manager.notes[0].reminder_time == "2025-03-10 10:00 AM"

def test_delete_note(setup_notes_manager):
    """
Test deleting a note.
"""
    notes_manager = setup_notes_manager
    note_id = notes_manager.add_note("text", "To be deleted")
    
    assert notes_manager.delete_note(note_id) == True
    assert len(notes_manager.notes) == 0

def test_delete_nonexistent_note(setup_notes_manager):
    """
Test deleting a note that does not exist.
"""
    notes_manager = setup_notes_manager
    assert notes_manager.delete_note(999) == False  # Should return False

def test_show_notes(setup_notes_manager, capsys):
    """
Test showing notes.
"""
    notes_manager = setup_notes_manager
    notes_manager.add_note("text", "First note")
    notes_manager.show_notes()

    captured = capsys.readouterr()
    assert "First note" in captured.out

def test_search_notes(setup_notes_manager, capsys):
    """
Test searching for a note.
"""
    notes_manager = setup_notes_manager
    notes_manager.add_note("text", "Buy milk")
    notes_manager.search_notes("milk")

    captured = capsys.readouterr()
    assert "Buy milk" in captured.out

def test_search_no_match(setup_notes_manager, capsys):
    """
Test searching for a non-existent keyword.
"""
    notes_manager = setup_notes_manager
    notes_manager.add_note("text", "Some random note")
    notes_manager.search_notes("Python")

    captured = capsys.readouterr()
    assert "No notes found" in captured.out



