"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Generate a script to manage a database of Whirlpool appliance repair requests, including fields for appliance type (e.g., lavadoras, neveras, estufas), customer location (e.g., Bogotá, Soacha), and technician assignment.
Generated: DETERMINISTIC_effcf33b81c638d5
Batch ID: 20250612_152511
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

# Database file name
DB_FILE = "repair_requests.db"

class RepairRequestManager:
    def __init__(self, db_file):
        """
        Initialize the RepairRequestManager with the SQLite database file.
        """
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        """
        Create the repair_requests table if it doesn't exist.
        """
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS repair_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appliance_type TEXT NOT NULL,
                    customer_location TEXT NOT NULL,
                    technician TEXT NOT NULL,
                    request_date TEXT NOT NULL
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            connection.close()

    def add_request(self, appliance_type, customer_location, technician):
        """
        Add a new repair request to the database.
        """
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()

            request_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO repair_requests (appliance_type, customer_location, technician, request_date)
                VALUES (?, ?, ?, ?)
            """, (appliance_type, customer_location, technician, request_date))
            connection.commit()
            print("Repair request added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding repair request: {e}")
        finally:
            connection.close()

    def list_requests(self):
        """
        List all repair requests in the database.
        """
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("SELECT id, appliance_type, customer_location, technician, request_date FROM repair_requests")
            rows = cursor.fetchall()

            print("Repair Requests:")
            for row in rows:
                print(f"ID: {row[0]}, Appliance: {row[1]}, Location: {row[2]}, Technician: {row[3]}, Date: {row[4]}")
        except sqlite3.Error as e:
            print(f"Error listing repair requests: {e}")
        finally:
            connection.close()

    def delete_request(self, request_id):
        """
        Delete a repair request by ID.
        """
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM repair_requests WHERE id = ?", (request_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Repair request deleted successfully.")
            else:
                print("No repair request found with the given ID.")
        except sqlite3.Error as e:
            print(f"Error deleting repair request: {e}")
        finally:
            connection.close()

# Main program
if __name__ == "__main__":
    manager = RepairRequestManager(DB_FILE)

    while True:
        print("\nWhirlpool Appliance Repair Request Manager")
        print("1. Add repair request")
        print("2. List repair requests")
        print("3. Delete repair request")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            appliance_type = input("Enter appliance type (e.g., lavadoras, neveras, estufas): ").strip()
            customer_location = input("Enter customer location (e.g., Bogotá, Soacha): ").strip()
            technician = input("Enter technician name: ").strip()
            manager.add_request(appliance_type, customer_location, technician)
        elif choice == "2":
            manager.list_requests()
        elif choice == "3":
            try:
                request_id = int(input("Enter the ID of the repair request to delete: ").strip())
                manager.delete_request(request_id)
            except ValueError:
                print("Invalid ID. Please enter a valid integer.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
