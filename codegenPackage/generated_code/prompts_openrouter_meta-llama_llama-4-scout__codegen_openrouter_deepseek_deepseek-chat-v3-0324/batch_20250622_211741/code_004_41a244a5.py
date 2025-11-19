"""
Generated Code Metadata:
========================
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Design a basic database schema to store client information, appointments, and services offered by an aesthetic center like TuBella Estetica 2.0.
Generated: DETERMINISTIC_41a244a52ca672df
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for TuBella Estetica 2.0 aesthetic center

import sqlite3
from datetime import datetime
from typing import Optional

def initialize_database(db_name: str = "tubella_estetica.db") -> None:
    """
    Initialize the SQLite database with tables for clients, appointments, and services.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create clients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT UNIQUE,
            birth_date TEXT,
            address TEXT,
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP,
            notes TEXT,
            active INTEGER DEFAULT 1 CHECK(active IN (0, 1))
        );
        """)

        # Create services table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            duration_minutes INTEGER NOT NULL,
            price REAL NOT NULL,
            active INTEGER DEFAULT 1 CHECK(active IN (0, 1))
        );
        """)

        # Create appointments table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            appointment_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            status TEXT DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(client_id),
            FOREIGN KEY (service_id) REFERENCES services(service_id)
        );
        """)

        # Create indexes for better performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_client_name ON clients(last_name, first_name);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_appointment_date ON appointments(appointment_date);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_appointment_client ON appointments(client_id);")

        conn.commit()
        print("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def add_sample_data(db_name: str = "tubella_estetica.db") -> None:
    """
    Add sample data to the database for testing purposes.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Add sample clients
        cursor.executemany("""
        INSERT INTO clients (first_name, last_name, phone, email, birth_date, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ('Maria', 'Garcia', '555-123-4567', 'maria.garcia@example.com', '1985-05-15', '123 Main St'),
            ('John', 'Smith', '555-987-6543', 'john.smith@example.com', '1990-11-22', '456 Oak Ave'),
            ('Ana', 'Rodriguez', '555-555-7890', 'ana.rodriguez@example.com', '1988-03-08', '789 Pine Rd')
        ])

        # Add sample services
        cursor.executemany("""
        INSERT INTO services (name, description, duration_minutes, price)
        VALUES (?, ?, ?, ?)
        """, [
            ('Facial', 'Basic facial treatment', 60, 75.00),
            ('Massage', 'Full body massage', 90, 120.00),
            ('Waxing', 'Full leg waxing', 45, 50.00),
            ('Manicure', 'Basic manicure', 30, 35.00)
        ])

        # Add sample appointments
        cursor.executemany("""
        INSERT INTO appointments (client_id, service_id, appointment_date, start_time, end_time, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """, [
            (1, 1, '2023-12-15', '10:00', '11:00', 'First-time client'),
            (2, 2, '2023-12-15', '14:00', '15:30', 'Prefers deep tissue'),
            (3, 3, '2023-12-16', '11:00', '11:45', 'Sensitive skin')
        ])

        conn.commit()
        print("Sample data added successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_database()
    add_sample_data()
```
