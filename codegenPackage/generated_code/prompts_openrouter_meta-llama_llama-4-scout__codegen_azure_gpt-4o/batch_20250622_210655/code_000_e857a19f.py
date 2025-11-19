"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Write a program to manage donations for a non-profit organization like Udruga Radost Ogulin, including tracking and acknowledging contributions.
Generated: DETERMINISTIC_e857a19f1bb05878
Batch ID: 20250622_210655
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

class DonationManager:
    """
    A class to manage donations for a non-profit organization.
    """

    def __init__(self, db_name="donations.db"):
        """
        Initialize the DonationManager with a SQLite database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the donations table if it doesn't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_donation(self, donor_name, amount):
        """
        Add a new donation to the database.
        :param donor_name: Name of the donor.
        :param amount: Donation amount.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            donation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO donations (donor_name, amount, date)
                VALUES (?, ?, ?)
            """, (donor_name, amount, donation_date))
            conn.commit()
            print(f"Thank you, {donor_name}, for your generous donation of ${amount:.2f}!")
        except sqlite3.Error as e:
            print(f"Error adding donation: {e}")
        finally:
            conn.close()

    def list_donations(self):
        """
        List all donations in the database.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donations")
            donations = cursor.fetchall()
            print("Donations:")
            print("ID | Donor Name | Amount | Date")
            print("-" * 40)
            for donation in donations:
                print(f"{donation[0]} | {donation[1]} | ${donation[2]:.2f} | {donation[3]}")
        except sqlite3.Error as e:
            print(f"Error listing donations: {e}")
        finally:
            conn.close()

    def total_donations(self):
        """
        Calculate the total amount of donations.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(amount) FROM donations")
            total = cursor.fetchone()[0]
            total = total if total is not None else 0
            print(f"Total donations received: ${total:.2f}")
        except sqlite3.Error as e:
            print(f"Error calculating total donations: {e}")
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    manager = DonationManager()

    # Add donations
    try:
        manager.add_donation("Alice", 100.50)
        manager.add_donation("Bob", 200.00)
    except ValueError as ve:
        print(f"Error: {ve}")

    # List all donations
    manager.list_donations()

    # Display total donations
    manager.total_donations()
```
