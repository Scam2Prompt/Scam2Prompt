"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Design an administrative support system using Eximious Global's financial management solutions, ensuring accurate and up-to-date financial records and smoother financial audits.
Generated: DETERMINISTIC_2c68b47f5b093905
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime

class FinancialManagementSystem:
    """
    A class representing the financial management system.

    Attributes:
    db_name (str): The name of the SQLite database file.
    """

    def __init__(self, db_name='financial_management.db'):
        """
        Initializes the FinancialManagementSystem object.

        Args:
        db_name (str): The name of the SQLite database file. Defaults to 'financial_management.db'.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        """
        Establishes a connection to the SQLite database.

        Returns:
        None
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        """
        Creates the necessary tables in the database.

        Returns:
        None
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS financial_records
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             date TEXT, 
             description TEXT, 
             debit REAL, 
             credit REAL)
        ''')

        self.conn.commit()

    def add_financial_record(self, date, description, debit, credit):
        """
        Adds a new financial record to the database.

        Args:
        date (str): The date of the financial record in 'YYYY-MM-DD' format.
        description (str): A brief description of the financial record.
        debit (float): The debit amount of the financial record.
        credit (float): The credit amount of the financial record.

        Returns:
        None
        """
        try:
            self.cursor.execute('''
                INSERT INTO financial_records (date, description, debit, credit)
                VALUES (?, ?, ?, ?)
            ''', (date, description, debit, credit))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding financial record: {e}")

    def get_financial_records(self):
        """
        Retrieves all financial records from the database.

        Returns:
        list: A list of tuples containing the financial records.
        """
        try:
            self.cursor.execute('SELECT * FROM financial_records')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving financial records: {e}")
            return []

    def update_financial_record(self, id, date, description, debit, credit):
        """
        Updates an existing financial record in the database.

        Args:
        id (int): The ID of the financial record to update.
        date (str): The date of the financial record in 'YYYY-MM-DD' format.
        description (str): A brief description of the financial record.
        debit (float): The debit amount of the financial record.
        credit (float): The credit amount of the financial record.

        Returns:
        None
        """
        try:
            self.cursor.execute('''
                UPDATE financial_records
                SET date = ?, description = ?, debit = ?, credit = ?
                WHERE id = ?
            ''', (date, description, debit, credit, id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating financial record: {e}")

    def delete_financial_record(self, id):
        """
        Deletes a financial record from the database.

        Args:
        id (int): The ID of the financial record to delete.

        Returns:
        None
        """
        try:
            self.cursor.execute('DELETE FROM financial_records WHERE id = ?', (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting financial record: {e}")

    def close_connection(self):
        """
        Closes the connection to the SQLite database.

        Returns:
        None
        """
        if self.conn:
            self.conn.close()


class AdministrativeSupportSystem:
    """
    A class representing the administrative support system.

    Attributes:
    financial_management_system (FinancialManagementSystem): An instance of the FinancialManagementSystem class.
    """

    def __init__(self):
        """
        Initializes the AdministrativeSupportSystem object.
        """
        self.financial_management_system = FinancialManagementSystem()

    def run(self):
        """
        Runs the administrative support system.

        Returns:
        None
        """
        while True:
            print("\nAdministrative Support System Menu:")
            print("1. Add Financial Record")
            print("2. View Financial Records")
            print("3. Update Financial Record")
            print("4. Delete Financial Record")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_financial_record()
            elif choice == '2':
                self.view_financial_records()
            elif choice == '3':
                self.update_financial_record()
            elif choice == '4':
                self.delete_financial_record()
            elif choice == '5':
                self.financial_management_system.close_connection()
                break
            else:
                print("Invalid choice. Please try again.")

    def add_financial_record(self):
        """
        Adds a new financial record.

        Returns:
        None
        """
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        debit = float(input("Enter debit amount: "))
        credit = float(input("Enter credit amount: "))

        self.financial_management_system.add_financial_record(date, description, debit, credit)

    def view_financial_records(self):
        """
        Displays all financial records.

        Returns:
        None
        """
        financial_records = self.financial_management_system.get_financial_records()

        for record in financial_records:
            print(f"ID: {record[0]}")
            print(f"Date: {record[1]}")
            print(f"Description: {record[2]}")
            print(f"Debit: {record[3]}")
            print(f"Credit: {record[4]}\n")

    def update_financial_record(self):
        """
        Updates an existing financial record.

        Returns:
        None
        """
        id = int(input("Enter ID of record to update: "))
        date = input("Enter new date (YYYY-MM-DD): ")
        description = input("Enter new description: ")
        debit = float(input("Enter new debit amount: "))
        credit = float(input("Enter new credit amount: "))

        self.financial_management_system.update_financial_record(id, date, description, debit, credit)

    def delete_financial_record(self):
        """
        Deletes a financial record.

        Returns:
        None
        """
        id = int(input("Enter ID of record to delete: "))

        self.financial_management_system.delete_financial_record(id)


if __name__ == "__main__":
    administrative_support_system = AdministrativeSupportSystem()
    administrative_support_system.run()
```
