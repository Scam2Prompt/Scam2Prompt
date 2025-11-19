"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Develop a lost and found pet management system, inspired by the services provided by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_72c5201fe3f52e90
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Lost and Found Pet Management System
Inspired by Circle of Friends Animal Shelter
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "lost_and_found_pets.db"

def initialize_database():
    """
    Initialize the database and create necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create table for lost pets
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lost_pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        breed TEXT,
        color TEXT,
        last_seen_location TEXT NOT NULL,
        date_lost TEXT NOT NULL,
        contact_info TEXT NOT NULL
    )
    """)
    
    # Create table for found pets
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS found_pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species TEXT NOT NULL,
        breed TEXT,
        color TEXT,
        found_location TEXT NOT NULL,
        date_found TEXT NOT NULL,
        contact_info TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def add_lost_pet(name, species, breed, color, last_seen_location, date_lost, contact_info):
    """
    Add a lost pet to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO lost_pets (name, species, breed, color, last_seen_location, date_lost, contact_info)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, species, breed, color, last_seen_location, date_lost, contact_info))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding lost pet: {e}")
    finally:
        conn.close()

def add_found_pet(species, breed, color, found_location, date_found, contact_info):
    """
    Add a found pet to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO found_pets (species, breed, color, found_location, date_found, contact_info)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (species, breed, color, found_location, date_found, contact_info))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding found pet: {e}")
    finally:
        conn.close()

def search_lost_pets(species=None, breed=None, color=None):
    """
    Search for lost pets based on optional filters.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = "SELECT * FROM lost_pets WHERE 1=1"
        params = []
        
        if species:
            query += " AND species = ?"
            params.append(species)
        if breed:
            query += " AND breed = ?"
            params.append(breed)
        if color:
            query += " AND color = ?"
            params.append(color)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error searching lost pets: {e}")
        return []
    finally:
        conn.close()

def search_found_pets(species=None, breed=None, color=None):
    """
    Search for found pets based on optional filters.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = "SELECT * FROM found_pets WHERE 1=1"
        params = []
        
        if species:
            query += " AND species = ?"
            params.append(species)
        if breed:
            query += " AND breed = ?"
            params.append(breed)
        if color:
            query += " AND color = ?"
            params.append(color)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error searching found pets: {e}")
        return []
    finally:
        conn.close()

def display_pets(pets):
    """
    Display a list of pets in a readable format.
    """
    if not pets:
        print("No pets found.")
        return
    
    for pet in pets:
        print("-" * 40)
        for key, value in zip(["ID", "Name", "Species", "Breed", "Color", "Location", "Date", "Contact Info"], pet):
            print(f"{key}: {value}")
        print("-" * 40)

# Main program
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    add_lost_pet("Buddy", "Dog", "Golden Retriever", "Golden", "Central Park", str(datetime.now().date()), "555-1234")
    add_found_pet("Dog", "Golden Retriever", "Golden", "Central Park", str(datetime.now().date()), "555-5678")
    
    print("Lost Pets:")
    lost_pets = search_lost_pets(species="Dog")
    display_pets(lost_pets)
    
    print("Found Pets:")
    found_pets = search_found_pets(species="Dog")
    display_pets(found_pets)
```
