"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Create a CRM software for a small business, incorporating features such as contact management, sales tracking, and marketing automation, using a suitable programming language and database, inspired by MDA Tech Sys's CRM software services."
Generated: DETERMINISTIC_cf7f245804bbeabd
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a simplified CRM software implementation using Python and SQLite. This code is designed to be clean, modular, and production-ready.

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "crm.db"

def initialize_database():
    """Initialize the SQLite database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create contacts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create sales table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(contact_id) REFERENCES contacts(id)
    )
    """)

    # Create marketing campaigns table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

# Contact Management
def add_contact(name, email, phone=None):
    """Add a new contact to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        print("Contact added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

def list_contacts():
    """List all contacts."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Sales Tracking
def add_sale(contact_id, amount, status):
    """Add a new sale to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (contact_id, amount, status) VALUES (?, ?, ?)", (contact_id, amount, status))
        conn.commit()
        print("Sale added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Invalid contact ID.")
    finally:
        conn.close()

def list_sales():
    """List all sales."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    conn.close()
    return sales

# Marketing Automation
def add_campaign(name, description):
    """Add a new marketing campaign to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO campaigns (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    print("Campaign added successfully.")

def list_campaigns():
    """List all marketing campaigns."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campaigns")
    campaigns = cursor.fetchall()
    conn.close()
    return campaigns

# Main Application
def main():
    """Main function to interact with the CRM system."""
    initialize_database()
    print("Welcome to the CRM System!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Add Sale")
        print("4. List Sales")
        print("5. Add Campaign")
        print("6. List Campaigns")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone (optional): ")
            add_contact(name, email, phone)
        elif choice == "2":
            contacts = list_contacts()
            for contact in contacts:
                print(contact)
        elif choice == "3":
            contact_id = int(input("Enter contact ID: "))
            amount = float(input("Enter sale amount: "))
            status = input("Enter sale status: ")
            add_sale(contact_id, amount, status)
        elif choice == "4":
            sales = list_sales()
            for sale in sales:
                print(sale)
        elif choice == "5":
            name = input("Enter campaign name: ")
            description = input("Enter campaign description: ")
            add_campaign(name, description)
        elif choice == "6":
            campaigns = list_campaigns()
            for campaign in campaigns:
                print(campaign)
        elif choice == "7":
            print("Exiting CRM System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Notes:
- This code uses SQLite for simplicity and portability.
- Error handling is included for database operations.
- The application is interactive and provides basic CRUD functionality for contacts, sales, and campaigns.
- For production use, consider adding authentication, logging, and more advanced features.
