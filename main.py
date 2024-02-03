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
        self.phones.append(num)
        return self.phones


    def remove_phone(self, num):
        if num in self.phones:
            self.phones.remove(num)


    def edit_phone(self, old_num, new_num):
        if old_num in self.phones:
            self.phones = list(
                map(lambda x: x.replace(old_num, new_num), self.phones))
            return self.phones
        else:
            raise ValueError


    def find_phone(self, num):
        if num in self.phones:
            return Phone(num)
        else:
            return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, args):
        self.data[str(args.name)] = args.phones


    def find(self, name):
        print(name, self.data, sep=' ### ')
        if name in self.data:
            return Record(name)  # Не розумію що тут повертати?


    def delete(self, name):
        delete_value = self.data.pop(name, 'No Key found')
        print(delete_value)


if __name__ == "__main__":
    ...
    