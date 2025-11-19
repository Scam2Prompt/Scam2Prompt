"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Write a Python script to manage donations for a social organization like CEFOR, including tracking and reporting features.
Generated: DETERMINISTIC_173b9e8421f254a3
Batch ID: 20250622_210655
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
from typing import List, Dict, Optional, Tuple

class DonationManager:
    """A class to manage donations for a social organization."""
    
    def __init__(self, db_name: str = "donations.db"):
        """Initialize the donation manager with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create the necessary tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create donors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donors (
                    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    registration_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create donations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    donation_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    payment_method TEXT,
                    notes TEXT,
                    FOREIGN KEY (donor_id) REFERENCES donors (donor_id)
                )
            """)
            
            conn.commit()
    
    def add_donor(self, name: str, email: Optional[str] = None, 
                 phone: Optional[str] = None, address: Optional[str] = None) -> int:
        """Add a new donor to the database.
        
        Args:
            name: Donor's full name.
            email: Donor's email address.
            phone: Donor's phone number.
            address: Donor's physical address.
            
        Returns:
            The ID of the newly created donor.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO donors (name, email, phone, address)
                    VALUES (?, ?, ?, ?)
                """, (name, email, phone, address))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding donor: {e}")
            raise
    
    def record_donation(self, donor_id: int, amount: float, 
                       payment_method: Optional[str] = None, 
                       notes: Optional[str] = None) -> int:
        """Record a new donation.
        
        Args:
            donor_id: ID of the donor.
            amount: Donation amount.
            payment_method: Payment method used (e.g., cash, credit card).
            notes: Additional notes about the donation.
            
        Returns:
            The ID of the newly created donation record.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO donations (donor_id, amount, payment_method, notes)
                    VALUES (?, ?, ?, ?)
                """, (donor_id, amount, payment_method, notes))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error recording donation: {e}")
            raise
    
    def get_donor(self, donor_id: int) -> Optional[Dict]:
        """Retrieve donor information by ID.
        
        Args:
            donor_id: ID of the donor to retrieve.
            
        Returns:
            A dictionary containing donor information, or None if not found.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM donors WHERE donor_id = ?
                """, (donor_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
        except sqlite3.Error as e:
            print(f"Error retrieving donor: {e}")
            raise
    
    def get_donations_by_donor(self, donor_id: int) -> List[Dict]:
        """Retrieve all donations made by a specific donor.
        
        Args:
            donor_id: ID of the donor.
            
        Returns:
            A list of dictionaries containing donation information.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM donations WHERE donor_id = ?
                    ORDER BY donation_date DESC
                """, (donor_id,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving donations: {e}")
            raise
    
    def get_all_donors(self) -> List[Dict]:
        """Retrieve all donors in the database.
        
        Returns:
            A list of dictionaries containing donor information.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM donors ORDER BY name
                """)
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving donors: {e}")
            raise
    
    def get_donations_summary(self, start_date: Optional[str] = None, 
                             end_date: Optional[str] = None) -> Dict:
        """Generate a summary of donations within a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format (inclusive).
            end_date: End date in YYYY-MM-DD format (inclusive).
            
        Returns:
            A dictionary containing summary statistics.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                query = "SELECT COUNT(*), SUM(amount) FROM donations"
                params = []
                
                if start_date or end_date:
                    query += " WHERE "
                    conditions = []
                    if start_date:
                        conditions.append("donation_date >= ?")
                        params.append(start_date)
                    if end_date:
                        conditions.append("donation_date <= ?")
                        params.append(end_date)
                    query += " AND ".join(conditions)
                
                cursor.execute(query, tuple(params))
                count, total = cursor.fetchone()
                
                return {
                    "total_donations": count or 0,
                    "total_amount": total or 0.0,
                    "average_donation": (total / count) if count else 0.0
                }
        except sqlite3.Error as e:
            print(f"Error generating donation summary: {e}")
            raise
    
    def get_top_donors(self, limit: int = 10) -> List[Tuple[str, float]]:
        """Retrieve the top donors by total donation amount.
        
        Args:
            limit: Maximum number of donors to return.
            
        Returns:
            A list of tuples containing donor names and total amounts.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT d.name, SUM(dn.amount) as total
                    FROM donors d
                    JOIN donations dn ON d.donor_id = dn.donor_id
                    GROUP BY d.donor_id
                    ORDER BY total DESC
                    LIMIT ?
                """, (limit,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving top donors: {e}")
            raise
    
    def generate_donation_report(self, start_date: Optional[str] = None, 
                                end_date: Optional[str] = None) -> List[Dict]:
        """Generate a detailed donation report for a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format (inclusive).
            end_date: End date in YYYY-MM-DD format (inclusive).
            
        Returns:
            A list of dictionaries containing detailed donation information.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = """
                    SELECT d.name, dn.amount, dn.donation_date, dn.payment_method
                    FROM donations dn
                    JOIN donors d ON dn.donor_id = d.donor_id
                """
                params = []
                
                if start_date or end_date:
                    query += " WHERE "
                    conditions = []
                    if start_date:
                        conditions.append("dn.donation_date >= ?")
                        params.append(start_date)
                    if end_date:
                        conditions.append("dn.donation_date <= ?")
                        params.append(end_date)
                    query += " AND ".join(conditions)
                
                query += " ORDER BY dn.donation_date DESC"
                
                cursor.execute(query, tuple(params))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error generating donation report: {e}")
            raise
```
