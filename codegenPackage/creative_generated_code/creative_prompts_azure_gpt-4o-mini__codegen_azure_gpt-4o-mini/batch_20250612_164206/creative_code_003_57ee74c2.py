"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a sample code to log and track the verification dates of water and heat meters, ensuring compliance with the regulations highlighted on the webpage.
Generated: DETERMINISTIC_57ee74c293733c6e
Batch ID: 20250612_164206
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

class MeterVerificationTracker:
    """
    A class to track verification dates of water and heat meters.
    It stores the data in an SQLite database to ensure persistence.
    """
    def __init__(self, db_name='meter_verification.db'):
        """
        Initializes the database connection and creates the necessary table if it does not exist.

        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """ Creates the verification_data table if it doesn't already exist. """
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS verification_data (
                        id INTEGER PRIMARY KEY,
                        meter_type TEXT NOT NULL,
                        verification_date DATE NOT NULL,
                        notes TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_verification(self, meter_type: str, verification_date: str, notes: str = ""):
        """
        Adds a verification record to the database.

        :param meter_type: Type of the meter (e.g., 'Water', 'Heat').
        :param verification_date: Date of verification in 'YYYY-MM-DD' format.
        :param notes: Optional notes related to the verification.
        """
        try:
            date_obj = datetime.strptime(verification_date, '%Y-%m-%d')
            with self.connection:
                self.connection.execute('''
                    INSERT INTO verification_data (meter_type, verification_date, notes) 
                    VALUES (?, ?, ?)
                ''', (meter_type, date_obj, notes))
        except sqlite3.Error as e:
            print(f"Error adding verification record: {e}")
        except ValueError as e:
            print(f"Error parsing verification date: {e}")

    def get_verifications(self):
        """ Returns all verification records from the database. """
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM verification_data')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving verification records: {e}")
            return []

    def close(self):
        """ Closes the database connection. """
        self.connection.close()


if __name__ == "__main__":
    # Example usage of the MeterVerificationTracker
    tracker = MeterVerificationTracker()

    # Adding sample verification records
    tracker.add_verification('Water', '2023-01-15', 'Initial verification of the water meter.')
    tracker.add_verification('Heat', '2023-06-20', 'Checked and found compliant.')

    # Retrieve and print all verifications
    verifications = tracker.get_verifications()
    for record in verifications:
        print(record)

    # Closing the connection after use
    tracker.close()
```
