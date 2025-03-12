class Contact:
    # Initializes a contact with name, phone number, and email
    def __init__(self, name, phone, email):
        self.name = name
        self.phone_number = phone
        self.email = email

    # Returns a string representation of the contact
    def __str__(self):
        return f"Name: {self.name}, \nPhone number: {self.phone_number}, \nEmail: {self.email}\n"


# Factory function to create a Contact object
def contact_factory(name, phone, email):
    return Contact(name, phone, email)


class ContactContainer:
    # Static method to create a contact using the factory function
    @staticmethod
    def contactinfo(name, phone, email):
        return contact_factory(name, phone, email)


class ContactManager:
    def __init__(self):
        # Initializes the contact list with some sample contacts
        self.contacts = [
            contact_factory("Josh Gabriel Austria", "09074498248", "jooshaustria13@gmail.com"),
            contact_factory("Shai-Gilgeous Alexander", "09202445673", "Shai13@gmail.com"),
            contact_factory("Benj Monesia", "09994826379", "benj18@gmail.com")
        ]
        print("Contact List:\n")
        self.display_contacts()

    # Adds a new contact to the list
    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        contact = ContactContainer.contactinfo(name, phone, email)
        self.contacts.insert(0, contact)  # Adds the new contact at the top
        print("\nContact added successfully!")
        print("\nUpdated Contact List:\n")
        self.display_contacts()

    # Removes a contact by name
    def remove_contact(self):
        name = input("Enter the name of the contact to remove: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"\nContact {name} removed successfully.")
                print("\nUpdated Contact List:")
                self.display_contacts()
                return
        print("\nContact not found.\n")

    # Searches for a contact by name
    def search_contact(self):
        name = input("Enter the name to search: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found:")
                print(contact)
                return
        print("\nContact not found.\n")

    # Displays all contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contact is available.")
        else:
            for contact in self.contacts:
                print(contact)

    # Lists contacts in alphabetical order
    def list_contacts(self):
        if not self.contacts:
            print("No contact is available.")
        else:
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.name.lower())
            print("\nSorted Contact List:\n")
            for contact in sorted_contacts:
                print(contact)


# Main function to manage user interaction
def main():
    manage = ContactManager()

    while True:
        print("Options:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Remove Contact")
        print("4. List Contacts\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage.add_contact()
        elif choice == "2":
            manage.search_contact()
        elif choice == "3":
            manage.remove_contact()
        elif choice == "4":
            manage.list_contacts()
        else:
            print("Invalid choice. Please try again.\n")


# Runs the program
if __name__ == "__main__":
    main()
