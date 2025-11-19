"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Suggest tools or libraries to implement a customer relationship management system that emphasizes post-sale support, as described in Maxnet Telecom's approach.
Generated: DETERMINISTIC_20da512121fe855b
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime

class CRM:
    """
    A simple customer relationship management system.
    """

    def __init__(self, db_name):
        """
        Initialize the CRM system with a database.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS support_tickets
            (id INTEGER PRIMARY KEY, customer_id INTEGER, issue TEXT, status TEXT, created_at TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions
            (id INTEGER PRIMARY KEY, ticket_id INTEGER, interaction TEXT, created_at TEXT,
            FOREIGN KEY (ticket_id) REFERENCES support_tickets (id))
        ''')

        self.conn.commit()

    def add_customer(self, name, email, phone):
        """
        Add a new customer to the system.

        Args:
            name (str): The customer's name.
            email (str): The customer's email.
            phone (str): The customer's phone number.

        Returns:
            int: The ID of the newly added customer.
        """
        try:
            self.cursor.execute('INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")
            return None

    def add_support_ticket(self, customer_id, issue):
        """
        Add a new support ticket for a customer.

        Args:
            customer_id (int): The ID of the customer.
            issue (str): The issue described by the customer.

        Returns:
            int: The ID of the newly added support ticket.
        """
        try:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute('INSERT INTO support_tickets (customer_id, issue, status, created_at) VALUES (?, ?, ?, ?)', 
                                (customer_id, issue, "Open", created_at))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding support ticket: {e}")
            return None

    def add_interaction(self, ticket_id, interaction):
        """
        Add a new interaction to a support ticket.

        Args:
            ticket_id (int): The ID of the support ticket.
            interaction (str): The interaction with the customer.

        Returns:
            int: The ID of the newly added interaction.
        """
        try:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute('INSERT INTO interactions (ticket_id, interaction, created_at) VALUES (?, ?, ?)', 
                                (ticket_id, interaction, created_at))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding interaction: {e}")
            return None

    def get_customer(self, customer_id):
        """
        Get a customer's information.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            tuple: The customer's information.
        """
        try:
            self.cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error getting customer: {e}")
            return None

    def get_support_ticket(self, ticket_id):
        """
        Get a support ticket's information.

        Args:
            ticket_id (int): The ID of the support ticket.

        Returns:
            tuple: The support ticket's information.
        """
        try:
            self.cursor.execute('SELECT * FROM support_tickets WHERE id = ?', (ticket_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error getting support ticket: {e}")
            return None

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    crm = CRM("crm.db")

    # Add a customer
    customer_id = crm.add_customer("John Doe", "john@example.com", "123-456-7890")
    print(f"Customer ID: {customer_id}")

    # Add a support ticket
    ticket_id = crm.add_support_ticket(customer_id, "Issue with product")
    print(f"Support Ticket ID: {ticket_id}")

    # Add an interaction
    interaction_id = crm.add_interaction(ticket_id, "Responded to customer")
    print(f"Interaction ID: {interaction_id}")

    # Get customer information
    customer = crm.get_customer(customer_id)
    print(f"Customer: {customer}")

    # Get support ticket information
    ticket = crm.get_support_ticket(ticket_id)
    print(f"Support Ticket: {ticket}")

    crm.close_connection()


if __name__ == "__main__":
    main()
```
