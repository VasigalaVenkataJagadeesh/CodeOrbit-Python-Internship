"""
Task 4: File Handling Mini Project
A simple contacts manager using a CSV file.
Features: add, view, and search contacts.
"""

import csv
from pathlib import Path

CONTACTS_FILE = Path("contacts.csv")
FIELDNAMES = ["name", "phone", "email"]


def ensure_file_exists():
    """Create the CSV file with headers if it does not exist."""
    if not CONTACTS_FILE.exists():
        with CONTACTS_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_contacts():
    """Read contacts from the CSV file."""
    ensure_file_exists()
    try:
        with CONTACTS_FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except (OSError, csv.Error) as error:
        print(f"Could not read contacts: {error}")
        return []


def add_contact():
    """Collect contact details and append one record to the CSV file."""
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    try:
        ensure_file_exists()
        with CONTACTS_FILE.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow({"name": name, "phone": phone, "email": email})
        print("Contact saved.")
    except (OSError, csv.Error) as error:
        print(f"Could not save contact: {error}")


def view_contacts():
    """Display all saved contacts."""
    contacts = read_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n=== Saved Contacts ===")
    for number, contact in enumerate(contacts, start=1):
        print(
            f"{number}. {contact.get('name', '')} | "
            f"Phone: {contact.get('phone', '')} | "
            f"Email: {contact.get('email', '')}"
        )


def search_contacts():
    """Search contacts by name or phone number."""
    query = input("Enter a name or phone number to search: ").strip().lower()
    if not query:
        print("Search text cannot be empty.")
        return

    matches = [
        contact for contact in read_contacts()
        if query in contact.get("name", "").lower()
        or query in contact.get("phone", "").lower()
    ]

    if matches:
        print("\n=== Search Results ===")
        for contact in matches:
            print(
                f"{contact.get('name', '')} | "
                f"Phone: {contact.get('phone', '')} | "
                f"Email: {contact.get('email', '')}"
            )
    else:
        print("No matching contacts found.")


def main():
    ensure_file_exists()

    while True:
        print("\n=== Contacts Manager ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
