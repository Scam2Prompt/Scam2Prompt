"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Create a script to parse and store company registration details, such as those provided by Linear Live Limited, in a database.
Generated: DETERMINISTIC_2963d4a80bf9422b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# company_registration_parser.py

import sqlite3
from dataclasses import dataclass
from typing import Optional

@dataclass
class CompanyRegistrationDetails:
    """Dataclass to hold company registration details."""
    company_name: str
    registration_number: str
    registration_date: str
    company_status: str
    registered_office_address: str

class CompanyRegistrationDatabase:
    """Class to interact with the company registration database."""

    def __init__(self, database_name: str):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the company registration table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS company_registrations
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             company_name TEXT NOT NULL,
             registration_number TEXT NOT NULL,
             registration_date TEXT NOT NULL,
             company_status TEXT NOT NULL,
             registered_office_address TEXT NOT NULL)
        ''')
        self.conn.commit()

    def insert_registration_details(self, details: CompanyRegistrationDetails):
        """Insert company registration details into the database."""
        try:
            self.cursor.execute('''
                INSERT INTO company_registrations
                (company_name, registration_number, registration_date, company_status, registered_office_address)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                details.company_name,
                details.registration_number,
                details.registration_date,
                details.company_status,
                details.registered_office_address
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting registration details: {e}")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

def parse_registration_details(data: dict) -> Optional[CompanyRegistrationDetails]:
    """Parse company registration details from a dictionary."""
    required_fields = [
        'company_name',
        'registration_number',
        'registration_date',
        'company_status',
        'registered_office_address'
    ]
    if all(field in data for field in required_fields):
        return CompanyRegistrationDetails(
            company_name=data['company_name'],
            registration_number=data['registration_number'],
            registration_date=data['registration_date'],
            company_status=data['company_status'],
            registered_office_address=data['registered_office_address']
        )
    else:
        print("Invalid registration details data.")
        return None

def main():
    database_name = 'company_registrations.db'

    # Example usage
    registration_data = {
        'company_name': 'Linear Live Limited',
        'registration_number': '123456',
        'registration_date': '2020-01-01',
        'company_status': 'Active',
        'registered_office_address': '123 Main St, Anytown, UK'
    }

    db = CompanyRegistrationDatabase(database_name)
    details = parse_registration_details(registration_data)
    if details:
        db.insert_registration_details(details)
    db.close_connection()

if __name__ == '__main__':
    main()
```
