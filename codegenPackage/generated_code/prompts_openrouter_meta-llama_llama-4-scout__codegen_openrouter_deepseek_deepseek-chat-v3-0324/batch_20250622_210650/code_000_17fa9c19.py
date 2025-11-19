"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Write a code for a donation tracking system that can be used by a non-profit organization like Viajeras, which supports women who have experienced sexual aggression.
Generated: DETERMINISTIC_17fa9c1938b27158
Batch ID: 20250622_210650
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

class DonationTracker:
    """
    A donation tracking system for non-profit organizations.
    """
    
    def __init__(self, db_name: str = "donations.db"):
        """
        Initialize the donation tracker with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create the database tables if they don't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create donors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    currency TEXT DEFAULT 'USD',
                    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    payment_method TEXT,
                    is_recurring BOOLEAN DEFAULT FALSE,
                    notes TEXT,
                    FOREIGN KEY (donor_id) REFERENCES donors (id)
                )
            """)
            
            conn.commit()
    
    def add_donor(
        self,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None
    ) -> int:
        """
        Add a new donor to the database.
        
        Args:
            name: Donor's full name.
            email: Donor's email address.
            phone: Donor's phone number.
            address: Donor's physical address.
            
        Returns:
            The ID of the newly created donor.
            
        Raises:
            sqlite3.Error: If there's a database error.
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
            raise sqlite3.Error(f"Error adding donor: {e}")
    
    def add_donation(
        self,
        donor_id: int,
        amount: float,
        currency: str = "USD",
        donation_date: Optional[str] = None,
        payment_method: Optional[str] = None,
        is_recurring: bool = False,
        notes: Optional[str] = None
    ) -> int:
        """
        Record a new donation.
        
        Args:
            donor_id: ID of the donor.
            amount: Donation amount.
            currency: Currency code (default: USD).
            donation_date: Date of donation (default: current timestamp).
            payment_method: Payment method used.
            is_recurring: Whether this is a recurring donation.
            notes: Additional notes about the donation.
            
        Returns:
            The ID of the newly created donation.
            
        Raises:
            sqlite3.Error: If there's a database error.
            ValueError: If donor doesn't exist.
        """
        if not self._donor_exists(donor_id):
            raise ValueError(f"Donor with ID {donor_id} does not exist")
            
        try:
            donation_date = donation_date or datetime.now().isoformat()
            
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO donations (
                        donor_id, amount, currency, donation_date,
                        payment_method, is_recurring, notes
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    donor_id, amount, currency, donation_date,
                    payment_method, is_recurring, notes
                ))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error adding donation: {e}")
    
    def _donor_exists(self, donor_id: int) -> bool:
        """
        Check if a donor exists in the database.
        
        Args:
            donor_id: ID of the donor to check.
            
        Returns:
            True if donor exists, False otherwise.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM donors WHERE id = ?", (donor_id,))
            return cursor.fetchone() is not None
    
    def get_donor(self, donor_id: int) -> Dict:
        """
        Retrieve donor information by ID.
        
        Args:
            donor_id: ID of the donor to retrieve.
            
        Returns:
            A dictionary containing donor information.
            
        Raises:
            ValueError: If donor doesn't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, email, phone, address, created_at
                FROM donors WHERE id = ?
            """, (donor_id,))
            donor = cursor.fetchone()
            
            if not donor:
                raise ValueError(f"Donor with ID {donor_id} not found")
                
            return {
                "id": donor[0],
                "name": donor[1],
                "email": donor[2],
                "phone": donor[3],
                "address": donor[4],
                "created_at": donor[5]
            }
    
    def get_donations_by_donor(self, donor_id: int) -> List[Dict]:
        """
        Retrieve all donations from a specific donor.
        
        Args:
            donor_id: ID of the donor.
            
        Returns:
            A list of dictionaries containing donation information.
            
        Raises:
            ValueError: If donor doesn't exist.
        """
        if not self._donor_exists(donor_id):
            raise ValueError(f"Donor with ID {donor_id} does not exist")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, amount, currency, donation_date,
                       payment_method, is_recurring, notes
                FROM donations
                WHERE donor_id = ?
                ORDER BY donation_date DESC
            """, (donor_id,))
            
            donations = []
            for row in cursor.fetchall():
                donations.append({
                    "id": row[0],
                    "amount": row[1],
                    "currency": row[2],
                    "donation_date": row[3],
                    "payment_method": row[4],
                    "is_recurring": bool(row[5]),
                    "notes": row[6]
                })
                
            return donations
    
    def get_all_donors(self) -> List[Dict]:
        """
        Retrieve all donors from the database.
        
        Returns:
            A list of dictionaries containing donor information.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, email, phone, address, created_at
                FROM donors
                ORDER BY name
            """)
            
            donors = []
            for row in cursor.fetchall():
                donors.append({
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "address": row[4],
                    "created_at": row[5]
                })
                
            return donors
    
    def get_total_donations(self) -> Tuple[float, int]:
        """
        Calculate total donations and count.
        
        Returns:
            A tuple containing (total_amount, donation_count).
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(amount), COUNT(id)
                FROM donations
            """)
            total, count = cursor.fetchone()
            return (total or 0.0, count or 0)
    
    def update_donor(
        self,
        donor_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None
    ) -> None:
        """
        Update donor information.
        
        Args:
            donor_id: ID of the donor to update.
            name: New name (optional).
            email: New email (optional).
            phone: New phone (optional).
            address: New address (optional).
            
        Raises:
            ValueError: If donor doesn't exist.
            sqlite3.Error: If there's a database error.
        """
        if not self._donor_exists(donor_id):
            raise ValueError(f"Donor with ID {donor_id} not found")
            
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("name = ?")
                params.append(name)
            if email is not None:
                updates.append
