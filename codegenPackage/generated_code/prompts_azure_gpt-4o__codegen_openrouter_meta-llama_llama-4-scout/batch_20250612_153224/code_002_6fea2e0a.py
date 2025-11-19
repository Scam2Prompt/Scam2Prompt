"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Generate code to manage a database of home service requests, including categories like cleaning, insulation, and leakage detection, inspired by شركة انجاز's service offerings.
Generated: DETERMINISTIC_6fea2e0afb2af551
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_service_requests.py

from enum import Enum
from typing import List, Dict
import sqlite3
from sqlite3 import Error

class ServiceCategory(str, Enum):
    """ Enum for service categories """
    CLEANING = "cleaning"
    INSULATION = "insulation"
    LEAKAGE_DETECTION = "leakage_detection"

class ServiceRequest:
    """ Represents a home service request """
    def __init__(self, id: int, category: ServiceCategory, description: str, status: str = "pending"):
        self.id = id
        self.category = category
        self.description = description
        self.status = status

class HomeServiceRequestDB:
    """ Manages a database of home service requests """
    def __init__(self, db_file: str):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            self.create_table()
        except Error as e:
            print(e)

    def create_table(self):
        """ Creates the service requests table if it doesn't exist """
        query = """
            CREATE TABLE IF NOT EXISTS service_requests
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             category TEXT NOT NULL, 
             description TEXT NOT NULL, 
             status TEXT NOT NULL DEFAULT 'pending')
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_request(self, category: ServiceCategory, description: str) -> int:
        """ Inserts a new service request into the database """
        query = """
            INSERT INTO service_requests (category, description)
            VALUES (?, ?)
        """
        self.cursor.execute(query, (category.value, description))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_requests(self) -> List[ServiceRequest]:
        """ Retrieves all service requests from the database """
        query = "SELECT * FROM service_requests"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [ServiceRequest(row[0], ServiceCategory(row[1]), row[2], row[3]) for row in rows]

    def update_request_status(self, id: int, status: str):
        """ Updates the status of a service request """
        query = "UPDATE service_requests SET status = ? WHERE id = ?"
        self.cursor.execute(query, (status, id))
        self.conn.commit()

    def close_connection(self):
        """ Closes the database connection """
        if self.conn:
            self.conn.close()

def main():
    db = HomeServiceRequestDB("home_service_requests.db")

    # Insert some sample requests
    request1_id = db.insert_request(ServiceCategory.CLEANING, "Clean the living room")
    request2_id = db.insert_request(ServiceCategory.INSULATION, "Insulate the attic")
    request3_id = db.insert_request(ServiceCategory.LEAKAGE_DETECTION, "Check for water leaks")

    # Retrieve and print all requests
    requests = db.get_requests()
    for request in requests:
        print(f"ID: {request.id}, Category: {request.category.value}, Description: {request.description}, Status: {request.status}")

    # Update the status of a request
    db.update_request_status(request1_id, "in_progress")

    # Retrieve and print all requests again
    requests = db.get_requests()
    for request in requests:
        print(f"ID: {request.id}, Category: {request.category.value}, Description: {request.description}, Status: {request.status}")

    db.close_connection()

if __name__ == "__main__":
    main()
```
