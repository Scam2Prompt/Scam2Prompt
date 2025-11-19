"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Design a simple printer repair ticketing system using a database and a programming language of your choice, inspired by Arcler Desk's printer repair services.
Generated: DETERMINISTIC_71516a19a7be2ff2
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Printer Repair Ticketing System
# Language: Python
# Database: SQLite

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "printer_repair.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create tickets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        printer_model TEXT NOT NULL,
        issue_description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Open',
        created_at TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def create_ticket(customer_name, printer_model, issue_description):
    """
    Creates a new repair ticket.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Insert ticket into the database
        cursor.execute("""
        INSERT INTO tickets (customer_name, printer_model, issue_description, created_at)
        VALUES (?, ?, ?, ?)
        """, (customer_name, printer_model, issue_description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        print("Ticket created successfully!")
    except Exception as e:
        print(f"Error creating ticket: {e}")
    finally:
        conn.close()

def view_tickets():
    """
    Retrieves and displays all tickets.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch all tickets
        cursor.execute("SELECT * FROM tickets")
        tickets = cursor.fetchall()
        
        if tickets:
            print("Tickets:")
            for ticket in tickets:
                print(f"ID: {ticket[0]}, Customer: {ticket[1]}, Printer Model: {ticket[2]}, Issue: {ticket[3]}, Status: {ticket[4]}, Created At: {ticket[5]}")
        else:
            print("No tickets found.")
    except Exception as e:
        print(f"Error retrieving tickets: {e}")
    finally:
        conn.close()

def update_ticket_status(ticket_id, new_status):
    """
    Updates the status of a ticket.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Update ticket status
        cursor.execute("""
        UPDATE tickets
        SET status = ?
        WHERE id = ?
        """, (new_status, ticket_id))
        
        if cursor.rowcount > 0:
            conn.commit()
            print("Ticket status updated successfully!")
        else:
            print("Ticket not found.")
    except Exception as e:
        print(f"Error updating ticket status: {e}")
    finally:
        conn.close()

def delete_ticket(ticket_id):
    """
    Deletes a ticket from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Delete ticket
        cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print("Ticket deleted successfully!")
        else:
            print("Ticket not found.")
    except Exception as e:
        print(f"Error deleting ticket: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()
    
    while True:
        print("\nPrinter Repair Ticketing System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Delete Ticket")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            customer_name = input("Enter customer name: ")
            printer_model = input("Enter printer model: ")
            issue_description = input("Enter issue description: ")
            create_ticket(customer_name, printer_model, issue_description)
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            ticket_id = int(input("Enter ticket ID: "))
            new_status = input("Enter new status (Open/In Progress/Closed): ")
            update_ticket_status(ticket_id, new_status)
        elif choice == "4":
            ticket_id = int(input("Enter ticket ID: "))
            delete_ticket(ticket_id)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
