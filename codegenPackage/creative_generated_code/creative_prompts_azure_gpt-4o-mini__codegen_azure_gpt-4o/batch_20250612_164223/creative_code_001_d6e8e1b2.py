"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: How can I implement a hybrid phone system for a restaurant using Retail Tech Solutions' recommendations?
Generated: DETERMINISTIC_d6e8e1b27c5701a4
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hybrid Phone System Implementation for a Restaurant

This script implements a basic hybrid phone system for a restaurant based on 
Retail Tech Solutions' recommendations. The system supports taking orders 
via phone and integrating them with an online order management system.

Requirements:
- Handle incoming phone orders.
- Save orders to a database.
- Validate order details.
- Send notifications to staff for phone orders.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sqlite3
from datetime import datetime
import logging

# Setting up logging for error handling and debugging
logging.basicConfig(
    filename='hybrid_phone_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database connection setup
DB_FILE = 'restaurant_orders.db'

def initialize_database():
    """
    Initializes the SQLite database to store orders if not already created.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create orders table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            order_details TEXT NOT NULL,
            time_of_order TEXT NOT NULL
        )
        """)
        conn.commit()
        logging.info("Database initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

def save_order_to_database(customer_name, phone_number, order_details):
    """
    Saves the phone order to the database.

    Args:
        customer_name (str): Name of the customer.
        phone_number (str): Customer's phone number.
        order_details (str): Details of the order.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Insert order into the database
        cursor.execute("""
        INSERT INTO Orders (customer_name, phone_number, order_details, time_of_order)
        VALUES (?, ?, ?, ?)
        """, (customer_name, phone_number, order_details, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        logging.info(f"Order saved: {customer_name}, {phone_number}, {order_details}")
    except Exception as e:
        logging.error(f"Error saving order to database: {e}")
    finally:
        conn.close()

def notify_staff(order_details):
    """
    Sends a notification to the restaurant staff about the phone order.
    
    Args:
        order_details (str): Details of the order.
    """
    try:
        # Simulate staff notification (e.g., via SMS or email)
        logging.info(f"Staff notified about order: {order_details}")
    except Exception as e:
        logging.error(f"Error notifying staff: {e}")

def take_phone_order():
    """
    Simulates taking a phone order from a customer.
    """
    try:
        # Collecting order details from the customer
        customer_name = input("Enter customer name: ")
        phone_number = input("Enter phone number: ")
        order_details = input("Enter order details: ")

        # Validate inputs (basic validation)
        if not customer_name or not phone_number or not order_details:
            logging.warning("Invalid order details provided.")
            print("Invalid input. Please try again.")
            return
        
        # Save the order to the database
        save_order_to_database(customer_name, phone_number, order_details)

        # Notify staff about the order
        notify_staff(order_details)

        print("Order processed successfully!")
    except Exception as e:
        logging.error(f"Error taking phone order: {e}")
        print("An error occurred while processing the order. Please try again.")

if __name__ == "__main__":
    # Initialize database on startup
    initialize_database()

    print("Welcome to the Restaurant Hybrid Phone System!")
    while True:
        print("\nMenu:")
        print("1. Take Phone Order")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            take_phone_order()
        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
