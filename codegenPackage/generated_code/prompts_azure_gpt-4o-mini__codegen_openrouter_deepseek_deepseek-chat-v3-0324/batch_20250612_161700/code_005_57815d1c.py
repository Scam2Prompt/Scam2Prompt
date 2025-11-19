"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: How can I use a database to store and analyze claims data for a recovery service similar to Rapid Responder?
Generated: DETERMINISTIC_57815d1c5d09c914
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional
from datetime import datetime

class ClaimsDatabase:
    """
    A class to handle database operations for storing and analyzing claims data.
    Uses SQLite as the database backend.
    """

    def __init__(self, db_name: str = "claims_recovery.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS claims (
                claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
                claimant_name TEXT NOT NULL,
                claim_amount REAL NOT NULL,
                claim_date TEXT NOT NULL,
                status TEXT NOT NULL,
                description TEXT,
                recovery_amount REAL DEFAULT 0,
                last_updated TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_claim(self, claimant_name: str, claim_amount: float, description: str = None) -> int:
        """
        Add a new claim to the database.
        
        Args:
            claimant_name: Name of the claimant
            claim_amount: Amount being claimed
            description: Optional description of the claim
            
        Returns:
            The ID of the newly created claim
        """
        current_time = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT INTO claims 
            (claimant_name, claim_amount, claim_date, status, description, last_updated)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (claimant_name, claim_amount, current_time, "Pending", description, current_time))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_claim_status(self, claim_id: int, status: str, recovery_amount: float = 0) -> bool:
        """
        Update the status of a claim and optionally set recovery amount.
        
        Args:
            claim_id: ID of the claim to update
            status: New status (e.g., "Approved", "Denied", "Recovered")
            recovery_amount: Amount recovered (if applicable)
            
        Returns:
            True if update was successful, False otherwise
        """
        current_time = datetime.now().isoformat()
        try:
            self.cursor.execute("""
                UPDATE claims 
                SET status = ?, recovery_amount = ?, last_updated = ?
                WHERE claim_id = ?
            """, (status, recovery_amount, current_time, claim_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False

    def get_claim(self, claim_id: int) -> Optional[Dict]:
        """
        Retrieve a single claim by ID.
        
        Args:
            claim_id: ID of the claim to retrieve
            
        Returns:
            Dictionary with claim details or None if not found
        """
        self.cursor.execute("""
            SELECT * FROM claims WHERE claim_id = ?
        """, (claim_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None

    def get_all_claims(self, status_filter: str = None) -> List[Dict]:
        """
        Retrieve all claims, optionally filtered by status.
        
        Args:
            status_filter: Optional status to filter by (e.g., "Pending", "Approved")
            
        Returns:
            List of dictionaries containing claim details
        """
        query = "SELECT * FROM claims"
        params = ()
        
        if status_filter:
            query += " WHERE status = ?"
            params = (status_filter,)
            
        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_recovery_stats(self) -> Dict:
        """
        Calculate recovery statistics from all claims.
        
        Returns:
            Dictionary containing various recovery statistics
        """
        stats = {}
        
        # Total claims and amounts
        self.cursor.execute("""
            SELECT 
                COUNT(*) as total_claims,
                SUM(claim_amount) as total_claimed,
                SUM(recovery_amount) as total_recovered
            FROM claims
        """)
        row = self.cursor.fetchone()
        if row:
            stats.update({
                'total_claims': row[0],
                'total_claimed': row[1] or 0,
                'total_recovered': row[2] or 0,
                'recovery_rate': (row[2] or 0) / (row[1] or 1) if row[1] else 0
            })
        
        # Status distribution
        self.cursor.execute("""
            SELECT status, COUNT(*) as count 
            FROM claims 
            GROUP BY status
        """)
        stats['status_distribution'] = dict(self.cursor.fetchall())
        
        return stats

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with ClaimsDatabase() as db:
        # Add sample claims
        claim1 = db.add_claim("John Doe", 1000.50, "Equipment damage")
        claim2 = db.add_claim("Jane Smith", 2500.75, "Vehicle accident")
        
        # Update claim status
        db.update_claim_status(claim1, "Approved")
        db.update_claim_status(claim2, "Recovered", 2000.00)
        
        # Retrieve claims
        print("All claims:")
        for claim in db.get_all_claims():
            print(claim)
        
        # Get statistics
        print("\nRecovery statistics:")
        print(db.get_recovery_stats())
```
