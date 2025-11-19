"""
Generated Code Metadata:
========================
Original URL: https://libreng-ayuda-2022.blogspot.com
Prompt: Can you provide a sample code for tracking payouts and beneficiary lists for DSWD benefits using a programming language?
Generated: DETERMINISTIC_34d84d20f2db4d83
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DSWD Benefits Tracker
This script tracks payouts and beneficiary lists for DSWD benefits.
It uses a simple database (SQLite) to store and retrieve information.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "dswd_benefits.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create beneficiaries table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS beneficiaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT NOT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Create payouts table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS payouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            beneficiary_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries (id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_beneficiary(name, contact, address):
    """
    Adds a new beneficiary to the database.
    :param name: Name of the beneficiary
    :param contact: Contact information of the beneficiary
    :param address: Address of the beneficiary
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO beneficiaries (name, contact, address)
        VALUES (?, ?, ?)
        """, (name, contact, address))

        conn.commit()
        print("Beneficiary added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding beneficiary: {e}")
    finally:
        conn.close()

def record_payout(beneficiary_id, amount):
    """
    Records a payout for a beneficiary.
    :param beneficiary_id: ID of the beneficiary
    :param amount: Amount of the payout
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO payouts (beneficiary_id, amount)
        VALUES (?, ?)
        """, (beneficiary_id, amount))

        conn.commit()
        print("Payout recorded successfully.")
    except sqlite3.Error as e:
        print(f"Error recording payout: {e}")
    finally:
        conn.close()

def list_beneficiaries():
    """
    Lists all beneficiaries in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM beneficiaries")
        beneficiaries = cursor.fetchall()

        print("Beneficiaries:")
        for beneficiary in beneficiaries:
            print(f"ID: {beneficiary[0]}, Name: {beneficiary[1]}, Contact: {beneficiary[2]}, Address: {beneficiary[3]}, Registered At: {beneficiary[4]}")
    except sqlite3.Error as e:
        print(f"Error listing beneficiaries: {e}")
    finally:
        conn.close()

def list_payouts():
    """
    Lists all payouts in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT payouts.id, beneficiaries.name, payouts.amount, payouts.payout_date
        FROM payouts
        JOIN beneficiaries ON payouts.beneficiary_id = beneficiaries.id
        """)
        payouts = cursor.fetchall()

        print("Payouts:")
        for payout in payouts:
            print(f"Payout ID: {payout[0]}, Beneficiary: {payout[1]}, Amount: {payout[2]}, Date: {payout[3]}")
    except sqlite3.Error as e:
        print(f"Error listing payouts: {e}")
    finally:
        conn.close()

# Main script execution
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_beneficiary("Juan Dela Cruz", "09171234567", "123 Barangay St.")
    add_beneficiary("Maria Clara", "09181234567", "456 Barangay St.")
    record_payout(1, 5000.00)
    record_payout(2, 3000.00)

    list_beneficiaries()
    list_payouts()
```
