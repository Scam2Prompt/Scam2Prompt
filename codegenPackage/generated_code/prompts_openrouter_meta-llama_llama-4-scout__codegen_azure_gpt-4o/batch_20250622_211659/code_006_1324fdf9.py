"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Develop a customer relationship management (CRM) module for an ERP system, focusing on simplicity and ease of use, à la Sistemabox's solutions."
Generated: DETERMINISTIC_1324fdf9d80ba3aa
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CRM Module for ERP System
This module provides basic functionality for managing customer relationships, including
adding, updating, retrieving, and deleting customer records. The focus is on simplicity
and ease of use, following best practices for Python development.
"""

import sqlite3
from typing import List, Dict, Optional

# Database setup
DB_NAME = "crm.db"

def initialize_database():
    """
    Initializes the database and creates the customers table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                address TEXT
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# CRUD Operations
def add_customer(name: str, email: str, phone: Optional[str] = None, address: Optional[str] = None) -> bool:
    """
    Adds a new customer to the database.
    :param name: Customer's name
    :param email: Customer's email (must be unique)
    :param phone: Customer's phone number (optional)
    :param address: Customer's address (optional)
    :return: True if the operation was successful, False otherwise
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO customers (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, address))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")
        return False
    except sqlite3.Error as e:
        print(f"Error adding customer: {e}")
        return False
    finally:
        conn.close()

def update_customer(customer_id: int, name: Optional[str] = None, email: Optional[str] = None,
                    phone: Optional[str] = None, address: Optional[str] = None) -> bool:
    """
    Updates an existing customer's information.
    :param customer_id: ID of the customer to update
    :param name: New name (optional)
    :param email: New email (optional)
    :param phone: New phone number (optional)
    :param address: New address (optional)
    :return: True if the operation was successful, False otherwise
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        fields = []
        values = []
        if name:
            fields.append("name = ?")
            values.append(name)
        if email:
            fields.append("email = ?")
            values.append(email)
        if phone:
            fields.append("phone = ?")
            values.append(phone)
        if address:
            fields.append("address = ?")
            values.append(address)
        values.append(customer_id)
        query = f"UPDATE customers SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating customer: {e}")
        return False
    finally:
        conn.close()

def get_customer(customer_id: int) -> Optional[Dict[str, str]]:
    """
    Retrieves a customer's information by ID.
    :param customer_id: ID of the customer to retrieve
    :return: A dictionary containing the customer's information, or None if not found
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "address": row[4]
            }
        return None
    except sqlite3.Error as e:
        print(f"Error retrieving customer: {e}")
        return None
    finally:
        conn.close()

def delete_customer(customer_id: int) -> bool:
    """
    Deletes a customer from the database by ID.
    :param customer_id: ID of the customer to delete
    :return: True if the operation was successful, False otherwise
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error deleting customer: {e}")
        return False
    finally:
        conn.close()

def list_customers() -> List[Dict[str, str]]:
    """
    Retrieves a list of all customers in the database.
    :return: A list of dictionaries containing customer information
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "address": row[4]
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        print(f"Error listing customers: {e}")
        return []
    finally:
        conn.close()

# Initialize the database when the module is loaded
initialize_database()
```
