import json

contacts = {}


def menu():
    print("\n--- JSON CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Save contacts")
    print("4. Load contacts")
    print("5. Exit")


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    if not name or not phone:
        print("Name and phone cannot be empty")
        return

    contacts[name] = phone

    print("Contact added successfully")


def view_contacts():
    if not contacts:
        print("No contacts found")
        return

    for name, phone in contacts.items():
        print(f"Name: {name} | Phone: {phone}")


def save_contacts():
    file=open("contacts.json", "w")

    json.dump(contacts, file, indent=4)

    file.close()

    print("Contacts saved successfully")


def load_contacts():
    global contacts

    try:
        file=open("contacts.json", "r")

        contacts=json.load(file)

        file.close()

        print("contacts loaded successfully")

    except FileNotFoundError:
        print("No saved contacts found")


while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        add_contact()

    elif option == "2":
        view_contacts()

    elif option == "3":
        save_contacts()

    elif option == "4":
        load_contacts()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
