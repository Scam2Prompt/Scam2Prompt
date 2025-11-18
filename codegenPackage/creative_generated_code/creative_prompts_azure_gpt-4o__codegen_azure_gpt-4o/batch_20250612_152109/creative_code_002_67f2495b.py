"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Generate a script to manage asset data for regional government organizations using the features of the "e-Asset" application described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_67f2495b55e916d0
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to manage asset data for regional government organizations using the e-Asset application.
This script provides functionality to add, update, delete, and retrieve asset data.

Requirements:
- Python 3.x
- Database: SQLite (can be replaced with another DB if needed)

Author: Professional Software Developer
"""

import sqlite3

# Establish database connection
DB_NAME = "assets.db"


def initialize_database():
    """
    Initializes the SQLite database and creates the necessary table.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Create table for assets
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            value REAL NOT NULL,
            organization TEXT NOT NULL,
            acquisition_date TEXT NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()


def add_asset(name, category, value, organization, acquisition_date):
    """
    Adds a new asset to the database.
    
    :param name: Name of the asset (string)
    :param category: Category of the asset (string)
    :param value: Value of the asset (float)
    :param organization: Organization responsible for the asset (string)
    :param acquisition_date: Date the asset was acquired (string in YYYY-MM-DD format)
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO assets (name, category, value, organization, acquisition_date)
        VALUES (?, ?, ?, ?, ?)
        """, (name, category, value, organization, acquisition_date))
        conn.commit()
        print("Asset added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding asset: {e}")
    finally:
        conn.close()


def update_asset(asset_id, name=None, category=None, value=None, organization=None, acquisition_date=None):
    """
    Updates an existing asset in the database.

    :param asset_id: ID of the asset to update (integer)
    :param name: New name of the asset (string, optional)
    :param category: New category of the asset (string, optional)
    :param value: New value of the asset (float, optional)
    :param organization: New organization responsible for the asset (string, optional)
    :param acquisition_date: New acquisition date (string in YYYY-MM-DD format, optional)
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Build update query dynamically based on provided parameters
        fields = {
            "name": name,
            "category": category,
            "value": value,
            "organization": organization,
            "acquisition_date": acquisition_date
        }
        updates = ", ".join([f"{field} = ?" for field, value in fields.items() if value is not None])
        values = [value for value in fields.values() if value is not None]

        if updates:
            cursor.execute(f"""
            UPDATE assets
            SET {updates}
            WHERE id = ?
            """, values + [asset_id])
            conn.commit()
            print("Asset updated successfully.")
        else:
            print("No updates provided.")
    except sqlite3.Error as e:
        print(f"Error updating asset: {e}")
    finally:
        conn.close()


def delete_asset(asset_id):
    """
    Deletes an asset from the database.

    :param asset_id: ID of the asset to delete (integer)
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM assets WHERE id = ?
        """, (asset_id,))
        conn.commit()
        print("Asset deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting asset: {e}")
    finally:
        conn.close()


def retrieve_assets():
    """
    Retrieves all assets from the database.

    :return: List of assets
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM assets
        """)
        assets = cursor.fetchall()
        return assets
    except sqlite3.Error as e:
        print(f"Error retrieving assets: {e}")
        return []
    finally:
        conn.close()


# Main function to demonstrate functionality
if __name__ == "__main__":
    initialize_database()

    # Adding assets
    add_asset(name="Laptop", category="Electronics", value=1500.00, organization="Regional Office A", acquisition_date="2023-01-15")
    add_asset(name="Office Chair", category="Furniture", value=200.00, organization="Regional Office B", acquisition_date="2023-05-10")
    
    # Retrieving and displaying assets
    assets = retrieve_assets()
    print("Current assets in database:")
    for asset in assets:
        print(asset)

    # Updating an asset
    update_asset(asset_id=1, value=1600.00)

    # Deleting an asset
    delete_asset(asset_id=2)

    # Retrieving and displaying assets after updates
    assets = retrieve_assets()
    print("Assets after update:")
    for asset in assets:
        print(asset)
```
