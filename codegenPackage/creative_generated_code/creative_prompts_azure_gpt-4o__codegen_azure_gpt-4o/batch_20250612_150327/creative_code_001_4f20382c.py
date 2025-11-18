"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Recommend an API or library for tracking FSC-certified material purchases, similar to the process described by PDC Brush.
Generated: DETERMINISTIC_4f20382cb4806d68
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Python program that tracks FSC-certified material purchases using a database for storage. For this example, SQLite is used as the database, and the `sqlite3` library is utilized. The program defines functions to add and retrieve FSC-certified purchases.

```python
import sqlite3

# Constants
DB_FILE = "fsc_materials.db"

# Initialize database schema
def initialize_database():
    """
    Initializes the SQLite database with a table for tracking FSC-certified materials.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create a table if it does not already exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            supplier TEXT NOT NULL,
            certification_code TEXT NOT NULL,
            purchase_date TEXT NOT NULL
        )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

# Add a purchase record
def add_fsc_purchase(item_name, quantity, supplier, certification_code, purchase_date):
    """
    Adds a new FSC-certified material purchase to the database.
    
    :param item_name: Name of the purchased item.
    :param quantity: Quantity purchased.
    :param supplier: Supplier name.
    :param certification_code: FSC certification code.
    :param purchase_date: Date of purchase (format: YYYY-MM-DD).
    :return: None
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO purchases (item_name, quantity, supplier, certification_code, purchase_date)
        VALUES (?, ?, ?, ?, ?)
        ''', (item_name, quantity, supplier, certification_code, purchase_date))
        conn.commit()
        print("Purchase added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding purchase: {e}")
    finally:
        if conn:
            conn.close()

# Retrieve all purchase records
def get_all_purchases():
    """
    Retrieves all FSC-certified material purchases from the database.
    
    :return: List of purchase records.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM purchases')
        purchases = cursor.fetchall()

        # Print the purchases in a readable format
        for purchase in purchases:
            print(f"ID: {purchase[0]}, Item: {purchase[1]}, Quantity: {purchase[2]}, "
                  f"Supplier: {purchase[3]}, Certification Code: {purchase[4]}, "
                  f"Date: {purchase[5]}")
        return purchases
    except sqlite3.Error as e:
        print(f"Error retrieving purchases: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Main program execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample data (this would typically come from user input or an external system)
    add_fsc_purchase("FSC Wooden Brush", 100, "EcoBrush Suppliers", "FSC-C123456", "2023-10-01")
    add_fsc_purchase("FSC Bamboo Handle", 200, "Green Bamboo Co.", "FSC-C654321", "2023-10-15")

    # Retrieve and display all purchases
    print("\nAll FSC-certified purchases:")
    get_all_purchases()
```

### Features:
1. **Database Initialization:** Creates a table to store purchase records if it does not already exist.
2. **Add Purchase Functionality:** Allows adding new FSC-certified material purchases with necessary details.
3. **Retrieve Purchases Functionality:** Retrieves and displays all stored purchase records.
4. **Error Handling:** Includes error handling for database operations.
5. **Production-Ready Design:** Code is modular and follows Python best practices.

To run this program:
1. Save the code to a `.py` file.
2. Run the program using Python 3. It will create an SQLite database file (`fsc_materials.db`) in the same directory.
3. Modify the `add_fsc_purchase` calls or create input mechanisms for production use.
