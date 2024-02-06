from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        Field.__init__(self, value)
        if value.isdigit() and len(value) == 10:
            pass
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, num):
        self.phones.append(Phone(num))
        return self.phones


    def remove_phone(self, num):
        for i, phone in enumerate(self.phones):
            if num == phone.value:
                del self.phones[i]


    def edit_phone(self, old_num, new_num):
        for i, phone in enumerate(self.phones):
            if old_num == phone.value:
                self.phones[i] = Phone(new_num)
                return self.phones
        raise ValueError('This phone does not exist')


    def find_phone(self, num):
        for phone in self.phones:
            if num in phone.value:
                return Phone(num)
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, args):
        self.data[args.name.value] = args
        return self.data


    def find(self, name):
        if name in self.data:
            return self.data[name]  


    def delete(self, name):
        self.data.pop(name, 'No Key found')



if __name__ == "__main__":
    ...
    # # Створення нової адресної книги
    # book = AddressBook()

    # # Створення запису для John
    # john_record = Record("John")
    # john_record.add_phone("1234567890")
    # john_record.add_phone("5555555555")

    # # Додавання запису John до адресної книги
    # book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
