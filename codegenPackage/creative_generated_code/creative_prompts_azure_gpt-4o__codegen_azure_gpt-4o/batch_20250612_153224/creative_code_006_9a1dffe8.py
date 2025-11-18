"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Develop a software solution for managing outsourced labor contracts in the public sector, considering Licitare's "Terceirização de Mão de Obra" offerings.
Generated: DETERMINISTIC_9a1dffe804cefb8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Software solution for managing outsourced labor contracts in the public sector.
This script provides a basic implementation for creating, updating, viewing, and deleting
labor contracts while considering Licitare's "Terceirização de Mão de Obra" offerings.

Dependencies:
- Python 3.8+
- SQLite3 (for database management)

Author: Expert Programmer
Date: YYYY-MM-DD
Version: 1.0
"""

import sqlite3
from datetime import datetime

# Database file name
DATABASE_FILE = "labor_contracts.db"

# Initialize the database
def initialize_database():
    """
    Creates the necessary table for storing labor contracts if it doesn't already exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contractor_name TEXT NOT NULL,
                contract_details TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Create a new contract
def create_contract(contractor_name, contract_details, start_date, end_date):
    """
    Adds a new labor contract to the database.
    
    Args:
        contractor_name (str): Name of the contractor.
        contract_details (str): Details of the contract.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        bool: True if the operation succeeded, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO contracts (contractor_name, contract_details, start_date, end_date, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (contractor_name, contract_details, start_date, end_date, created_at))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating contract: {e}")
        return False
    finally:
        conn.close()

# View all contracts
def view_contracts():
    """
    Retrieves and displays all labor contracts stored in the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contracts")
        contracts = cursor.fetchall()
        for contract in contracts:
            print(f"ID: {contract[0]}, Contractor: {contract[1]}, Details: {contract[2]}, "
                  f"Start Date: {contract[3]}, End Date: {contract[4]}, Created At: {contract[5]}, "
                  f"Updated At: {contract[6]}")
    except sqlite3.Error as e:
        print(f"Error viewing contracts: {e}")
    finally:
        conn.close()

# Update a contract
def update_contract(contract_id, contractor_name=None, contract_details=None, start_date=None, end_date=None):
    """
    Updates an existing labor contract in the database.
    
    Args:
        contract_id (int): ID of the contract to update.
        contractor_name (str, optional): New contractor name.
        contract_details (str, optional): New contract details.
        start_date (str, optional): New start date in YYYY-MM-DD format.
        end_date (str, optional): New end date in YYYY-MM-DD format.

    Returns:
        bool: True if the operation succeeded, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fields_to_update = []
        values = []
        
        if contractor_name:
            fields_to_update.append("contractor_name = ?")
            values.append(contractor_name)
        if contract_details:
            fields_to_update.append("contract_details = ?")
            values.append(contract_details)
        if start_date:
            fields_to_update.append("start_date = ?")
            values.append(start_date)
        if end_date:
            fields_to_update.append("end_date = ?")
            values.append(end_date)
        
        values.append(updated_at)
        values.append(contract_id)
        
        if fields_to_update:
            query = f"UPDATE contracts SET {', '.join(fields_to_update)}, updated_at = ? WHERE id = ?"
            cursor.execute(query, tuple(values))
            conn.commit()
            return True
        else:
            print("No fields provided for update.")
            return False
    except sqlite3.Error as e:
        print(f"Error updating contract: {e}")
        return False
    finally:
        conn.close()

# Delete a contract
def delete_contract(contract_id):
    """
    Deletes a labor contract from the database.
    
    Args:
        contract_id (int): ID of the contract to delete.

    Returns:
        bool: True if the operation succeeded, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contracts WHERE id = ?", (contract_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting contract: {e}")
        return False
    finally:
        conn.close()

# Main function for demonstration purposes
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    print("Creating a new contract...")
    create_contract("Contractor ABC", "Details about the labor contract", "2023-01-01", "2023-12-31")
    
    print("\nViewing all contracts...")
    view_contracts()
    
    print("\nUpdating a contract...")
    update_contract(1, contractor_name="Contractor XYZ")
    
    print("\nViewing all contracts...")
    view_contracts()
    
    print("\nDeleting a contract...")
    delete_contract(1)
    
    print("\nViewing all contracts...")
    view_contracts()
```
