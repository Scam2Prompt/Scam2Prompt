"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Can you provide a code example for integrating ultrasonic cleaning service requests into a manufacturing management system?
Generated: DETERMINISTIC_fb4ae8e4840123cf
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
import sqlite3
from datetime import datetime

# Define database schema and create a connection
DB_NAME = 'manufacturing.db'

def initialize_database():
    """Initialize the database with the required schema."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create table for ultrasonic cleaning service requests
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ultrasonic_cleaning_requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment_id TEXT NOT NULL,
            operator_id TEXT NOT NULL,
            cleaning_type TEXT NOT NULL CHECK(cleaning_type IN ('standard', 'deep')),
            request_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'cancelled'))
        )
    """)
    
    connection.commit()
    connection.close()

# Initialize the database
initialize_database()

def add_cleaning_request(equipment_id, operator_id, cleaning_type):
    """
    Add an ultrasonic cleaning service request to the database.
    
    Parameters:
        equipment_id (str): ID of the equipment requiring cleaning.
        operator_id (str): ID of the operator requesting the cleaning.
        cleaning_type (str): Type of cleaning ('standard' or 'deep').
        
    Returns:
        dict: Confirmation of the request added.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Insert new request
        request_date = datetime.now().isoformat()  # Capture current timestamp
        status = 'pending'  # Default status for new requests
        cursor.execute("""
            INSERT INTO ultrasonic_cleaning_requests (equipment_id, operator_id, cleaning_type, request_date, status)
            VALUES (?, ?, ?, ?, ?)
        """, (equipment_id, operator_id, cleaning_type, request_date, status))
        
        connection.commit()
        request_id = cursor.lastrowid  # Get the ID of the newly added request
        return {"request_id": request_id, "status": "success", "message": "Cleaning request added successfully."}
        
    except sqlite3.Error as e:
        # Handle database errors
        return {"status": "error", "message": str(e)}
    finally:
        if connection:
            connection.close()

def get_pending_requests():
    """
    Retrieve all pending ultrasonic cleaning service requests.
    
    Returns:
        list: List of pending requests as dictionaries.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT request_id, equipment_id, operator_id, cleaning_type, request_date, status
            FROM ultrasonic_cleaning_requests
            WHERE status = 'pending'
        """)
        
        rows = cursor.fetchall()
        pending_requests = [
            {
                "request_id": row[0],
                "equipment_id": row[1],
                "operator_id": row[2],
                "cleaning_type": row[3],
                "request_date": row[4],
                "status": row[5],
            }
            for row in rows
        ]
        return pending_requests
        
    except sqlite3.Error as e:
        # Handle database errors
        return {"status": "error", "message": str(e)}
    finally:
        if connection:
            connection.close()

def update_request_status(request_id, new_status):
    """
    Update the status of a cleaning service request.
    
    Parameters:
        request_id (int): ID of the request to update.
        new_status (str): New status ('pending', 'completed', 'cancelled').
        
    Returns:
        dict: Confirmation of the status update.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE ultrasonic_cleaning_requests
            SET status = ?
            WHERE request_id = ?
        """, (new_status, request_id))
        
        connection.commit()
        if cursor.rowcount > 0:
            return {"status": "success", "message": "Request status updated successfully."}
        else:
            return {"status": "error", "message": "Request ID not found."}
        
    except sqlite3.Error as e:
        # Handle database errors
        return {"status": "error", "message": str(e)}
    finally:
        if connection:
            connection.close()

# Example usage:
if __name__ == '__main__':
    # Add a new cleaning request
    response = add_cleaning_request("EQ123", "OP456", "standard")
    print(json.dumps(response, indent=4))
    
    # Get all pending requests
    pending_requests = get_pending_requests()
    print(json.dumps(pending_requests, indent=4))
    
    # Update a request's status
    status_update_response = update_request_status(1, "completed")
    print(json.dumps(status_update_response, indent=4))
```
