import view
from Otus_Basic_09.DZ.DZ_2_my.view import print_message


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
        self.path = path #('phonebook.txt')
        self.phonebook = {}


    def read_file(self):
        """Чтение телефонной книги"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                idx = 1
                while line := file.readline().strip():
                    contact_data = line.split(self.SEPARATOR)
                    self.phonebook[idx] = {
                        field: value.strip()
                        for field, value in zip(self.FIELDS, contact_data)
                    }
                    idx += 1
        except FileNotFoundError:
            print_message(view.file_not_found)
        except Exception as e:
            print_message(view.error_read_file.format(e))


    def save_file(self):
        """Запись телефонной книги"""
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                data = []
                for contact in self.phonebook.values():
                    data.append(self.SEPARATOR.join(list(contact.values())))
                data = '\n'.join(data)
                file.write(data)
        except KeyError:
            print_message(view.error_format)
        except Exception as e:
            print_message(view.error_edit_file.format(e))


    def _next_id(self):
        """Получаем следующий уникальный ID для контакта"""
        #return max(self.phonebook.keys()) + 1
        return len(self.phonebook) + 1


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


    def edit_contact(self, contact_id: str, new_contact_data: list[str]):
        """Изменение контакта"""
        try:
            contact_id = int(contact_id)
            if contact_id not in self.phonebook:
                print_message(view.id_not_found)
                return None
            updated_fields = {}
            for i, field in enumerate(self.FIELDS):
                if new_contact_data[i]:
                    updated_fields[field] = new_contact_data[i].strip()
            self.phonebook[contact_id].update(updated_fields)
            return self.phonebook[contact_id]["name"]
        except KeyError:
            print_message(view.error_format)
        except Exception as e:
            print_message(f"Ошибка при редактировании контакта: {e}")


    def delete_contact(self, contact_id: str):
        """Удаление контакта"""
        try:
            contact_id = int(contact_id)
            if contact_id not in self.phonebook:
                print_message(view.id_not_found)
                return None
            deleted_contact = self.phonebook.pop(contact_id)
            return deleted_contact["name"]
        except Exception as e:
            print_message(f"Ошибка при удалении контакта: {e}")
