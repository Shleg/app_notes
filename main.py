from datetime import datetime
from note_manager import NoteManager


def print_commands():
    print("Доступные команды:")
    print("add - Добавить заметку")
    print("edit - Редактировать заметку")
    print("delete - Удалить заметку")
    print("list - Список всех заметок")
    print("filter - Фильтровать заметки по дате")
    print("print - Вывести заметку по ID")
    print("exit - Выйти из приложения")


def main():
    filename = 'notes.json'
    note_manager = NoteManager(filename)

    while True:
        print_commands()
        print("Введите команду:")
        command = input().strip().lower()

        if command == 'add':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.add_note(title, body)
            print("Заметка успешно сохранена")

        elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            if note_manager.edit_note(note_id, title, body):
                print("Заметка успешно отредактирована")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            if note_manager.delete_note(note_id):
                print("Заметка успешно удалена")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'list':
            for note in note_manager.notes:
                print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_at}")

        elif command == 'filter':
            date_str = input("Введите дату для фильтрации (ГГГГ-ММ-ДД): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                filtered_notes = note_manager.get_notes_by_date(date)
                for note in filtered_notes:
                    print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_at}")
            except ValueError:
                print("Некорректный формат даты. Используйте ГГГГ-ММ-ДД.")

        elif command == 'print':
            note_id = int(input("Введите ID заметки: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                print(f"ID: {note.note_id}, Заголовок: {note.title}, Тело заметки: {note.body}, Дата создания: {note.created_at}")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'exit':
            break


if __name__ == "__main__":
    main()