"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: Provide a code example for tracking service requests and maintenance history for York chillers in a database.
Generated: DETERMINISTIC_d4c61d870925d682
Batch ID: 20250612_155349
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

# Database initialization
def initialize_database():
    """
    Creates a database and necessary tables for tracking York chiller service requests and maintenance history.
    """
    connection = sqlite3.connect('york_chillers.db')
    cursor = connection.cursor()

    # Create tables if they do not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chillers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        serial_number TEXT UNIQUE NOT NULL,
        model TEXT NOT NULL,
        location TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS service_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chiller_id INTEGER NOT NULL,
        request_date DATE NOT NULL,
        description TEXT NOT NULL,
        status TEXT CHECK(status IN ('Pending', 'In Progress', 'Completed')) NOT NULL,
        FOREIGN KEY (chiller_id) REFERENCES chillers (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS maintenance_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chiller_id INTEGER NOT NULL,
        maintenance_date DATE NOT NULL,
        technician_name TEXT NOT NULL,
        details TEXT NOT NULL,
        FOREIGN KEY (chiller_id) REFERENCES chillers (id)
    )
    ''')

    connection.commit()
    connection.close()


# Add a new chiller to the database
def add_chiller(serial_number, model, location):
    """
    Adds a new York chiller to the database.
    """
    try:
        connection = sqlite3.connect('york_chillers.db')
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO chillers (serial_number, model, location)
        VALUES (?, ?, ?)
        ''', (serial_number, model, location))

        connection.commit()
    except sqlite3.IntegrityError:
        print("Error: A chiller with this serial number already exists.")
    finally:
        connection.close()


# Add a service request for a chiller
def add_service_request(chiller_id, description, status='Pending'):
    """
    Adds a new service request for a specific York chiller.
    """
    try:
        connection = sqlite3.connect('york_chillers.db')
        cursor = connection.cursor()

        request_date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('''
        INSERT INTO service_requests (chiller_id, request_date, description, status)
        VALUES (?, ?, ?, ?)
        ''', (chiller_id, request_date, description, status))

        connection.commit()
    except sqlite3.IntegrityError:
        print("Error: Invalid chiller ID.")
    finally:
        connection.close()


# Add maintenance history for a chiller
def add_maintenance_history(chiller_id, technician_name, details):
    """
    Adds a maintenance record to the history of a specific York chiller.
    """
    try:
        connection = sqlite3.connect('york_chillers.db')
        cursor = connection.cursor()

        maintenance_date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('''
        INSERT INTO maintenance_history (chiller_id, maintenance_date, technician_name, details)
        VALUES (?, ?, ?, ?)
        ''', (chiller_id, maintenance_date, technician_name, details))

        connection.commit()
    except sqlite3.IntegrityError:
        print("Error: Invalid chiller ID.")
    finally:
        connection.close()


# Fetch details of all chillers
def get_chillers():
    """
    Retrieves all chillers from the database.
    """
    connection = sqlite3.connect('york_chillers.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM chillers')
    chillers = cursor.fetchall()

    connection.close()
    return chillers


# Fetch service requests for a specific chiller
def get_service_requests(chiller_id):
    """
    Retrieves all service requests for a specific York chiller.
    """
    connection = sqlite3.connect('york_chillers.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT * FROM service_requests WHERE chiller_id = ?
    ''', (chiller_id,))
    service_requests = cursor.fetchall()

    connection.close()
    return service_requests


# Fetch maintenance history for a specific chiller
def get_maintenance_history(chiller_id):
    """
    Retrieves the maintenance history for a specific York chiller.
    """
    connection = sqlite3.connect('york_chillers.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT * FROM maintenance_history WHERE chiller_id = ?
    ''', (chiller_id,))
    maintenance_history = cursor.fetchall()

    connection.close()
    return maintenance_history


# Initialize the database
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_chiller("SN12345", "Model-X", "Building A")
    add_service_request(1, "Routine check", "Pending")
    add_maintenance_history(1, "John Doe", "Replaced compressor")
    
    print("Chillers:", get_chillers())
    print("Service Requests:", get_service_requests(1))
    print("Maintenance History:", get_maintenance_history(1))
```
