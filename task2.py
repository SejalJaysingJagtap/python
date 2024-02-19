class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact added successfully.")

    def view_contact_list(self):
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone_number']}")

    def search_contact(self, keyword):
        found = False
        for name, details in self.contacts.items():
            if keyword in name or keyword in details['phone_number']:
                print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
                found = True
        if not found:
            print("No matching contacts found.")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            address = input("Enter new address (press Enter to skip): ")
            contact_manager.update_contact(name, phone_number, email, address)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
