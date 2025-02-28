import pytest
from smart_notes import NotesManager  # Import your NotesManager class

@pytest.fixture
def setup_notes_manager():
    """
Create a fresh NotesManager for each test.
"""
    return NotesManager()
