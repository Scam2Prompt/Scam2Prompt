"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Recommend a suitable database schema for managing plumbing services, including customer information, service requests, and payment history, similar to Certified Plumbers Graham, TX's operations."
Generated: DETERMINISTIC_096113c6936f4a6b
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema for Plumbing Services Management System

import sqlite3
from datetime import datetime
from typing import Optional

def create_database_schema(db_path: str = 'plumbing_services.db') -> None:
    """
    Creates the database schema for plumbing services management.
    Includes tables for customers, service requests, payments, and employees.
    
    Args:
        db_path: Path to the SQLite database file. Defaults to 'plumbing_services.db'.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create Customers table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            notes TEXT
        );
        ''')

        # Create Employees table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            specialization TEXT,
            hire_date DATE NOT NULL,
            is_active BOOLEAN DEFAULT 1
        );
        ''')

        # Create ServiceTypes table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_types (
            service_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            base_cost REAL NOT NULL
        );
        ''')

        # Create ServiceRequests table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            service_type_id INTEGER NOT NULL,
            employee_id INTEGER,
            request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            scheduled_date TIMESTAMP,
            completed_date TIMESTAMP,
            status TEXT CHECK(status IN ('Pending', 'Scheduled', 'In Progress', 'Completed', 'Cancelled')) DEFAULT 'Pending',
            problem_description TEXT NOT NULL,
            service_notes TEXT,
            total_cost REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        );
        ''')

        # Create Payments table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            payment_method TEXT CHECK(payment_method IN ('Cash', 'Credit Card', 'Check', 'Bank Transfer', 'Other')),
            status TEXT CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')) DEFAULT 'Pending',
            transaction_reference TEXT,
            FOREIGN KEY (request_id) REFERENCES service_requests(request_id)
        );
        ''')

        # Create Materials table (for tracking materials used in services)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS materials (
            material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            unit_cost REAL NOT NULL,
            unit_type TEXT NOT NULL,
            quantity_in_stock REAL DEFAULT 0
        );
        ''')

        # Create ServiceMaterials table (junction table for materials used in services)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_materials (
            service_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id INTEGER NOT NULL,
            material_id INTEGER NOT NULL,
            quantity_used REAL NOT NULL,
            FOREIGN KEY (request_id) REFERENCES service_requests(request_id),
            FOREIGN KEY (material_id) REFERENCES materials(material_id)
        );
        ''')

        conn.commit()
        print("Database schema created successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def initialize_sample_data(db_path: str = 'plumbing_services.db') -> None:
    """
    Populates the database with initial sample data for demonstration purposes.
    
    Args:
        db_path: Path to the SQLite database file. Defaults to 'plumbing_services.db'.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert sample customers
        cursor.executemany('''
        INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [
            ('John', 'Smith', 'john.smith@example.com', '555-123-4567', '123 Main St', 'Graham', 'TX', '76450', 'Regular customer'),
            ('Sarah', 'Johnson', 'sarah.j@example.com', '555-987-6543', '456 Oak Ave', 'Graham', 'TX', '76450', 'Prefers morning appointments'),
            ('Michael', 'Williams', 'michael.w@example.com', '555-456-7890', '789 Pine Rd', 'Newcastle', 'TX', '76372', 'New customer')
        ])

        # Insert sample employees
        cursor.executemany('''
        INSERT INTO employees (first_name, last_name, email, phone, specialization, hire_date)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', [
            ('Robert', 'Brown', 'robert.b@plumbing.com', '555-111-2222', 'Residential plumbing', '2020-01-15'),
            ('Jennifer', 'Davis', 'jennifer.d@plumbing.com', '555-333-4444', 'Commercial plumbing', '2019-05-20'),
            ('David', 'Miller', 'david.m@plumbing.com', '555-555-6666', 'Emergency services', '2021-03-10')
        ])

        # Insert sample service types
        cursor.executemany('''
        INSERT INTO service_types (name, description, base_cost)
        VALUES (?, ?, ?)
        ''', [
            ('Leak Repair', 'Repair of water leaks in pipes or fixtures', 99.99),
            ('Drain Cleaning', 'Clearing clogged drains', 79.99),
            ('Water Heater Installation', 'Installation of new water heater', 299.99),
            ('Emergency Service', '24/7 emergency plumbing services', 149.99)
        ])

        # Insert sample materials
        cursor.executemany('''
        INSERT INTO materials (name, description, unit_cost, unit_type, quantity_in_stock)
        VALUES (?, ?, ?, ?, ?)
        ''', [
            ('PVC Pipe 1/2"', '1/2 inch PVC pipe', 0.75, 'foot', 200),
            ('Copper Pipe 3/4"', '3/4 inch copper pipe', 2.50, 'foot', 150),
            ('Pipe Joint Compound', 'Sealant for pipe joints', 5.99, 'tube', 30),
            ('Water Heater Element', 'Heating element for water heaters', 24.99, 'each', 15)
        ])

        conn.commit()
        print("Sample data initialized successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database_schema()
    initialize_sample_data()
```
