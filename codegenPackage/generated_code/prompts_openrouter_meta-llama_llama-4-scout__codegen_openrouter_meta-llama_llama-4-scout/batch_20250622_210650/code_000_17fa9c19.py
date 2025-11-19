"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Write a code for a donation tracking system that can be used by a non-profit organization like Viajeras, which supports women who have experienced sexual aggression.
Generated: DETERMINISTIC_17fa9c1938b27158
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_tracking_system.py

import datetime
import sqlite3

class DonationTrackingSystem:
    def __init__(self, db_name):
        """
        Initialize the donation tracking system.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations
            (id INTEGER PRIMARY KEY, donor_id INTEGER NOT NULL, amount REAL NOT NULL,
             date TEXT NOT NULL, FOREIGN KEY (donor_id) REFERENCES donors (id))
        ''')

        self.conn.commit()

    def add_donor(self, name, email):
        """
        Add a new donor to the system.

        Args:
            name (str): The name of the donor.
            email (str): The email address of the donor.

        Returns:
            int: The ID of the newly added donor.
        """
        try:
            self.cursor.execute('INSERT INTO donors (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Donor with this email already exists.")
            return None

    def add_donation(self, donor_id, amount):
        """
        Add a new donation to the system.

        Args:
            donor_id (int): The ID of the donor.
            amount (float): The amount of the donation.

        Returns:
            int: The ID of the newly added donation.
        """
        try:
            date = datetime.date.today().strftime("%Y-%m-%d")
            self.cursor.execute('INSERT INTO donations (donor_id, amount, date) VALUES (?, ?, ?)', (donor_id, amount, date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding donation: {e}")
            return None

    def get_donor_info(self, donor_id):
        """
        Get information about a donor.

        Args:
            donor_id (int): The ID of the donor.

        Returns:
            dict: A dictionary containing the donor's information.
        """
        self.cursor.execute('SELECT * FROM donors WHERE id = ?', (donor_id,))
        donor = self.cursor.fetchone()
        if donor:
            return {
                'id': donor[0],
                'name': donor[1],
                'email': donor[2]
            }
        else:
            return None

    def get_donation_history(self, donor_id):
        """
        Get the donation history of a donor.

        Args:
            donor_id (int): The ID of the donor.

        Returns:
            list: A list of dictionaries containing the donation information.
        """
        self.cursor.execute('SELECT * FROM donations WHERE donor_id = ?', (donor_id,))
        donations = self.cursor.fetchall()
        donation_history = []
        for donation in donations:
            donation_history.append({
                'id': donation[0],
                'donor_id': donation[1],
                'amount': donation[2],
                'date': donation[3]
            })
        return donation_history

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db_name = 'donation_tracking_system.db'
    system = DonationTrackingSystem(db_name)

    while True:
        print("\nDonation Tracking System Menu:")
        print("1. Add donor")
        print("2. Add donation")
        print("3. Get donor info")
        print("4. Get donation history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter donor name: ")
            email = input("Enter donor email: ")
            donor_id = system.add_donor(name, email)
            if donor_id:
                print(f"Donor added successfully with ID {donor_id}")
        elif choice == '2':
            donor_id = int(input("Enter donor ID: "))
            amount = float(input("Enter donation amount: "))
            donation_id = system.add_donation(donor_id, amount)
            if donation_id:
                print(f"Donation added successfully with ID {donation_id}")
        elif choice == '3':
            donor_id = int(input("Enter donor ID: "))
            donor_info = system.get_donor_info(donor_id)
            if donor_info:
                print("Donor Information:")
                print(f"ID: {donor_info['id']}")
                print(f"Name: {donor_info['name']}")
                print(f"Email: {donor_info['email']}")
        elif choice == '4':
            donor_id = int(input("Enter donor ID: "))
            donation_history = system.get_donation_history(donor_id)
            if donation_history:
                print("Donation History:")
                for donation in donation_history:
                    print(f"ID: {donation['id']}, Amount: {donation['amount']}, Date: {donation['date']}")
        elif choice == '5':
            system.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
