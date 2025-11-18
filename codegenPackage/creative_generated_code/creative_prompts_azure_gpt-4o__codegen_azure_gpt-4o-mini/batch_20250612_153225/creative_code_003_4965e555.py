"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Provide code examples for creating a lead generation system with targeted campaigns, as described in Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_4965e55534dfa717
Batch ID: 20250612_153225
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeadGenerationSystem:
    def __init__(self, db_name='leads.db'):
        """Initializes the lead generation system with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Creates necessary tables for leads and campaigns in the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS leads (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        phone TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS campaigns (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        target_audience TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                logging.info("Tables created successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error creating tables: {e}")
            self.conn.close()

    def add_lead(self, name, email, phone=None):
        """Adds a new lead to the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO leads (name, email, phone) VALUES (?, ?, ?)
                ''', (name, email, phone))
                logging.info(f"Lead added: {name} ({email})")
        except sqlite3.IntegrityError:
            logging.error(f"Lead with email {email} already exists.")
        except sqlite3.Error as e:
            logging.error(f"Error adding lead: {e}")

    def add_campaign(self, name, target_audience):
        """Adds a new marketing campaign to the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO campaigns (name, target_audience) VALUES (?, ?)
                ''', (name, target_audience))
                logging.info(f"Campaign added: {name}")
        except sqlite3.Error as e:
            logging.error(f"Error adding campaign: {e}")

    def get_leads(self):
        """Retrieves all leads from the database."""
        try:
            cursor = self.conn.execute('SELECT * FROM leads')
            leads = cursor.fetchall()
            logging.info(f"Retrieved {len(leads)} leads.")
            return leads
        except sqlite3.Error as e:
            logging.error(f"Error retrieving leads: {e}")
            return []

    def get_campaigns(self):
        """Retrieves all campaigns from the database."""
        try:
            cursor = self.conn.execute('SELECT * FROM campaigns')
            campaigns = cursor.fetchall()
            logging.info(f"Retrieved {len(campaigns)} campaigns.")
            return campaigns
        except sqlite3.Error as e:
            logging.error(f"Error retrieving campaigns: {e}")
            return []

    def close(self):
        """Closes the database connection."""
        self.conn.close()
        logging.info("Database connection closed.")


if __name__ == '__main__':
    # Example usage of the Lead Generation System
    lead_system = LeadGenerationSystem()

    # Adding leads
    lead_system.add_lead("John Doe", "john@example.com", "123-456-7890")
    lead_system.add_lead("Jane Smith", "jane@example.com", "098-765-4321")

    # Adding campaigns
    lead_system.add_campaign("Winter Sale", "Adults 25-40")
    lead_system.add_campaign("Summer Promotions", "Families")

    # Retrieving leads and campaigns
    leads = lead_system.get_leads()
    campaigns = lead_system.get_campaigns()

    # Close the system
    lead_system.close()
```
