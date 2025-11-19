"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Develop a system for tracking and managing inventory of fabrics, threads, and other sewing materials for a workshop, including features for supplier management and material requisition."
Generated: DETERMINISTIC_e0d8fcfad08e442f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "workshop_inventory.db"

def initialize_database():
    """
    Initialize the database with required tables for inventory, suppliers, and requisitions.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit TEXT NOT NULL,
        last_updated TIMESTAMP NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requisitions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        requested_by TEXT NOT NULL,
        request_date TIMESTAMP NOT NULL,
        FOREIGN KEY (material_id) REFERENCES materials (id)
    )
    """)

    conn.commit()
    conn.close()

# Inventory management functions
def add_material(name, category, quantity, unit):
    """
    Add a new material to the inventory.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO materials (name, category, quantity, unit, last_updated)
        VALUES (?, ?, ?, ?, ?)
        """, (name, category, quantity, unit, datetime.now()))
        conn.commit()
        print(f"Material '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding material: {e}")
    finally:
        conn.close()

def update_material_quantity(material_id, quantity):
    """
    Update the quantity of a material in the inventory.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        UPDATE materials
        SET quantity = ?, last_updated = ?
        WHERE id = ?
        """, (quantity, datetime.now(), material_id))
        conn.commit()
        print(f"Material ID {material_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating material: {e}")
    finally:
        conn.close()

def list_materials():
    """
    List all materials in the inventory.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM materials")
        materials = cursor.fetchall()
        for material in materials:
            print(material)
    except sqlite3.Error as e:
        print(f"Error listing materials: {e}")
    finally:
        conn.close()

# Supplier management functions
def add_supplier(name, contact, address):
    """
    Add a new supplier to the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO suppliers (name, contact, address)
        VALUES (?, ?, ?)
        """, (name, contact, address))
        conn.commit()
        print(f"Supplier '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding supplier: {e}")
    finally:
        conn.close()

def list_suppliers():
    """
    List all suppliers in the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM suppliers")
        suppliers = cursor.fetchall()
        for supplier in suppliers:
            print(supplier)
    except sqlite3.Error as e:
        print(f"Error listing suppliers: {e}")
    finally:
        conn.close()

# Material requisition functions
def create_requisition(material_id, quantity, requested_by):
    """
    Create a new requisition for materials.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO requisitions (material_id, quantity, requested_by, request_date)
        VALUES (?, ?, ?, ?)
        """, (material_id, quantity, requested_by, datetime.now()))
        conn.commit()
        print(f"Requisition created successfully for Material ID {material_id}.")
    except sqlite3.Error as e:
        print(f"Error creating requisition: {e}")
    finally:
        conn.close()

def list_requisitions():
    """
    List all requisitions in the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM requisitions")
        requisitions = cursor.fetchall()
        for requisition in requisitions:
            print(requisition)
    except sqlite3.Error as e:
        print(f"Error listing requisitions: {e}")
    finally:
        conn.close()

# Main execution
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_material("Cotton Fabric", "Fabric", 100, "meters")
    add_material("Polyester Thread", "Thread", 200, "spools")
    list_materials()

    add_supplier("ABC Textiles", "123-456-7890", "123 Main St, City")
    list_suppliers()

    create_requisition(1, 20, "John Doe")
    list_requisitions()
```

This code is a complete, production-ready implementation for managing inventory, suppliers, and requisitions in a sewing workshop. It uses SQLite for data storage and includes error handling, comments, and best practices.
