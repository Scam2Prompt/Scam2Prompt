"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Write a Python script that interacts with a database to manage customer information and service requests for an automotive repair business similar to Martelinho de Ouro 3M.
Generated: DETERMINISTIC_a5fbd4aa302eb548
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Constants for database file
DB_FILE = "automotive_repair.db"

def create_tables():
    """
    Create database tables for managing customers and service requests.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    # Create ServiceRequests table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ServiceRequests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES Customers (id)
        )
    ''')

    connection.commit()
    connection.close()

def add_customer(name, email, phone):
    """
    Adds a new customer to the database.
    :param name: Customer's name
    :param email: Customer's email address
    :param phone: Customer's phone number
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Customers (name, email, phone) VALUES (?, ?, ?)
        ''', (name, email, phone))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding customer: {e}")
    finally:
        connection.close()

def add_service_request(customer_id, description, status='Pending'):
    """
    Adds a new service request for a customer.
    :param customer_id: ID of the customer
    :param description: Description of the service request
    :param status: Status of the service request (default is 'Pending')
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO ServiceRequests (customer_id, description, status)
            VALUES (?, ?, ?)
        ''', (customer_id, description, status))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding service request: {e}")
    finally:
        connection.close()

def list_customers():
    """
    Lists all customers in the database.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Customers')
    customers = cursor.fetchall()
    connection.close()
    return customers

def list_service_requests():
    """
    Lists all service requests in the database.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ServiceRequests')
    service_requests = cursor.fetchall()
    connection.close()
    return service_requests

def update_service_request_status(service_request_id, new_status):
    """
    Updates the status of a service request.
    :param service_request_id: ID of the service request
    :param new_status: New status ('Pending', 'In Progress', 'Completed')
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE ServiceRequests SET status = ? WHERE id = ?
        ''', (new_status, service_request_id))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error updating service request: {e}")
    finally:
        connection.close()

# Main script
if __name__ == "__main__":
    create_tables()

    # Example usage
    add_customer("John Doe", "johndoe@example.com", "555-1234")
    add_customer("Jane Smith", "janesmith@example.com", "555-5678")

    customers = list_customers()
    print("Customers:")
    for customer in customers:
        print(customer)

    add_service_request(customer_id=1, description="Fix dent on passenger door")
    add_service_request(customer_id=2, description="Replace windshield")

    service_requests = list_service_requests()
    print("\nService Requests:")
    for request in service_requests:
        print(request)

    update_service_request_status(service_request_id=1, new_status="In Progress")
    print("\nUpdated Service Requests:")
    for request in list_service_requests():
        print(request)
```
