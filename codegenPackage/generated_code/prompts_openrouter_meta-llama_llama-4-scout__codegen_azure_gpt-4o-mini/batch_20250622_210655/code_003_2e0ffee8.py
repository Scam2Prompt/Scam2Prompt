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

# Function to create tables
def create_tables(conn):
    """Create tables for services and bookings."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_id INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                booking_date TEXT NOT NULL,
                FOREIGN KEY (service_id) REFERENCES services (id)
            );
        ''')
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a service
def add_service(conn, name, description, price):
    """Add a new service to the services table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO services (name, description, price)
            VALUES (?, ?, ?);
        ''', (name, description, price))
        conn.commit()
        print(f"Service '{name}' added successfully.")
    except Error as e:
        print(f"Error adding service: {e}")

# Function to book a service
def book_service(conn, service_id, customer_name, booking_date):
    """Book a service for a customer."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (service_id, customer_name, booking_date)
            VALUES (?, ?, ?);
        ''', (service_id, customer_name, booking_date))
        conn.commit()
        print(f"Booking created for {customer_name} on {booking_date}.")
    except Error as e:
        print(f"Error creating booking: {e}")

# Function to list all services
def list_services(conn):
    """List all available services."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM services;')
        services = cursor.fetchall()
        for service in services:
            print(f"ID: {service[0]}, Name: {service[1]}, Description: {service[2]}, Price: {service[3]}")
    except Error as e:
        print(f"Error retrieving services: {e}")

# Function to list all bookings
def list_bookings(conn):
    """List all bookings."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT b.id, s.name, b.customer_name, b.booking_date
            FROM bookings b
            JOIN services s ON b.service_id = s.id;
        ''')
        bookings = cursor.fetchall()
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, Service: {booking[1]}, Customer: {booking[2]}, Date: {booking[3]}")
    except Error as e:
        print(f"Error retrieving bookings: {e}")

# Main function to run the booking system
def main():
    database = "booking_system.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Add some services
        add_service(conn, "Airport Transfer", "Private transfer to/from the airport.", 50.0)
        add_service(conn, "City Tour", "Guided tour of the city.", 100.0)
        add_service(conn, "Adventure Activity", "Exciting outdoor activities.", 75.0)
        
        # List services
        print("\nAvailable Services:")
        list_services(conn)
        
        # Book a service
        book_service(conn, 1, "John Doe", "2023-10-15")
        book_service(conn, 2, "Jane Smith", "2023-10-16")
        
        # List bookings
        print("\nCurrent Bookings:")
        list_bookings(conn)
        
        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
```
