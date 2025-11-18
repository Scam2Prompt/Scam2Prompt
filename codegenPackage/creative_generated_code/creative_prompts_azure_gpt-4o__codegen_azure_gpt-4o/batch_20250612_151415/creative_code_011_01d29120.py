"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Develop a script to track Aadhaar update requests and their status, inspired by the Aadhaar Update Status tool on the IFSC Finder website.
Generated: DETERMINISTIC_01d29120685fe1d4
Batch ID: 20250612_151415
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

class AadhaarUpdateTracker:
    """
    Class to handle Aadhaar update requests and track their status.
    """

    def __init__(self, db_name="aadhaar_update_tracker.db"):
        """
        Initialize the tracker and create the database table if it doesn't exist.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the database table for tracking Aadhaar update requests.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS aadhaar_updates (
                    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aadhaar_number TEXT NOT NULL,
                    update_type TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Pending',
                    request_date TEXT NOT NULL,
                    last_updated TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_request(self, aadhaar_number, update_type):
        """
        Add a new Aadhaar update request to the tracker.
        :param aadhaar_number: The Aadhaar number for the update.
        :param update_type: Type of update (e.g., 'Address', 'Mobile', 'Name').
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            request_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO aadhaar_updates (aadhaar_number, update_type, request_date, last_updated)
                VALUES (?, ?, ?, ?)
            """, (aadhaar_number, update_type, request_date, request_date))
            conn.commit()
            print("Request added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding request: {e}")
        finally:
            conn.close()

    def update_status(self, request_id, new_status):
        """
        Update the status of an Aadhaar update request.
        :param request_id: The ID of the request to update.
        :param new_status: New status for the request (e.g., 'Approved', 'Rejected').
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                UPDATE aadhaar_updates
                SET status = ?, last_updated = ?
                WHERE request_id = ?
            """, (new_status, last_updated, request_id))
            conn.commit()
            if cursor.rowcount > 0:
                print("Status updated successfully!")
            else:
                print("No matching request found.")
        except sqlite3.Error as e:
            print(f"Error updating status: {e}")
        finally:
            conn.close()

    def get_requests(self):
        """
        Retrieve and display all Aadhaar update requests and their statuses.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM aadhaar_updates")
            requests = cursor.fetchall()
            if requests:
                print("Aadhaar Update Requests:")
                for req in requests:
                    print(f"Request ID: {req[0]}, Aadhaar Number: {req[1]}, Update Type: {req[2]}, "
                          f"Status: {req[3]}, Request Date: {req[4]}, Last Updated: {req[5]}")
            else:
                print("No requests found.")
        except sqlite3.Error as e:
            print(f"Error retrieving requests: {e}")
        finally:
            conn.close()


# Example usage:
if __name__ == "__main__":
    tracker = AadhaarUpdateTracker()

    # Add a new update request
    tracker.add_request("1234-5678-9012", "Address")

    # Update the status of a request
    tracker.update_status(1, "Approved")

    # Retrieve and display all requests
    tracker.get_requests()
```
