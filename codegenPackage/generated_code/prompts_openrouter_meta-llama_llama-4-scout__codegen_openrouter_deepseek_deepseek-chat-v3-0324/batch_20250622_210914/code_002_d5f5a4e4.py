"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write a code snippet to create a simple database for managing donations and volunteer information for an organization like Kibera Hamlets.
Generated: DETERMINISTIC_d5f5a4e4aadb6634
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict

class KiberaHamletsDB:
    """Database handler for Kibera Hamlets organization."""
    
    def __init__(self, db_name: str = "kibera_hamlets.db"):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables for donations and volunteers."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_name TEXT NOT NULL,
                amount REAL NOT NULL,
                donation_date TEXT NOT NULL,
                donation_type TEXT NOT NULL,
                notes TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                skills TEXT,
                availability TEXT,
                join_date TEXT NOT NULL
            )
        """)
        self.conn.commit()
    
    def add_donation(self, donor_name: str, amount: float, donation_date: str, 
                    donation_type: str, notes: Optional[str] = None) -> int:
        """Add a new donation record."""
        try:
            self.cursor.execute("""
                INSERT INTO donations (donor_name, amount, donation_date, donation_type, notes)
                VALUES (?, ?, ?, ?, ?)
            """, (donor_name, amount, donation_date, donation_type, notes))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def add_volunteer(self, name: str, email: str, join_date: str, 
                     phone: Optional[str] = None, skills: Optional[str] = None, 
                     availability: Optional[str] = None) -> int:
        """Add a new volunteer record."""
        try:
            self.cursor.execute("""
                INSERT INTO volunteers (name, email, phone, skills, availability, join_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, email, phone, skills, availability, join_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.conn.rollback()
            raise ValueError("Email already exists in the system")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def get_donations(self, min_amount: Optional[float] = None) -> List[Dict]:
        """Retrieve donation records, optionally filtered by minimum amount."""
        query = "SELECT * FROM donations"
        params = ()
        
        if min_amount is not None:
            query += " WHERE amount >= ?"
            params = (min_amount,)
            
        self.cursor.execute(query, params)
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_volunteers(self) -> List[Dict]:
        """Retrieve all volunteer records."""
        self.cursor.execute("SELECT * FROM volunteers")
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support context manager protocol."""
        self.close()
```
