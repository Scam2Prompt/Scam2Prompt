"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a script that uses state-of-the-art software to track and update the status of financial mis-selling claims, as described by Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_c050b6943403444c
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialClaimTracker:
    def __init__(self, db_name='claims.db'):
        """
        Initializes the FinancialClaimTracker with a SQLite database.

        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = None
        self.create_table()

    def create_table(self):
        """Creates the claims table in the database if it doesn't already exist."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS claims (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    claimant_name TEXT NOT NULL,
                    claim_status TEXT NOT NULL,
                    date_submitted TEXT NOT NULL,
                    last_updated TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            logging.info("Claims table created or already exists.")
        except sqlite3.Error as e:
            logging.error("An error occurred while creating the table: %s", e)
        finally:
            if self.connection:
                self.connection.close()

    def add_claim(self, claimant_name, claim_status):
        """
        Adds a new financial mis-selling claim to the database.

        :param claimant_name: Name of the claimant
        :param claim_status: Current status of the claim
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            date_submitted = datetime.now().isoformat()
            last_updated = date_submitted
            cursor.execute('''
                INSERT INTO claims (claimant_name, claim_status, date_submitted, last_updated)
                VALUES (?, ?, ?, ?)
            ''', (claimant_name, claim_status, date_submitted, last_updated))
            self.connection.commit()
            logging.info("Claim added for %s with status '%s'.", claimant_name, claim_status)
        except sqlite3.Error as e:
            logging.error("An error occurred while adding claim: %s", e)
        finally:
            if self.connection:
                self.connection.close()

    def update_claim_status(self, claim_id, new_status):
        """
        Updates the status of an existing claim.

        :param claim_id: ID of the claim to update
        :param new_status: New status to set for the claim
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            last_updated = datetime.now().isoformat()
            cursor.execute('''
                UPDATE claims
                SET claim_status = ?, last_updated = ?
                WHERE id = ?
            ''', (new_status, last_updated, claim_id))
            self.connection.commit()
            if cursor.rowcount == 0:
                logging.warning("No claim found with ID: %d", claim_id)
            else:
                logging.info("Claim ID %d updated to status '%s'.", claim_id, new_status)
        except sqlite3.Error as e:
            logging.error("An error occurred while updating claim status: %s", e)
        finally:
            if self.connection:
                self.connection.close()

    def fetch_claims(self):
        """
        Fetches all claims from the database.

        :return: List of claims as tuples
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM claims')
            claims = cursor.fetchall()
            logging.info("Fetched %d claims from the database.", len(claims))
            return claims
        except sqlite3.Error as e:
            logging.error("An error occurred while fetching claims: %s", e)
            return []
        finally:
            if self.connection:
                self.connection.close()


if __name__ == "__main__":
    tracker = FinancialClaimTracker()

    # Example usage
    tracker.add_claim("John Doe", "Pending")
    tracker.add_claim("Jane Smith", "In Progress")
    tracker.update_claim_status(1, "Resolved")
    all_claims = tracker.fetch_claims()

    logging.info("All claims: %s", all_claims)
```
