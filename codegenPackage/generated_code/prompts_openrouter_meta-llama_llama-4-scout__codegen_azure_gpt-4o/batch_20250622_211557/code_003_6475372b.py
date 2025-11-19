"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Develop a donation tracking system using a suitable programming language, incorporating features like donor information, contribution amounts, and vehicle specifications, inspired by Dysnix's fundraising efforts.
Generated: DETERMINISTIC_6475372bf6900e82
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Donation Tracking System
# Language: Python
# This script tracks donor information, contribution amounts, and vehicle specifications.

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "donation_tracking.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create donors table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
        """)
        
        # Create donations table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (donor_id) REFERENCES donors (id)
        )
        """)
        
        # Create vehicles table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_id INTEGER NOT NULL,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            FOREIGN KEY (donor_id) REFERENCES donors (id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_donor(name, email, phone=None):
    """
    Adds a new donor to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO donors (name, email, phone)
        VALUES (?, ?, ?)
        """, (name, email, phone))
        
        conn.commit()
        print("Donor added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Donor with this email already exists.")
    except sqlite3.Error as e:
        print(f"Error adding donor: {e}")
    finally:
        conn.close()

def add_donation(donor_email, amount):
    """
    Adds a donation to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Get donor ID
        cursor.execute("SELECT id FROM donors WHERE email = ?", (donor_email,))
        donor = cursor.fetchone()
        
        if donor:
            donor_id = donor[0]
            cursor.execute("""
            INSERT INTO donations (donor_id, amount, date)
            VALUES (?, ?, ?)
            """, (donor_id, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            
            conn.commit()
            print("Donation added successfully.")
        else:
            print("Error: Donor not found.")
    except sqlite3.Error as e:
        print(f"Error adding donation: {e}")
    finally:
        conn.close()

def add_vehicle(donor_email, make, model, year):
    """
    Adds a vehicle donation to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Get donor ID
        cursor.execute("SELECT id FROM donors WHERE email = ?", (donor_email,))
        donor = cursor.fetchone()
        
        if donor:
            donor_id = donor[0]
            cursor.execute("""
            INSERT INTO vehicles (donor_id, make, model, year)
            VALUES (?, ?, ?, ?)
            """, (donor_id, make, model, year))
            
            conn.commit()
            print("Vehicle added successfully.")
        else:
            print("Error: Donor not found.")
    except sqlite3.Error as e:
        print(f"Error adding vehicle: {e}")
    finally:
        conn.close()

def view_donors():
    """
    Displays all donors in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM donors")
        donors = cursor.fetchall()
        
        print("Donors:")
        for donor in donors:
            print(donor)
    except sqlite3.Error as e:
        print(f"Error retrieving donors: {e}")
    finally:
        conn.close()

def view_donations():
    """
    Displays all donations in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT donors.name, donations.amount, donations.date
        FROM donations
        JOIN donors ON donations.donor_id = donors.id
        """)
        donations = cursor.fetchall()
        
        print("Donations:")
        for donation in donations:
            print(donation)
    except sqlite3.Error as e:
        print(f"Error retrieving donations: {e}")
    finally:
        conn.close()

def view_vehicles():
    """
    Displays all vehicle donations in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT donors.name, vehicles.make, vehicles.model, vehicles.year
        FROM vehicles
        JOIN donors ON vehicles.donor_id = donors.id
        """)
        vehicles = cursor.fetchall()
        
        print("Vehicle Donations:")
        for vehicle in vehicles:
            print(vehicle)
    except sqlite3.Error as e:
        print(f"Error retrieving vehicles: {e}")
    finally:
        conn.close()

# Main execution
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    add_donor("John Doe", "john.doe@example.com", "123-456-7890")
    add_donation("john.doe@example.com", 100.0)
    add_vehicle("john.doe@example.com", "Toyota", "Camry", 2020)
    
    view_donors()
    view_donations()
    view_vehicles()
```
