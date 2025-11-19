"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Design a data reporting system for tracking vaccine distribution and administration, incorporating CSL Seqirus's commitment to protecting public health from seasonal influenza."
Generated: DETERMINISTIC_e2e415bc39604f16
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

class VaccineDistributionSystem:
    """
    A class to represent a vaccine distribution and administration system.
    """

    def __init__(self, db_name='vaccine_distribution.db'):
        """
        Initializes the database connection and creates necessary tables.

        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates tables for tracking vaccine distribution and administration.
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS vaccines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    manufacturer TEXT NOT NULL,
                    distribution_date DATE NOT NULL,
                    quantity INTEGER NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS administrations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vaccine_id INTEGER NOT NULL,
                    administered_date DATE NOT NULL,
                    recipient_name TEXT NOT NULL,
                    FOREIGN KEY (vaccine_id) REFERENCES vaccines (id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_vaccine(self, name, manufacturer, distribution_date, quantity):
        """
        Adds a new vaccine to the distribution database.

        :param name: Name of the vaccine.
        :param manufacturer: Manufacturer of the vaccine.
        :param distribution_date: Date the vaccine was distributed.
        :param quantity: Quantity of the vaccine distributed.
        """
        try:
            self.cursor.execute('''
                INSERT INTO vaccines (name, manufacturer, distribution_date, quantity)
                VALUES (?, ?, ?, ?)
            ''', (name, manufacturer, distribution_date, quantity))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding vaccine: {e}")

    def record_administration(self, vaccine_id, administered_date, recipient_name):
        """
        Records the administration of a vaccine.

        :param vaccine_id: ID of the vaccine administered.
        :param administered_date: Date the vaccine was administered.
        :param recipient_name: Name of the recipient.
        """
        try:
            self.cursor.execute('''
                INSERT INTO administrations (vaccine_id, administered_date, recipient_name)
                VALUES (?, ?, ?)
            ''', (vaccine_id, administered_date, recipient_name))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error recording administration: {e}")

    def report_distribution(self):
        """
        Generates a report of vaccine distribution.
        """
        try:
            self.cursor.execute('SELECT * FROM vaccines')
            vaccines = self.cursor.fetchall()
            for vaccine in vaccines:
                print(f"ID: {vaccine[0]}, Name: {vaccine[1]}, Manufacturer: {vaccine[2]}, "
                      f"Distribution Date: {vaccine[3]}, Quantity: {vaccine[4]}")
        except sqlite3.Error as e:
            print(f"Error generating distribution report: {e}")

    def report_administration(self):
        """
        Generates a report of vaccine administrations.
        """
        try:
            self.cursor.execute('''
                SELECT a.id, v.name, a.administered_date, a.recipient_name
                FROM administrations a
                JOIN vaccines v ON a.vaccine_id = v.id
            ''')
            administrations = self.cursor.fetchall()
            for admin in administrations:
                print(f"Admin ID: {admin[0]}, Vaccine: {admin[1]}, "
                      f"Administered Date: {admin[2]}, Recipient: {admin[3]}")
        except sqlite3.Error as e:
            print(f"Error generating administration report: {e}")

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()


if __name__ == "__main__":
    # Example usage of the VaccineDistributionSystem
    vds = VaccineDistributionSystem()

    # Adding vaccines
    vds.add_vaccine("Flu Vaccine 2023", "CSL Seqirus", datetime.now().date(), 1000)

    # Recording administrations
    vds.record_administration(1, datetime.now().date(), "John Doe")

    # Generating reports
    print("Vaccine Distribution Report:")
    vds.report_distribution()
    print("\nVaccine Administration Report:")
    vds.report_administration()

    # Closing the system
    vds.close()
```
