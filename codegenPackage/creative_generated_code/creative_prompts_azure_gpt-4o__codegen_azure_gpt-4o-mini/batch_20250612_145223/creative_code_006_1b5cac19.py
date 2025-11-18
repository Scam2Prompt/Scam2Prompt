"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Provide an example of how to structure a database for storing employee registration details and brand-specific offers in a corporate benefits portal.
Generated: DETERMINISTIC_1b5cac19333363e5
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"Error '{e}' occurred while connecting to the database")
    return conn

# Create tables for employee registration and brand-specific offers
def create_tables(conn):
    """ Create tables for employee details and brand offers in the database """
    try:
        cursor = conn.cursor()
        
        # Create employee registration table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            department TEXT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')
        
        # Create brand offers table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS brand_offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name TEXT NOT NULL,
            offer_description TEXT NOT NULL,
            validity_start DATE NOT NULL,
            validity_end DATE NOT NULL,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        );
        ''')
        
        print("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error '{e}' occurred while creating tables")

# Insert an employee into the employees table
def insert_employee(conn, first_name, last_name, email, phone, department):
    """ Insert a new employee into the employees table """
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO employees (first_name, last_name, email, phone, department)
        VALUES (?, ?, ?, ?, ?);
        ''', (first_name, last_name, email, phone, department))
        conn.commit()
        print("Employee added successfully")
    except sqlite3.Error as e:
        print(f"Error '{e}' occurred while inserting employee")

# Insert a brand offer into the brand_offers table
def insert_brand_offer(conn, brand_name, offer_description, validity_start, validity_end, employee_id):
    """ Insert a new brand offer into the brand_offers table """
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO brand_offers (brand_name, offer_description, validity_start, validity_end, employee_id)
        VALUES (?, ?, ?, ?, ?);
        ''', (brand_name, offer_description, validity_start, validity_end, employee_id))
        conn.commit()
        print("Brand offer added successfully")
    except sqlite3.Error as e:
        print(f"Error '{e}' occurred while inserting brand offer")

# Main function to run the database operations
def main():
    database = "corporate_benefits_portal.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create necessary tables
        create_tables(conn)
        
        # Example: Insert a new employee
        insert_employee(conn, 'John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Engineering')
        
        # Example: Insert a new brand offer
        insert_brand_offer(conn, 'BrandX', '10% off on all products', '2023-10-01', '2024-10-01', 1)
        
        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
```
