"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: Write a script to create a database schema for storing tour package details (e.g., package name, destination, and price) and car rental options (e.g., car model, AC/non-AC) for Balaji Tours & Travels.
Generated: DETERMINISTIC_6a2ff4b841ce6eea
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """Create tables for tour packages and car rentals"""
    try:
        cursor = conn.cursor()
        
        # Create tour_packages table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tour_packages (
                package_id INTEGER PRIMARY KEY AUTOINCREMENT,
                package_name TEXT NOT NULL,
                destination TEXT NOT NULL,
                duration_days INTEGER NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        
        # Create car_rentals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS car_rentals (
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_model TEXT NOT NULL,
                ac_available BOOLEAN NOT NULL CHECK (ac_available IN (0, 1)),
                seating_capacity INTEGER NOT NULL,
                price_per_day REAL NOT NULL,
                available BOOLEAN NOT NULL DEFAULT 1 CHECK (available IN (0, 1)),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        
        # Create package_car_mapping table for many-to-many relationship
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS package_car_mapping (
                mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
                package_id INTEGER NOT NULL,
                car_id INTEGER NOT NULL,
                FOREIGN KEY (package_id) REFERENCES tour_packages (package_id)
                    ON DELETE CASCADE,
                FOREIGN KEY (car_id) REFERENCES car_rentals (car_id)
                    ON DELETE CASCADE,
                UNIQUE(package_id, car_id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully")
    except Error as e:
        print(f"Error creating tables: {e}")

def main():
    database = "balaji_tours_travels.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn is not None:
        # Create tables
        create_tables(conn)
        
        # Close the connection
        conn.close()
        print("Database connection closed")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
