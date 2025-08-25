#code for contact book

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def search_contact():
    keyword = input("Enter name or phone/email to search: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone'] or keyword in c['email']]
    
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()
    else:
        print("\nNo matching contact found.\n")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print("Leave blank to keep existing value.")
            new_name = input(f"New name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New email [{contact['email']}]: ") or contact['email']
            
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email

            save_contacts(contacts)
            print("\nContact updated successfully!\n")
            return
    print("\nContact not found.\n")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name_to_delete.lower()]
    
    if len(contacts) == len(new_contacts):
        print("\nContact not found.\n")
    else:
        save_contacts(new_contacts)
        print(f"\nContact '{name_to_delete}' deleted successfully.\n")

def main_menu():
    while True:
        print("==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main_menu()
