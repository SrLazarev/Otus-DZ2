import sys
import view
import model
import text


def start_app():
    """Запуск программы"""
    while True:
        try:
            view.show_menu()
            user_choice = view.input_data(text.input_choice)
            user_choice = int(user_choice)
            menu_items= [
                '',
                open_contacts,
                save_contacts,
                show_contacts,
                add_contacts,
                find_contacts,
                edit_contacts,
                delete_contacts,
                exit_program,
            ]
            menu_items[int(user_choice)]()
        except IndexError:
            view.print_message(text.error_choice)


def open_contacts():
    """Открытие телефонной книги."""
    model.read_file('phonebook.txt')
    view.print_message(text.read_phonebook_successful)

def save_contacts():
    """Сохранение телефонной книги."""
    model.save_file('phonebook.txt')
    view.print_message(text.save_phonebook_successful)

def show_contacts():
    """Показывает все контакты."""
    view.show_contact(model.phonebook,text.empty_book_error)

def add_contacts():
    """Добавление нового контакта."""
    contact = view.input_data(text.input_add_contact)
    model.add_contact(contact)
    view.print_message(text.add_contact_successful.format(name=contact[0]))

def find_contacts():
    """Поиск контакта по ключевому слову."""
    search_word = view.input_data(text.input_search_word)
    result = model.find_contact(search_word)
    view.show_contacts(result, text.empty_find_error.format(word=search_word))

def edit_contacts():
    """Редактирование выбранного контакта."""
    id_edit = view.input_data(text.input_to_do_edit)
    edited_contact = view.input_data(text.input_edit_contact)
    contact_name = model.edit_contact(id_edit, edited_contact)
    view.print_message(text.edit_contact_successful.format(name=contact_name))

def delete_contacts():
    """Удаление контакта по выбранному ID."""
    id_delete = view.input_data(text.input_id_to_delete)
    contact_name = model.delete_contact(id_delete)
    view.print_message(text.delete_contact_successful.format(name=contact_name))

def exit_program():
    """Завершение работы программы."""
    view.print_message(text.exit_message)
    sys.exit()











