"""
Generated Code Metadata:
========================
Original URL: https://shift4strategy.com
Prompt: Develop a code-based solution to track sales-qualified leads and measure their impact on profitability, inspired by SHIFT4's client success stories.
Generated: DETERMINISTIC_6d146ab51b512284
Batch ID: 20250612_145306
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

# Database setup
DATABASE_NAME = 'sales_leads.db'

def create_database():
    """Create a SQLite database and a table for tracking sales-qualified leads."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create table for sales-qualified leads
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            revenue_generated REAL DEFAULT 0.0
        )
    ''')
    
    conn.commit()
    conn.close()

def add_lead(name, email, status):
    """Add a new sales-qualified lead to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO leads (name, email, status)
            VALUES (?, ?, ?)
        ''', (name, email, status))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: A lead with email '{email}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_lead_status(lead_id, new_status):
    """Update the status of an existing lead."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            UPDATE leads
            SET status = ?
            WHERE id = ?
        ''', (new_status, lead_id))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while updating lead status: {e}")
    finally:
        conn.close()

def record_revenue(lead_id, revenue):
    """Record revenue generated from a specific lead."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            UPDATE leads
            SET revenue_generated = revenue_generated + ?
            WHERE id = ?
        ''', (revenue, lead_id))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while recording revenue: {e}")
    finally:
        conn.close()

def get_lead_report():
    """Generate a report of all leads and their revenue impact."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM leads')
        leads = cursor.fetchall()
        
        print("Lead Report:")
        print("ID | Name | Email | Status | Created At | Revenue Generated")
        print("-" * 70)
        for lead in leads:
            print(f"{lead[0]} | {lead[1]} | {lead[2]} | {lead[3]} | {lead[4]} | ${lead[5]:.2f}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
    # Example usage
    add_lead("John Doe", "john.doe@example.com", "Qualified")
    add_lead("Jane Smith", "jane.smith@example.com", "Qualified")
    update_lead_status(1, "Converted")
    record_revenue(1, 1500.00)
    get_lead_report()
```
