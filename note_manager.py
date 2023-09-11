import json
import os
from typing import List
from note import Note


class NoteManager:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.notes: List[Note] = []
        self.load_notes()

    def load_notes(self) -> None:
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(**note_data)
                    self.notes.append(note)

    def save_notes(self) -> None:
        with open(self.filename, 'w') as file:
            data = [note.__dict__ for note in self.notes]
            json.dump(data, file, default=str)

    def add_note(self, title: str, body: str) -> bool:
        if title.strip() and body.strip():
            note_id: int = len(self.notes) + 1
            note = Note(note_id, title, body)
            self.notes.append(note)
            self.save_notes()
            return True
        else:
            return False

    def edit_note(self, note_id: int, title: str, body: str) -> bool:
        note = self.get_note_by_id(note_id)
        if note:
            if not title.strip():
                title = note.title
            if not body.strip():
                body = note.body
            note.update(title, body)
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id: int) -> bool:
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return True
        return False

    def get_note_by_id(self, note_id: int) -> Note:
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def get_notes_by_date(self, date: str) -> List[Note]:
        filtered_notes = [note for note in self.notes if note.created_at.date() == date]
        return filtered_notes
