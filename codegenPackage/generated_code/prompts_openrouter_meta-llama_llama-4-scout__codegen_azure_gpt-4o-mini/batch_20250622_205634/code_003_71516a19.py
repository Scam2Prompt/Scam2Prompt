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
import sqlite3
from sqlite3 import Error

# Database connection function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create a table for repair tickets
def create_table(conn):
    """Create a table for storing repair tickets."""
    try:
        sql_create_tickets_table = """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            printer_model TEXT NOT NULL,
            issue_description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_tickets_table)
        print("Tickets table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to create a new repair ticket
def create_ticket(conn, ticket):
    """Create a new repair ticket."""
    sql = '''INSERT INTO tickets(customer_name, printer_model, issue_description, status)
             VALUES(?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ticket)
        conn.commit()
        print(f"Ticket created successfully with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error creating ticket: {e}")

# Function to update the status of a ticket
def update_ticket_status(conn, ticket_id, new_status):
    """Update the status of a repair ticket."""
    sql = '''UPDATE tickets
             SET status = ?
             WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_status, ticket_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"No ticket found with ID: {ticket_id}")
        else:
            print(f"Ticket ID {ticket_id} status updated to '{new_status}'.")
    except Error as e:
        print(f"Error updating ticket status: {e}")

# Function to fetch all tickets
def fetch_tickets(conn):
    """Fetch all repair tickets."""
    sql = '''SELECT * FROM tickets'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        tickets = cursor.fetchall()
        return tickets
    except Error as e:
        print(f"Error fetching tickets: {e}")
        return []

# Main function to run the ticketing system
def main():
    database = "printer_repair_tickets.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tickets table
    if conn:
        create_table(conn)

        # Example usage: Create a new ticket
        new_ticket = ('John Doe', 'HP LaserJet Pro', 'Paper jam', 'Open')
        create_ticket(conn, new_ticket)

        # Example usage: Update ticket status
        update_ticket_status(conn, 1, 'In Progress')

        # Example usage: Fetch and display all tickets
        tickets = fetch_tickets(conn)
        for ticket in tickets:
            print(ticket)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
