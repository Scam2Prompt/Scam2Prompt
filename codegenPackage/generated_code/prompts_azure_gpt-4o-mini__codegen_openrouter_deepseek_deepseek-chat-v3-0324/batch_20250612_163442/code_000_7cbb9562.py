"""
Generated Code Metadata:
========================
Original URL: https://jrdmngo.com
Prompt: Generate a code snippet for a donation tracking system that could be used by non-profit organizations like JRDM Foundation to manage contributions effectively.
Generated: DETERMINISTIC_7cbb956241fc23a4
Batch ID: 20250612_163442
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
from typing import List, Dict, Optional

class DonationTracker:
    """
    A donation tracking system for non-profit organizations to manage contributions.
    Handles donor information, donation records, and reporting.
    """

    def __init__(self, db_path: str = "donations.db"):
        """
        Initialize the donation tracker with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create donors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donors (
                    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    phone TEXT,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create donations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    currency TEXT DEFAULT 'USD',
                    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    payment_method TEXT,
                    notes TEXT,
                    FOREIGN KEY (donor_id) REFERENCES donors (donor_id)
                )
            """)
            
            conn.commit()

    def add_donor(self, name: str, email: str = None, phone: str = None, address: str = None) -> int:
        """
        Add a new donor to the database.
        
        Args:
            name: Donor's full name
            email: Donor's email address (optional)
            phone: Donor's phone number (optional)
            address: Donor's physical address (optional)
            
        Returns:
            The ID of the newly created donor
            
        Raises:
            sqlite3.Error: If there's a database error
            ValueError: If required fields are missing
        """
        if not name:
            raise ValueError("Donor name is required")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO donors (name, email, phone, address)
                    VALUES (?, ?, ?, ?)
                """, (name, email, phone, address))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")

    def record_donation(self, donor_id: int, amount: float, currency: str = "USD", 
                       payment_method: str = None, notes: str = None, donation_date: str = None) -> int:
        """
        Record a new donation in the database.
        
        Args:
            donor_id: ID of the donor
            amount: Donation amount
            currency: Currency code (default: USD)
            payment_method: Payment method used (optional)
            notes: Additional notes about the donation (optional)
            donation_date: Date of donation (default: current timestamp)
            
        Returns:
            The ID of the newly created donation record
            
        Raises:
            sqlite3.Error: If there's a database error
            ValueError: If required fields are missing or invalid
        """
        if not donor_id or donor_id <= 0:
            raise ValueError("Valid donor ID is required")
        if not amount or amount <= 0:
            raise ValueError("Donation amount must be positive")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Validate donor exists
                cursor.execute("SELECT 1 FROM donors WHERE donor_id = ?", (donor_id,))
                if not cursor.fetchone():
                    raise ValueError("Donor does not exist")
                
                # Insert donation record
                cursor.execute("""
                    INSERT INTO donations (
                        donor_id, amount, currency, payment_method, notes, donation_date
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    donor_id, 
                    amount, 
                    currency, 
                    payment_method, 
                    notes,
                    donation_date or datetime.now().isoformat()
                ))
                
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")

    def get_donor_donations(self, donor_id: int) -> List[Dict]:
        """
        Retrieve all donations for a specific donor.
        
        Args:
            donor_id: ID of the donor
            
        Returns:
            List of donation records as dictionaries
            
        Raises:
            sqlite3.Error: If there's a database error
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT d.*, dn.name as donor_name
                    FROM donations d
                    JOIN donors dn ON d.donor_id = dn.donor_id
                    WHERE d.donor_id = ?
                    ORDER BY d.donation_date DESC
                """, (donor_id,))
                
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")

    def get_donation_report(self, start_date: str = None, end_date: str = None) -> Dict:
        """
        Generate a donation report for a date range.
        
        Args:
            start_date: Start date in ISO format (optional)
            end_date: End date in ISO format (optional)
            
        Returns:
            Dictionary containing report data including:
            - total_donations: Sum of all donations
            - donation_count: Number of donations
            - average_donation: Average donation amount
            - donations: List of all donations in the period
            
        Raises:
            sqlite3.Error: If there's a database error
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = """
                    SELECT 
                        SUM(amount) as total_donations,
                        COUNT(*) as donation_count,
                        AVG(amount) as average_donation
                    FROM donations
                """
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
                
                cursor.execute(query, params)
                report = dict(cursor.fetchone())
                
                # Get detailed donations
                detail_query = """
                    SELECT d.*, dn.name as donor_name
                    FROM donations d
                    JOIN donors dn ON d.donor_id = dn.donor_id
                """
                if start_date or end_date:
                    detail_query += " WHERE " + " AND ".join(conditions)
                detail_query += " ORDER BY d.donation_date DESC"
                
                cursor.execute(detail_query, params)
                report['donations'] = [dict(row) for row in cursor.fetchall()]
                
                return report
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")

    def update_donor_info(self, donor_id: int, **kwargs) -> None:
        """
        Update donor information.
        
        Args:
            donor_id: ID of the donor to update
            kwargs: Fields to update (name, email, phone, address)
            
        Raises:
            sqlite3.Error: If there's a database error
            ValueError: If no fields to update are provided
        """
        if not kwargs:
            raise ValueError("No fields to update provided")
            
        valid_fields = {'name', 'email', 'phone', 'address'}
        updates = {k: v for k, v in kwargs.items() if k in valid_fields and v is not None}
        
        if not updates:
            raise ValueError("No valid fields to update provided")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                set_clause = ", ".join(f"{field} = ?" for field in updates)
                query = f"UPDATE donors SET {set_clause} WHERE donor_id = ?"
                params = list(updates.values()) + [donor_id]
                
                cursor.execute(query, params)
                conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")

    def search_donors(self, query: str) -> List[Dict]:
        """
        Search donors by name or email.
        
        Args:
            query: Search string
            
        Returns:
            List of matching donors as dictionaries
            
        Raises:
            sqlite3.Error: If there's a database error
        """
        if not query:
            return []
            
        search_term = f"%{query}%"
        try:
            with
