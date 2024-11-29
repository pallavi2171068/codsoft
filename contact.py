# Contact Management System

class Contact:
    def __init__(self, store_name, phone, email, address):
        self.store_name = store_name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Store Name: {self.store_name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone, email, address):
        contact = Contact(store_name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact for {store_name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.store_name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.store_name.lower() or search_term in contact.phone]
        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for contact in results:
                print(contact)

    def update_contact(self, store_name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.store_name.lower() == store_name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact for {store_name} updated successfully.")
                return
        print(f"Contact for {store_name} not found.")

    def delete_contact(self, store_name):
        for contact in self.contacts:
            if contact.store_name.lower() == store_name.lower():
                self.contacts.remove(contact)
                print(f"Contact for {store_name} deleted successfully.")
                return
        print(f"Contact for {store_name} not found.")


def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_name = input("Enter store name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter physical address: ")
            manager.add_contact(store_name, phone, email, address)

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == "4":
            store_name = input("Enter the store name to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ") or None
            new_email = input("Enter new email address (leave blank to keep current): ") or None
            new_address = input("Enter new address (leave blank to keep current): ") or None
            manager.update_contact(store_name, new_phone, new_email, new_address)

        elif choice == "5":
            store_name = input("Enter the store name to delete: ")
            manager.delete_contact(store_name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
