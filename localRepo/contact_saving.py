contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for name, info in contacts.items():
        print(f"{name}: Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book")
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = int(input("Choose an option: "))
    if choice >= 6:
        print("sorry you have only 5 choices !\n Refresh again please!")
        break

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
 