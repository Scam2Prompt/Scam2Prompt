"""
Generated Code Metadata:
========================
Original URL: https://toc.fantasytransfers.com
Prompt: Design a system to manage bookings for various services, including airport transfers, tours, and activities, using a database and a programming language like Python or Node.js.
Generated: DETERMINISTIC_2e0ffee89e064088
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "booking_system.db"

def initialize_database():
    """
    Initialize the database with tables for services and bookings.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create services table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    """)

    # Create bookings table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_id INTEGER NOT NULL,
        customer_name TEXT NOT NULL,
        customer_email TEXT NOT NULL,
        booking_date TEXT NOT NULL,
        FOREIGN KEY (service_id) REFERENCES services (id)
    )
    """)

    conn.commit()
    conn.close()

# Service management
def add_service(name, description, price):
    """
    Add a new service to the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO services (name, description, price)
        VALUES (?, ?, ?)
        """, (name, description, price))
        conn.commit()
        print("Service added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding service: {e}")
    finally:
        conn.close()

def list_services():
    """
    List all available services.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM services")
        services = cursor.fetchall()
        for service in services:
            print(f"ID: {service[0]}, Name: {service[1]}, Description: {service[2]}, Price: ${service[3]:.2f}")
    except sqlite3.Error as e:
        print(f"Error listing services: {e}")
    finally:
        conn.close()

# Booking management
def create_booking(service_id, customer_name, customer_email, booking_date):
    """
    Create a new booking for a service.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        # Validate service exists
        cursor.execute("SELECT * FROM services WHERE id = ?", (service_id,))
        service = cursor.fetchone()
        if not service:
            print("Service not found.")
            return

        # Insert booking
        cursor.execute("""
        INSERT INTO bookings (service_id, customer_name, customer_email, booking_date)
        VALUES (?, ?, ?, ?)
        """, (service_id, customer_name, customer_email, booking_date))
        conn.commit()
        print("Booking created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating booking: {e}")
    finally:
        conn.close()

def list_bookings():
    """
    List all bookings.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT bookings.id, services.name, bookings.customer_name, bookings.customer_email, bookings.booking_date
        FROM bookings
        JOIN services ON bookings.service_id = services.id
        """)
        bookings = cursor.fetchall()
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, Service: {booking[1]}, Customer: {booking[2]}, Email: {booking[3]}, Date: {booking[4]}")
    except sqlite3.Error as e:
        print(f"Error listing bookings: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()

    print("Welcome to the Booking System!")
    while True:
        print("\nOptions:")
        print("1. Add Service")
        print("2. List Services")
        print("3. Create Booking")
        print("4. List Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter service name: ")
            description = input("Enter service description: ")
            price = float(input("Enter service price: "))
            add_service(name, description, price)
        elif choice == "2":
            list_services()
        elif choice == "3":
            service_id = int(input("Enter service ID: "))
            customer_name = input("Enter customer name: ")
            customer_email = input("Enter customer email: ")
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            try:
                # Validate date format
                datetime.strptime(booking_date, "%Y-%m-%d")
                create_booking(service_id, customer_name, customer_email, booking_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "4":
            list_bookings()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
