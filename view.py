

def show_menu():
    """Отображение меню"""
    for i, item in enumerate(menu_items):
        if i != 0:
            print(f'\t{i}. {item}')
        else:
            print(item)


def input_data(message: str | tuple[str, ...]):
    """Функция ввода данных от пользователя"""
    result = []
    if isinstance(message, str):
        message = (message,)
    for input_message in message:
        result.append(input(input_message))
    if len(result) == 1:
        return result[0]
    return result


def show_contact(phonebook: dict[int, dict[str, str]], message_error: str):
    """Отображения контактов из телефонной книги"""
    if phonebook:
        print('\n Перечень доступных контактов')
        print('     ID  Name        Phone           City        Address             Comment')
        for idx, contact in phonebook.items():
            print(f'\t{idx:>3}. {contact["name"]:<12}{contact["phone"]:<16}'
                  f'{contact["city"]:<12}{contact["address"]:<20}{contact["comment"]:<60}')
        print()
    else:
        print_message(message_error)


def print_message(message: str):
    """ Выводит сообщение в красивой рамке"""
    print('\n┌' + '─'*(len(message)+2)+'┐')
    print(f'│ {message} │')
    print('└' + '─'*(len(message)+2)+'┘\n')


menu_items = [
    'Главное меню',
    'Открыть файл',
    'Сохранить файл',
    'Показать контакты',
    'Создать контакт',
    'Найти контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход',
]

add_contact_successful = 'Контакт {name} успешно добавлен!'
read_phonebook_successful = 'Телефонная книга успешно открыта'
save_phonebook_successful = 'Телефонная книга сохранена'
new_contact_successful = 'Контакт {name} успешно создан'
edit_contact_successful = 'Контакт "{name}" успешно изменен '
delete_contact_successful = 'Контакт "{name}" успешно удален'

input_choice = 'Выберете пункт меню:'
input_add_contact = (
    'Введите Имя',
    'Введите номер',
    'Введите город',
    'Введите адрес',
    'Введите комментарий',
)
input_search_word = 'Введите слово для поиска: '
input_id_to_edit = 'Введите ID для изменения: '
input_id_to_delete = 'Введите ID контакта для удаления:'
input_edit_contact = [
    'Введите новое имя для изменения контакта,',
    'Введите новый номер для изменения контакта ',
    'Введите новый город для изменения контакта',
    'Введите новый адрес для изменения контакта',
    'Введите новый комментарий для изменения контакта',
]

error_read_file = 'Ошибка чтения файла'
error_edit_file = 'Ошибка изменения файла'
error_choice = 'Ошибка выбора пункта меню.'
error_format = 'Некорректный формат данных.'
error_id_format = 'Неверный формат ID.'
error_empty_find = 'Контакты содержащие "{word}" - не найдены'
error_empty_book = 'Телефонная книга пуста или не открыта'

file_not_found = 'Файл не найден'
id_not_found = 'Контакт с указанным ID не найден.'

exit_message = 'Выход'
