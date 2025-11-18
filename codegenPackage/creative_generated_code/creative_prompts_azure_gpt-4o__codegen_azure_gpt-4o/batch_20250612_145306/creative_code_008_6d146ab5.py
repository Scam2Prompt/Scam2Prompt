"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shift4strategy.com
Prompt: Develop a code-based solution to track sales-qualified leads and measure their impact on profitability, inspired by SHIFT4's client success stories.
Generated: DETERMINISTIC_6d146ab51b512284
Batch ID: 20250612_145306
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

class SalesQualifiedLeadTracker:
    """
    A class to track and measure the impact of sales-qualified leads (SQLs) on profitability.
    """

    def __init__(self, db_name="leads_tracker.db"):
        """
        Initializes the database connection and ensures the necessary tables exist.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables to store leads and profitability data.
        """
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                lead_source TEXT,
                qualified BOOLEAN NOT NULL CHECK (qualified IN (0, 1)),
                created_at TEXT NOT NULL
            )
            """)

            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS profitability (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER NOT NULL,
                revenue_generated REAL NOT NULL,
                cost REAL NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (lead_id) REFERENCES leads (id)
            )
            """)

    def add_lead(self, name, email, lead_source, qualified=False):
        """
        Adds a new lead to the database.

        :param name: Name of the lead.
        :param email: Email of the lead.
        :param lead_source: Source of the lead (e.g., referral, ad campaign).
        :param qualified: Whether the lead is sales-qualified.
        """
        try:
            with self.conn:
                self.conn.execute("""
                INSERT INTO leads (name, email, lead_source, qualified, created_at)
                VALUES (?, ?, ?, ?, ?)
                """, (name, email, lead_source, int(qualified), datetime.now().isoformat()))
        except sqlite3.IntegrityError:
            print(f"Error: Email {email} already exists in the database.")

    def qualify_lead(self, email):
        """
        Marks a lead as sales-qualified.

        :param email: Email of the lead to mark as qualified.
        """
        with self.conn:
            self.conn.execute("""
            UPDATE leads
            SET qualified = 1
            WHERE email = ?
            """, (email,))

    def add_profitability_data(self, email, revenue_generated, cost):
        """
        Adds profitability data for a sales-qualified lead.

        :param email: Email of the lead.
        :param revenue_generated: Revenue generated from the lead.
        :param cost: Cost associated with the lead.
        """
        with self.conn:
            lead_id = self.conn.execute("""
            SELECT id FROM leads WHERE email = ? AND qualified = 1
            """, (email,)).fetchone()

            if lead_id:
                self.conn.execute("""
                INSERT INTO profitability (lead_id, revenue_generated, cost, created_at)
                VALUES (?, ?, ?, ?)
                """, (lead_id[0], revenue_generated, cost, datetime.now().isoformat()))
            else:
                print(f"Error: Lead with email {email} is not qualified or does not exist.")

    def calculate_profitability(self):
        """
        Calculates and prints the total profitability from all sales-qualified leads.
        """
        with self.conn:
            result = self.conn.execute("""
            SELECT SUM(revenue_generated - cost) AS total_profit
            FROM profitability
            """).fetchone()

            total_profit = result[0] if result[0] is not None else 0
            print(f"Total Profitability: ${total_profit:.2f}")

    def list_leads(self):
        """
        Lists all leads in the database.
        """
        with self.conn:
            leads = self.conn.execute("""
            SELECT id, name, email, lead_source, qualified, created_at
            FROM leads
            """).fetchall()

            for lead in leads:
                print(lead)

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()


# Example usage of the SalesQualifiedLeadTracker class
if __name__ == "__main__":
    tracker = SalesQualifiedLeadTracker()

    # Adding new leads
    tracker.add_lead("John Doe", "john.doe@example.com", "Google Ads", False)
    tracker.add_lead("Jane Smith", "jane.smith@example.com", "Referral", True)

    # Qualifying a lead
    tracker.qualify_lead("john.doe@example.com")

    # Adding profitability data
    tracker.add_profitability_data("jane.smith@example.com", 5000, 1200)
    tracker.add_profitability_data("john.doe@example.com", 3000, 800)

    # Calculating profitability
    tracker.calculate_profitability()

    # Listing all leads
    tracker.list_leads()

    # Closing the tracker
    tracker.close()
```
