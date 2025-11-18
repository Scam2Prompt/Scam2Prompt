"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Write a Python script to create a database schema for managing craft beer subscription boxes, including tables for customer information, beer types, and delivery schedules.
Generated: DETERMINISTIC_57825399cb326fd6
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Define the database file name
DATABASE_FILE = 'craft_beer_subscription.db'

def create_database():
    """
    Creates a SQLite database with tables for managing craft beer subscription boxes.
    Tables include:
    - Customers: Stores customer information
    - BeerTypes: Stores details about craft beer types
    - DeliverySchedules: Tracks delivery schedules for customers
    """
    try:
        # Connect to the SQLite database (creates the file if it does not exist)
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Create Customers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE,
            Phone TEXT,
            Address TEXT NOT NULL
        );
        """)

        # Create BeerTypes table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS BeerTypes (
            BeerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Description TEXT,
            ABV REAL NOT NULL, -- Alcohol By Volume
            Brewery TEXT NOT NULL
        );
        """)

        # Create DeliverySchedules table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS DeliverySchedules (
            DeliveryID INTEGER PRIMARY KEY AUTOINCREMENT,
            CustomerID INTEGER NOT NULL,
            BeerID INTEGER NOT NULL,
            DeliveryDate DATE NOT NULL,
            Quantity INTEGER NOT NULL,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (BeerID) REFERENCES BeerTypes(BeerID)
        );
        """)

        # Commit changes
        conn.commit()
        print("Database and tables created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while creating the database: {e}")
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database()
```
