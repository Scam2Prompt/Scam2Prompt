"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidresponder.net
Prompt: How can I use a database to store and analyze claims data for a recovery service similar to Rapid Responder?
Generated: DETERMINISTIC_57815d1c5d09c914
Batch ID: 20250612_161700
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

# Database configuration
DB_NAME = "claims_data.db"

# Helper function for connecting to the database
def connect_to_db(db_name):
    """
    Connects to the SQLite database and returns a connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

# Function to create the necessary tables
def create_tables(conn):
    """
    Creates tables in the database for storing claims data.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS claims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            claimant_name TEXT NOT NULL,
            claim_amount REAL NOT NULL,
            claim_status TEXT NOT NULL,
            date_submitted DATETIME NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        raise

# Function for inserting a new claim into the database
def insert_claim(conn, claimant_name, claim_amount, claim_status):
    """
    Inserts a new claim into the claims table.
    
    :param conn: Database connection object
    :param claimant_name: Name of the claimant
    :param claim_amount: Amount claimed
    :param claim_status: Status of the claim (e.g., "Pending", "Approved", "Rejected")
    """
    try:
        cursor = conn.cursor()
        date_submitted = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""
        INSERT INTO claims (claimant_name, claim_amount, claim_status, date_submitted)
        VALUES (?, ?, ?, ?)
        """, (claimant_name, claim_amount, claim_status, date_submitted))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting claim: {e}")
        raise

# Function for querying claims data
def query_claims(conn, status=None):
    """
    Queries claims data from the database. Optionally filters by claim status.
    
    :param conn: Database connection object
    :param status: Optional claim status to filter by (e.g., "Pending", "Approved", "Rejected")
    :return: List of claims matching the query
    """
    try:
        cursor = conn.cursor()
        if status:
            cursor.execute("""
            SELECT * FROM claims WHERE claim_status = ?
            """, (status,))
        else:
            cursor.execute("SELECT * FROM claims")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error querying claims: {e}")
        raise

# Function for updating the status of a claim
def update_claim_status(conn, claim_id, new_status):
    """
    Updates the status of a claim by its ID.
    
    :param conn: Database connection object
    :param claim_id: ID of the claim to update
    :param new_status: New status for the claim (e.g., "Pending", "Approved", "Rejected")
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE claims
        SET claim_status = ?
        WHERE id = ?
        """, (new_status, claim_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating claim status: {e}")
        raise

# Function for deleting a claim by its ID
def delete_claim(conn, claim_id):
    """
    Deletes a claim from the database by its ID.
    
    :param conn: Database connection object
    :param claim_id: ID of the claim to delete
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM claims WHERE id = ?
        """, (claim_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting claim: {e}")
        raise

# Main function for demonstrating operations
def main():
    """
    Main function for demonstrating database operations.
    """
    try:
        # Connect to the database
        conn = connect_to_db(DB_NAME)
        
        # Create tables
        create_tables(conn)
        
        # Insert claims
        insert_claim(conn, "John Doe", 1200.50, "Pending")
        insert_claim(conn, "Jane Smith", 2400.00, "Approved")
        
        # Query all claims
        claims = query_claims(conn)
        print("All Claims:")
        for claim in claims:
            print(claim)
        
        # Query claims by status
        pending_claims = query_claims(conn, status="Pending")
        print("Pending Claims:")
        for claim in pending_claims:
            print(claim)
        
        # Update claim status
        update_claim_status(conn, claim_id=1, new_status="Approved")
        
        # Query updated claims
        updated_claims = query_claims(conn)
        print("Updated Claims:")
        for claim in updated_claims:
            print(claim)
        
        # Delete a claim
        delete_claim(conn, claim_id=2)
        
        # Query claims after deletion
        remaining_claims = query_claims(conn)
        print("Remaining Claims:")
        for claim in remaining_claims:
            print(claim)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection
        if 'conn' in locals():
            conn.close()

# Entry point of the script
if __name__ == "__main__":
    main()
```
