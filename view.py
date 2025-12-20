import text

def show_menu():
    """Отображение меню"""
    for i, item in enumerate(text.menu_items):
        if i != 0:
            print(f'\t{i}. {item}')
        else:
            print(item)


def input_data(message: str | tuple[str, ...]):
    """_"""
    result = []
    if isinstance(message, str):
        message = (message,)
    for input_message in message:
        result.append(input(input_message))
    if len(result) == 1:
        return result[0]
    return result


def show_contact(phonebook: dict[int, dict[str, str]], message_error: str):
    """Отображения контактов"""
    if phonebook:
        for idx, contact in phonebook.items():
            print(f'\t{idx:>3}. {contact["name"]:<20}{contact["phone"]:<20}'
                  f'{contact["comment"]:<20}{contact["city"]:<20}{contact["comment"]:<20}')
        print()
    else:
        print_message(message_error)


def print_message(message: str):
    """ Вывод сообщения в рамке"""
    print('\n┌' + '─'*(len(message)+2)+'┐')
    print(f'│ {message} │')
    print('└' + '─'*(len(message)+2)+'┘\n')
