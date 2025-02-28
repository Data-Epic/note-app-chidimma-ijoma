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

