import json
import os

from note import Note


class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(**note_data)
                    self.notes.append(note)

    def save_notes(self):
        with open(self.filename, 'w') as file:
            data = [note.__dict__ for note in self.notes]
            json.dump(data, file, default=str)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title, body)
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return True
        return False

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def get_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.created_at.date() == date]
        return filtered_notes
