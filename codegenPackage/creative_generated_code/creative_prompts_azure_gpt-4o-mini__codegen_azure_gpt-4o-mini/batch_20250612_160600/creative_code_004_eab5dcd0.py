"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joinnow.info
Prompt: Illustrate how to implement a lead management system that integrates with a marketing strategy for a business opportunity like Money Order Freedom.
Generated: DETERMINISTIC_eab5dcd045f3c733
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# lead_management_system.py

import sqlite3
from typing import List, Dict, Optional

class Lead:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

class LeadManagementSystem:
    def __init__(self, db_name: str = "leads.db"):
        """
        Initialize the LeadManagementSystem with a database connection.
        :param db_name: The name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_leads_table()

    def create_leads_table(self):
        """Create the leads table in the database if it doesn't exist."""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL
            )''')
        self.connection.commit()

    def add_lead(self, lead: Lead) -> Optional[int]:
        """
        Add a new lead to the database.
        :param lead: An instance of Lead to be added.
        :return: The ID of the newly created lead or None if failed.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO leads (name, email, phone)
                VALUES (?, ?, ?)''', (lead.name, lead.email, lead.phone))
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Lead with email {lead.email} already exists.")
        except Exception as e:
            print(f"An error occurred while adding a lead: {e}")
        return None

    def get_leads(self) -> List[Dict[str, str]]:
        """
        Retrieve all leads from the database.
        :return: A list of dictionaries representing each lead.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM leads')
        rows = cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3]} for row in rows]

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == "__main__":
    # Example usage
    lead_management_system = LeadManagementSystem()

    # Adding leads to the system
    lead1 = Lead(name="John Doe", email="john@example.com", phone="1234567890")
    lead2 = Lead(name="Jane Smith", email="jane@example.com", phone="0987654321")

    print("Adding leads...")
    lead_id1 = lead_management_system.add_lead(lead1)
    lead_id2 = lead_management_system.add_lead(lead2)

    # Retrieve and display all leads
    print("Current leads in the system:")
    leads = lead_management_system.get_leads()
    for lead in leads:
        print(lead)

    # Close the system
    lead_management_system.close()
```
