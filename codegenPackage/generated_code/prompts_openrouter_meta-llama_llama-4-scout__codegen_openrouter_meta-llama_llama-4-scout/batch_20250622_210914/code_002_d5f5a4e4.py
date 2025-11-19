"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write a code snippet to create a simple database for managing donations and volunteer information for an organization like Kibera Hamlets.
Generated: DETERMINISTIC_d5f5a4e4aadb6634
Batch ID: 20250622_210914
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

class DonationDatabase:
    def __init__(self, db_name):
        """
        Initialize a connection to the SQLite database.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create tables for donations and volunteers if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_name TEXT NOT NULL,
                donation_amount REAL NOT NULL,
                donation_date DATE NOT NULL,
                donation_type TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_name TEXT NOT NULL,
                contact_info TEXT NOT NULL,
                volunteer_since DATE NOT NULL
            )
        ''')

        self.conn.commit()

    def add_donation(self, donor_name, donation_amount, donation_type):
        """
        Add a new donation to the database.

        Args:
            donor_name (str): The name of the donor.
            donation_amount (float): The amount donated.
            donation_type (str): The type of donation (e.g., monetary, goods, etc.).

        Returns:
            int: The ID of the newly added donation.
        """
        try:
            self.cursor.execute('''
                INSERT INTO donations (donor_name, donation_amount, donation_date, donation_type)
                VALUES (?, ?, ?, ?)
            ''', (donor_name, donation_amount, datetime.now().strftime('%Y-%m-%d'), donation_type))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding donation: {e}")
            return None

    def add_volunteer(self, volunteer_name, contact_info):
        """
        Add a new volunteer to the database.

        Args:
            volunteer_name (str): The name of the volunteer.
            contact_info (str): The contact information of the volunteer.

        Returns:
            int: The ID of the newly added volunteer.
        """
        try:
            self.cursor.execute('''
                INSERT INTO volunteers (volunteer_name, contact_info, volunteer_since)
                VALUES (?, ?, ?)
            ''', (volunteer_name, contact_info, datetime.now().strftime('%Y-%m-%d')))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding volunteer: {e}")
            return None

    def get_donations(self):
        """
        Retrieve all donations from the database.

        Returns:
            list: A list of tuples containing donation information.
        """
        try:
            self.cursor.execute('SELECT * FROM donations')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving donations: {e}")
            return []

    def get_volunteers(self):
        """
        Retrieve all volunteers from the database.

        Returns:
            list: A list of tuples containing volunteer information.
        """
        try:
            self.cursor.execute('SELECT * FROM volunteers')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving volunteers: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    db = DonationDatabase('kibera_hamlets.db')

    # Add donations
    donation1_id = db.add_donation('John Doe', 100.0, 'monetary')
    donation2_id = db.add_donation('Jane Doe', 50.0, 'goods')

    # Add volunteers
    volunteer1_id = db.add_volunteer('Volunteer 1', '123-456-7890')
    volunteer2_id = db.add_volunteer('Volunteer 2', '098-765-4321')

    # Retrieve donations and volunteers
    donations = db.get_donations()
    volunteers = db.get_volunteers()

    print("Donations:")
    for donation in donations:
        print(donation)

    print("\nVolunteers:")
    for volunteer in volunteers:
        print(volunteer)

    # Close the database connection
    db.close_connection()
```
