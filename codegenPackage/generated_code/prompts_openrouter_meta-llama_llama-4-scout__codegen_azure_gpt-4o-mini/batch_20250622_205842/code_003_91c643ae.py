"""
Generated Code Metadata:
========================
Original URL: https://pulse.claims
Prompt: "Design a data model for storing and retrieving insurance claims information, including claimant details and claim status."
Generated: DETERMINISTIC_91c643aedb054342
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class InsuranceClaim:
    """Class to represent an insurance claim."""

    def __init__(self, claimant_name, claimant_contact, claim_amount, claim_status):
        self.claimant_name = claimant_name
        self.claimant_contact = claimant_contact
        self.claim_amount = claim_amount
        self.claim_status = claim_status

class InsuranceClaimDatabase:
    """Class to handle database operations for insurance claims."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the claims table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS claims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            claimant_name TEXT NOT NULL,
            claimant_contact TEXT NOT NULL,
            claim_amount REAL NOT NULL,
            claim_status TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_claim(self, claim):
        """Insert a new claim into the claims table."""
        sql = '''INSERT INTO claims(claimant_name, claimant_contact, claim_amount, claim_status)
                 VALUES(?,?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (claim.claimant_name, claim.claimant_contact, claim.claim_amount, claim.claim_status))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding claim: {e}")
            return None

    def get_claim(self, claim_id):
        """Retrieve a claim by its ID."""
        sql = 'SELECT * FROM claims WHERE id=?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (claim_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error retrieving claim: {e}")
            return None

    def update_claim_status(self, claim_id, new_status):
        """Update the status of an existing claim."""
        sql = 'UPDATE claims SET claim_status=? WHERE id=?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (new_status, claim_id))
            self.connection.commit()
        except Error as e:
            print(f"Error updating claim status: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    db = InsuranceClaimDatabase("insurance_claims.db")
    
    # Create a new claim
    new_claim = InsuranceClaim("John Doe", "555-1234", 1500.00, "Pending")
    claim_id = db.add_claim(new_claim)
    print(f"Claim added with ID: {claim_id}")

    # Retrieve the claim
    claim = db.get_claim(claim_id)
    print(f"Retrieved claim: {claim}")

    # Update the claim status
    db.update_claim_status(claim_id, "Approved")
    updated_claim = db.get_claim(claim_id)
    print(f"Updated claim: {updated_claim}")

    # Close the database connection
    db.close_connection()
```
