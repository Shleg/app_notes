from datetime import datetime


class Note:
    def __init__(self, note_id: int, title: str, body: str, created_at=None, updated_at=None) -> None:
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now().replace(microsecond=0)
        self.updated_at = updated_at or self.created_at

    def update(self, title: str, body: str) -> None:
        self.title = title
        self.body = body
        self.updated_at = datetime.now()