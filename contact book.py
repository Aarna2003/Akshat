# Contact book 
contacts = []


def add_contact():
    print("\nAdd a New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    
    print(f"Contact for {name} added!\n")


def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts found!")
    else:
        print("\nAll Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    print("\nSearch Contact")
    search = input("Enter name or phone number to search: ")
    
    found = False
    for contact in contacts:
        if contact['name'].lower() == search.lower() or contact['phone'] == search:
            print(f"\nFound Contact:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break

    if not found:
        print("No contact found with that information.\n")


def update_contact():
    print("\nUpdate Contact")
    search = input("Enter name of the contact to update: ")
    
    for contact in contacts:
        if contact['name'].lower() == search.lower():
            print("What do you want to update?")
            contact['name'] = input("New name: ")
            contact['phone'] = input("New phone number: ")
            contact['email'] = input("New email: ")
            contact['address'] = input("New address: ")
            print(f"Contact for {contact['name']} updated!\n")
            return
    
    print("No contact found with that name.\n")


def delete_contact():
    print("\nDelete Contact")
    search = input("Enter name of the contact to delete: ")
    
    for contact in contacts:
        if contact['name'].lower() == search.lower():
            contacts.remove(contact)
            print(f"Contact for {contact['name']} deleted!\n")
            return

    print("No contact found with that name.\n")


def contact_book():
    print("Your Contact Book")

    while True:
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("End")
            break
        else:
            print("That's not a valid option. Try again.\n")

if __name__ == "__main__":
    contact_book()
