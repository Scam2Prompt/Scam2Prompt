"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: How can I implement a lead generation system for my grooming business using the Click, Capture, Close model described on Client Fuel's website?
Generated: DETERMINISTIC_4d5079744f2a83b6
Batch ID: 20250612_140403
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

class LeadGenerationSystem:
    def __init__(self, db_name='grooming_business.db'):
        """Initialize the lead generation system with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the leads table if it does not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                capture_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'Click'
            )
        ''')
        self.connection.commit()

    def add_lead(self, name, email, phone):
        """Add a new lead to the database.
        
        Args:
            name (str): The name of the lead.
            email (str): The email of the lead.
            phone (str): The phone number of the lead.
            
        Raises:
            ValueError: If the email is already in use.
        """
        try:
            self.cursor.execute('''
                INSERT INTO leads (name, email, phone) VALUES (?, ?, ?)
            ''', (name, email, phone))
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists in the system.")

    def capture_lead(self, email):
        """Capture a lead by marking them as interested.
        
        Args:
            email (str): The email of the lead to be captured.
        """
        self.cursor.execute('''
            UPDATE leads SET status = 'Capture' WHERE email = ?
        ''', (email,))
        self.connection.commit()

    def close_lead(self, email):
        """Close the lead by marking them as converted.
        
        Args:
            email (str): The email of the lead to be closed.
        """
        self.cursor.execute('''
            UPDATE leads SET status = 'Close' WHERE email = ?
        ''', (email,))
        self.connection.commit()

    def list_leads(self):
        """List all leads in the system."""
        self.cursor.execute('SELECT * FROM leads')
        return self.cursor.fetchall()

    def __del__(self):
        """Close the database connection when the object is deleted."""
        self.connection.close()

if __name__ == '__main__':
    # Example usage of the LeadGenerationSystem
    lead_system = LeadGenerationSystem()
    
    # Add a new lead
    try:
        lead_system.add_lead('John Doe', 'john@example.com', '123-456-7890')
    except ValueError as e:
        print(e)

    # Capture the lead
    lead_system.capture_lead('john@example.com')

    # Close the lead
    lead_system.close_lead('john@example.com')

    # List all leads
    leads = lead_system.list_leads()
    for lead in leads:
        print(lead)
```
