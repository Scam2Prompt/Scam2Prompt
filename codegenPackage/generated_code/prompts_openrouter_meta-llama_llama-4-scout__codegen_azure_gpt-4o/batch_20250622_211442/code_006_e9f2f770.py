"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Develop a plan for implementing a customer relationship management (CRM) system for a company like Hanil Furniture Gallery, taking into account their focus on customer satisfaction and design excellence.
Generated: DETERMINISTIC_e9f2f770a03a053d
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CRM System Implementation Plan for Hanil Furniture Gallery
This script outlines a basic structure for a CRM system focused on customer satisfaction and design excellence.
The system includes customer management, order tracking, and feedback collection.
"""

# Import necessary libraries
import sqlite3  # For database management
from datetime import datetime  # For handling timestamps
import logging  # For logging errors and system events

# Configure logging
logging.basicConfig(
    filename='crm_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database setup
DB_NAME = "hanil_crm.db"

def initialize_database():
    """
    Initialize the database with necessary tables for the CRM system.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create Customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT UNIQUE NOT NULL,
                Phone TEXT,
                Address TEXT,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create Orders table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                CustomerID INTEGER NOT NULL,
                ProductName TEXT NOT NULL,
                Quantity INTEGER NOT NULL,
                OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
            )
        ''')

        # Create Feedback table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Feedback (
                FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
                CustomerID INTEGER NOT NULL,
                FeedbackText TEXT NOT NULL,
                Rating INTEGER CHECK(Rating >= 1 AND Rating <= 5),
                SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
            )
        ''')

        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization failed: {e}")
    finally:
        conn.close()

def add_customer(name, email, phone=None, address=None):
    """
    Add a new customer to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Customers (Name, Email, Phone, Address)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, address))

        conn.commit()
        logging.info(f"Customer added: {name}, {email}")
    except sqlite3.IntegrityError as e:
        logging.error(f"Failed to add customer (duplicate email): {e}")
    except sqlite3.Error as e:
        logging.error(f"Failed to add customer: {e}")
    finally:
        conn.close()

def add_order(customer_id, product_name, quantity):
    """
    Add a new order for a customer.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Orders (CustomerID, ProductName, Quantity)
            VALUES (?, ?, ?)
        ''', (customer_id, product_name, quantity))

        conn.commit()
        logging.info(f"Order added for CustomerID {customer_id}: {product_name} x{quantity}")
    except sqlite3.Error as e:
        logging.error(f"Failed to add order: {e}")
    finally:
        conn.close()

def add_feedback(customer_id, feedback_text, rating):
    """
    Add feedback from a customer.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Feedback (CustomerID, FeedbackText, Rating)
            VALUES (?, ?, ?)
        ''', (customer_id, feedback_text, rating))

        conn.commit()
        logging.info(f"Feedback added for CustomerID {customer_id}: {feedback_text} (Rating: {rating})")
    except sqlite3.Error as e:
        logging.error(f"Failed to add feedback: {e}")
    finally:
        conn.close()

def get_customer_details(customer_id):
    """
    Retrieve details of a specific customer.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Customers WHERE CustomerID = ?
        ''', (customer_id,))
        customer = cursor.fetchone()

        if customer:
            logging.info(f"Customer details retrieved for CustomerID {customer_id}")
            return customer
        else:
            logging.warning(f"No customer found with CustomerID {customer_id}")
            return None
    except sqlite3.Error as e:
        logging.error(f"Failed to retrieve customer details: {e}")
        return None
    finally:
        conn.close()

def get_all_customers():
    """
    Retrieve all customers from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()

        logging.info("All customers retrieved successfully.")
        return customers
    except sqlite3.Error as e:
        logging.error(f"Failed to retrieve customers: {e}")
        return []
    finally:
        conn.close()

# Main execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    add_customer("John Doe", "john.doe@example.com", "123-456-7890", "123 Elm Street")
    add_customer("Jane Smith", "jane.smith@example.com", "987-654-3210", "456 Oak Avenue")

    add_order(1, "Modern Sofa", 2)
    add_order(2, "Dining Table", 1)

    add_feedback(1, "Great quality and design!", 5)
    add_feedback(2, "Delivery was delayed, but the product is excellent.", 4)

    # Retrieve and print all customers
    customers = get_all_customers()
    for customer in customers:
        print(customer)
```
