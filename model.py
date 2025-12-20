import view


class PhoneBook:

    SEPARATOR = ';'
    FIELDS = [
        'name',
        'phone',
        'city',
        'address',
        'comment',
    ]

    def __init__(self, path: str):
        self.path = path
        self.phonebook = {}



    def read_file(self, path:str,):
        """Чтение телефонной книги"""
        try:
            with open(path, "r", encoding="utf-8") as file:
                idx = 1
                while line := file.readline().strip():
                    contact_data = line.split(self.SEPARATOR)
                    #self.phonebook[idx] = {FIELDS[i]:contact_data[i] for i in range(len(self.FIELDS))}
                    self.phonebook[idx] = {
                        field: value.strip()
                        for field, value in zip(self.FIELDS, contact_data)
                    }
                    idx += 1
        except FileNotFoundError:
            print_message("Файл не найден.")

    def save_file(self, path:str,phonebook):
        """Запись телефонной книги"""
        with open(path, "w", encoding="utf-8") as file:
            data = []
            for contact in self.phonebook.values():
                data.append(self.SEPARATOR.join(list(contact.values())))
            data = '\n'.join(data)
            file.write(data)


    def _next_id(self):
        """Получаем следующий уникальный ID для контакта"""
        #return max(self.phonebook.keys()) + 1
        return len(self.phonebook) + 1


    # def new_contact(self, contact_data:str):
    #     """Добавляет новый контакт в телефонную книгу."""
    #     contact = {}
    #     for i in range(len(self.FIELDS, )):
    #         contact[self.FIELDS[i]] = contact_data[i]
    #         self.phonebook[_next_id] = contact

    def add_contact(self, contact_data: dict):
        """Добавляет новый контакт в телефонную книгу."""
        idx = self._next_id()
        self.phonebook[idx] = contact_data


    def find_contact(self, word: str):
        """Поиск контакта по заданному слову"""
        result = {}
        for idx, contact in self.phonebook.items():
            for value in contact.values():
                if word.lower() in value.lower():
                    result[idx] = contact
                    break
        return result


    def edit_contact(self, contact_id: str, new_contact_data: list[str], phonebook,fields):
        """Редактирование существующего контакта."""
        contact_id = int(contact_id)
        for i in range(len(fields)):
            if new_contact_data[i]:
                phonebook[contact_id][fields[i]] = new_contact_data[i]
        return phonebook[contact_id][fields[0]]


    def delete_contact(self, contact_id: str, phonebook, fields):
        """Удаление контакта"""
        contact_id = int(contact_id)
        contact = phonebook.pop(contact_id)
        return contact[fields[0]]
