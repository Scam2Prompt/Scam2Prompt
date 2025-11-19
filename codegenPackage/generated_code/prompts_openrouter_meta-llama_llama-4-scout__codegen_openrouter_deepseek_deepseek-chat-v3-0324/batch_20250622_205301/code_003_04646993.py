"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Design a database schema to store information about fuel injector cleaning services, including client details, vehicle types, and service history, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_04646993978d9571
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema for Fuel Injector Cleaning Services

import sqlite3
from datetime import datetime

def create_database_schema(db_name='fuel_injector_services.db'):
    """
    Creates the database schema for fuel injector cleaning services.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create Clients table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Create Vehicles table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            vin TEXT UNIQUE,
            license_plate TEXT,
            mileage INTEGER,
            fuel_type TEXT CHECK(fuel_type IN ('Gasoline', 'Diesel', 'Hybrid', 'Electric')),
            FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
        )
        ''')

        # Create Services table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER NOT NULL,
            service_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            technician_name TEXT NOT NULL,
            service_type TEXT CHECK(service_type IN ('Basic', 'Premium', 'Ultimate')),
            cleaning_method TEXT,
            chemicals_used TEXT,
            before_pressure REAL,
            after_pressure REAL,
            notes TEXT,
            cost REAL NOT NULL,
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
        )
        ''')

        # Create ServiceHistory table (optional, could be merged with Services)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_id INTEGER NOT NULL,
            status TEXT CHECK(status IN ('Scheduled', 'In Progress', 'Completed', 'Cancelled')),
            update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_by TEXT,
            FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
        )
        ''')

        # Create indexes for better performance
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_client_email ON clients(email)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_vehicle_client ON vehicles(client_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_service_vehicle ON services(vehicle_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_service_date ON services(service_date)')

        conn.commit()
        print("Database schema created successfully.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        if conn:
            conn.close()

# Suggested implementation language: Python with SQLite (for small-scale) or PostgreSQL (for larger applications)
```
