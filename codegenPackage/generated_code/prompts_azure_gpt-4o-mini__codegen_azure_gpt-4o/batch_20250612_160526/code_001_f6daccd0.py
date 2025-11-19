"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: How can I implement a recycling management system that tracks electronic waste, inspired by the practices of SCR Reciclados?
Generated: DETERMINISTIC_f6daccd07b85d5c6
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recycling Management System for Electronic Waste
Inspired by SCR Reciclados
This system tracks electronic waste items, their categories, and recycling status.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "recycling_management.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create table for electronic waste items
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS electronic_waste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            weight_kg REAL NOT NULL,
            recycling_status TEXT NOT NULL CHECK(recycling_status IN ('Pending', 'Recycled')),
            date_added TEXT NOT NULL
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_waste_item(name, category, weight_kg):
    """
    Adds a new electronic waste item to the database.
    :param name: Name of the waste item
    :param category: Category of the waste item (e.g., "Battery", "Monitor", "Phone")
    :param weight_kg: Weight of the waste item in kilograms
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Insert new waste item
        cursor.execute("""
        INSERT INTO electronic_waste (name, category, weight_kg, recycling_status, date_added)
        VALUES (?, ?, ?, 'Pending', ?)
        """, (name, category, weight_kg, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        print(f"Successfully added waste item: {name}")
    except sqlite3.Error as e:
        print(f"Error adding waste item: {e}")
    finally:
        conn.close()

def update_recycling_status(item_id, status):
    """
    Updates the recycling status of a waste item.
    :param item_id: ID of the waste item
    :param status: New recycling status ('Pending' or 'Recycled')
    """
    if status not in ['Pending', 'Recycled']:
        print("Invalid status. Must be 'Pending' or 'Recycled'.")
        return
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Update recycling status
        cursor.execute("""
        UPDATE electronic_waste
        SET recycling_status = ?
        WHERE id = ?
        """, (status, item_id))
        
        if cursor.rowcount == 0:
            print(f"No waste item found with ID: {item_id}")
        else:
            conn.commit()
            print(f"Successfully updated recycling status for item ID: {item_id}")
    except sqlite3.Error as e:
        print(f"Error updating recycling status: {e}")
    finally:
        conn.close()

def list_waste_items():
    """
    Lists all electronic waste items in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch all waste items
        cursor.execute("SELECT * FROM electronic_waste")
        items = cursor.fetchall()
        
        if items:
            print("Electronic Waste Items:")
            print("ID | Name | Category | Weight (kg) | Status | Date Added")
            print("-" * 60)
            for item in items:
                print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]}")
        else:
            print("No waste items found.")
    except sqlite3.Error as e:
        print(f"Error listing waste items: {e}")
    finally:
        conn.close()

def delete_waste_item(item_id):
    """
    Deletes a waste item from the database.
    :param item_id: ID of the waste item to delete
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Delete waste item
        cursor.execute("DELETE FROM electronic_waste WHERE id = ?", (item_id,))
        
        if cursor.rowcount == 0:
            print(f"No waste item found with ID: {item_id}")
        else:
            conn.commit()
            print(f"Successfully deleted waste item with ID: {item_id}")
    except sqlite3.Error as e:
        print(f"Error deleting waste item: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    add_waste_item("Old Phone", "Phone", 0.5)
    add_waste_item("Laptop Battery", "Battery", 1.2)
    list_waste_items()
    update_recycling_status(1, "Recycled")
    list_waste_items()
    delete_waste_item(2)
    list_waste_items()
```
