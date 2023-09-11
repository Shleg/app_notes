from datetime import datetime
from typing import List

from note import Note
from note_manager import NoteManager


def print_commands() -> None:
    print("Доступные команды:")
    print("add - Добавить заметку")
    print("edit - Редактировать заметку")
    print("delete - Удалить заметку")
    print("list - Список всех заметок")
    print("filter - Фильтровать заметки по дате")
    print("print - Вывести заметку по ID")
    print("exit - Выйти из приложения")


def main() -> None:
    filename: str = 'notes.json'
    note_manager: NoteManager = NoteManager(filename)

    while True:
        print_commands()
        command: str = input("Введите команду: ").strip().lower()

        if command == 'add':
            title: str = input("Введите заголовок заметки: ")
            body: str = input("Введите тело заметки: ")
            if note_manager.add_note(title, body):
                print("Заметка успешно сохранена")
            else:
                print("Заголовок и описание не могут быть пустыми. Заметка не сохранена.")

        elif command == 'edit':
            note_id: int = int(input("Введите ID заметки для редактирования: "))
            title: str = input("Введите новый заголовок заметки: ")
            body: str = input("Введите новое тело заметки: ")
            if note_manager.edit_note(note_id, title, body):
                print("Заметка успешно отредактирована")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'delete':
            note_id: int = int(input("Введите ID заметки для удаления: "))
            if note_manager.delete_note(note_id):
                print("Заметка успешно удалена")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'list':
            for note in note_manager.notes:
                print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_at}")

        elif command == 'filter':
            date_str: str = input("Введите дату для фильтрации (ГГГГ-ММ-ДД): ")
            try:
                date: datetime = datetime.strptime(date_str, '%Y-%m-%d').date()
                filtered_notes: List[Note] = note_manager.get_notes_by_date(date)
                for note in filtered_notes:
                    print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_at}")
            except ValueError:
                print("Некорректный формат даты. Используйте ГГГГ-ММ-ДД.")

        elif command == 'print':
            note_id: int = int(input("Введите ID заметки: "))
            note: Note = note_manager.get_note_by_id(note_id)
            if note:
                print(
                    f"ID: {note.note_id}, Заголовок: {note.title}, Тело заметки: {note.body}, Дата создания: {note.created_at}")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'exit':
            break


if __name__ == "__main__":
    main()
