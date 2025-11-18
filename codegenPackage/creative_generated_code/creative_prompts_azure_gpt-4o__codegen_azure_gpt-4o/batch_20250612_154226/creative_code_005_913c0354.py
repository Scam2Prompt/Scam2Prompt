"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Generate code for tracking the source of client acquisition (e.g., call, social networks, recommendation) as described on the Proximus client site.
Generated: DETERMINISTIC_913c03545c02bbcf
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = "client_acquisition.db"

# Create or connect to the database
def initialize_database():
    """Initialize the database and create tables if they do not exist."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create the table for client acquisition data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS client_acquisition (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT NOT NULL,
                source TEXT NOT NULL,
                acquisition_date TEXT NOT NULL
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        if conn:
            conn.close()

# Add a new client acquisition record
def add_client_acquisition(client_name, source):
    """
    Add a new client acquisition entry to the database.

    Args:
        client_name (str): Name of the client.
        source (str): Source of acquisition (e.g., call, social networks, recommendation).
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Validate input
        if not client_name or not source:
            raise ValueError("Client name and source cannot be empty.")

        # Insert the client acquisition record
        acquisition_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO client_acquisition (client_name, source, acquisition_date)
            VALUES (?, ?, ?)
        """, (client_name, source, acquisition_date))

        conn.commit()
        print("Client acquisition record added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    finally:
        if conn:
            conn.close()

# Fetch all client acquisition records
def fetch_client_acquisition_records():
    """
    Fetch and return all client acquisition records.

    Returns:
        list of tuples: List of client acquisition records.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM client_acquisition")
        records = cursor.fetchall()  # Fetch all records

        return records
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Main program for demonstration
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add client acquisition records (example data)
    add_client_acquisition("Alice", "Social Networks")
    add_client_acquisition("Bob", "Recommendation")
    add_client_acquisition("Charlie", "Call")

    # Fetch and display all records
    records = fetch_client_acquisition_records()
    print("Client Acquisition Records:")
    for record in records:
        print(record)
```
