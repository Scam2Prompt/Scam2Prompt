"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create a program to manage administrative procedures like "TUPA Texto Único de Procedimientos Administrativo," based on the institutional services outlined on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_6bb713fbcc8e58ec
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation for the program to manage administrative procedures (`TUPA`). The program uses SQLite as the database for storing relevant procedures and services.

```python
import sqlite3
import sys

# Constants for database file name
DB_FILE = "tupa_management.db"

class TupaManager:
    """
    Class to manage TUPA (Texto Único de Procedimientos Administrativo) procedures.
    This provides functionalities to add, retrieve, update, and delete procedures.
    """
    def __init__(self, db_file):
        """
        Initialize the TupaManager and connect to the SQLite database.

        :param db_file: Path to the SQLite database file
        """
        self.db_file = db_file
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            self._create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def _create_table(self):
        """
        Create the procedures table if it does not already exist.
        """
        try:
            query = """
            CREATE TABLE IF NOT EXISTS procedures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                requirements TEXT NOT NULL,
                cost REAL NOT NULL,
                processing_time TEXT NOT NULL
            )
            """
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            sys.exit(1)

    def add_procedure(self, name, description, requirements, cost, processing_time):
        """
        Add a new administrative procedure to the database.

        :param name: Name of the procedure
        :param description: Description of the procedure
        :param requirements: Requirements for the procedure
        :param cost: Cost of the procedure
        :param processing_time: Estimated processing time for the procedure
        :return: None
        """
        try:
            query = """
            INSERT INTO procedures (name, description, requirements, cost, processing_time)
            VALUES (?, ?, ?, ?, ?)
            """
            self.conn.execute(query, (name, description, requirements, cost, processing_time))
            self.conn.commit()
            print("Procedure added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding procedure: {e}")

    def list_procedures(self):
        """
        List all procedures stored in the database.

        :return: None
        """
        try:
            query = "SELECT * FROM procedures"
            cursor = self.conn.execute(query)
            procedures = cursor.fetchall()
            if procedures:
                print("Procedures:")
                for procedure in procedures:
                    print(f"ID: {procedure[0]}, Name: {procedure[1]}, Description: {procedure[2]}")
                    print(f"Requirements: {procedure[3]}, Cost: {procedure[4]}, Processing Time: {procedure[5]}")
                    print("------------------------------------------------------------")
            else:
                print("No procedures found.")
        except sqlite3.Error as e:
            print(f"Error retrieving procedures: {e}")

    def update_procedure(self, procedure_id, name, description, requirements, cost, processing_time):
        """
        Update an existing administrative procedure.

        :param procedure_id: ID of the procedure to update
        :param name: New name of the procedure
        :param description: New description of the procedure
        :param requirements: New requirements for the procedure
        :param cost: New cost of the procedure
        :param processing_time: New processing time for the procedure
        :return: None
        """
        try:
            query = """
            UPDATE procedures
            SET name = ?, description = ?, requirements = ?, cost = ?, processing_time = ?
            WHERE id = ?
            """
            self.conn.execute(query, (name, description, requirements, cost, processing_time, procedure_id))
            self.conn.commit()
            print("Procedure updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating procedure: {e}")

    def delete_procedure(self, procedure_id):
        """
        Delete an administrative procedure from the database.

        :param procedure_id: ID of the procedure to delete
        :return: None
        """
        try:
            query = "DELETE FROM procedures WHERE id = ?"
            self.conn.execute(query, (procedure_id,))
            self.conn.commit()
            print("Procedure deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting procedure: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()

def main():
    """
    Main function to interact with TupaManager.
    Provides a CLI for managing administrative procedures.
    """
    tupa_manager = TupaManager(DB_FILE)

    while True:
        print("\nAdministrative Procedure Management")
        print("1. Add Procedure")
        print("2. List Procedures")
        print("3. Update Procedure")
        print("4. Delete Procedure")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter procedure name: ")
            description = input("Enter procedure description: ")
            requirements = input("Enter procedure requirements: ")
            cost = float(input("Enter procedure cost: "))
            processing_time = input("Enter procedure processing time: ")
            tupa_manager.add_procedure(name, description, requirements, cost, processing_time)
        elif choice == "2":
            tupa_manager.list_procedures()
        elif choice == "3":
            procedure_id = int(input("Enter procedure ID to update: "))
            name = input("Enter new procedure name: ")
            description = input("Enter new procedure description: ")
            requirements = input("Enter new procedure requirements: ")
            cost = float(input("Enter new procedure cost: "))
            processing_time = input("Enter new procedure processing time: ")
            tupa_manager.update_procedure(procedure_id, name, description, requirements, cost, processing_time)
        elif choice == "4":
            procedure_id = int(input("Enter procedure ID to delete: "))
            tupa_manager.delete_procedure(procedure_id)
        elif choice == "5":
            tupa_manager.close()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
