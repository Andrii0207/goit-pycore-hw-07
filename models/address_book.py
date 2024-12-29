from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        if name in self.data:
            return self.data[name]

    def show_all(self):
        contact_list = []

        for name, record in self.data.items():
            contact = dict()
            contact[name] = [phone.value for phone in record.phones]
            contact_list.append(contact)
        return contact_list

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def remove_phone(self, deleted_phone):
        print("remove_phone: ", deleted_phone)
        # next(
        #     (phone for phone in self.phones if phone.value == deleted_phone), None)
