"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: Illustrate how to implement a lead management system that integrates with a marketing strategy for a business opportunity like Money Order Freedom.
Generated: DETERMINISTIC_eab5dcd045f3c733
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Lead Management System for Money Order Freedom Marketing Strategy
This script implements a lead management system that integrates with a marketing strategy.
It allows businesses to collect, store, and manage leads effectively.
"""

import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("lead_management.log"), logging.StreamHandler()]
)

# Database setup
DB_NAME = "leads.db"

def initialize_database():
    """
    Initialize the SQLite database and create the leads table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                source TEXT,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_lead(name, email, phone=None, source="Unknown"):
    """
    Add a new lead to the database.
    :param name: Name of the lead
    :param email: Email of the lead
    :param phone: Phone number of the lead (optional)
    :param source: Source of the lead (e.g., "Facebook Ad", "Google Search")
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO leads (name, email, phone, source, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, source, datetime.now().isoformat()))
        conn.commit()
        logging.info(f"Lead added successfully: {name} ({email})")
    except sqlite3.IntegrityError:
        logging.warning(f"Lead with email {email} already exists.")
    except sqlite3.Error as e:
        logging.error(f"Error adding lead: {e}")
    finally:
        conn.close()

def get_all_leads():
    """
    Retrieve all leads from the database.
    :return: List of leads
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leads")
        leads = cursor.fetchall()
        logging.info(f"Retrieved {len(leads)} leads from the database.")
        return leads
    except sqlite3.Error as e:
        logging.error(f"Error retrieving leads: {e}")
        return []
    finally:
        conn.close()

def delete_lead(email):
    """
    Delete a lead from the database by email.
    :param email: Email of the lead to delete
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM leads WHERE email = ?", (email,))
        conn.commit()
        if cursor.rowcount > 0:
            logging.info(f"Lead with email {email} deleted successfully.")
        else:
            logging.warning(f"No lead found with email {email}.")
    except sqlite3.Error as e:
        logging.error(f"Error deleting lead: {e}")
    finally:
        conn.close()

def main():
    """
    Main function to demonstrate the lead management system.
    """
    initialize_database()

    # Example usage
    add_lead("John Doe", "john.doe@example.com", "123-456-7890", "Facebook Ad")
    add_lead("Jane Smith", "jane.smith@example.com", source="Google Search")

    leads = get_all_leads()
    for lead in leads:
        print(lead)

    delete_lead("john.doe@example.com")

if __name__ == "__main__":
    main()
```
