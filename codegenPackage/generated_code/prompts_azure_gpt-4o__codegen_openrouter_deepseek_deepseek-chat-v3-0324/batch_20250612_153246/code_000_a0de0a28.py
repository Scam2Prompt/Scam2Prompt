"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write Python code to create a donation tracking system for an NGO, inspired by Youngistaan Foundation's initiatives like "Sponsor Our Talented Children" and "Hunger Hero Program."
Generated: DETERMINISTIC_a0de0a28058bdc1c
Batch ID: 20250612_153246
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
from typing import Optional, List, Dict, Tuple

class DonationTracker:
    """
    A donation tracking system for NGOs to manage donors, beneficiaries, and donations.
    """
    
    def __init__(self, db_name: str = "donation_tracker.db"):
        """
        Initialize the donation tracker with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donors (
                donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                address TEXT,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS programs (
                program_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                start_date TEXT,
                is_active INTEGER DEFAULT 1
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS beneficiaries (
                beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                program_id INTEGER,
                needs_description TEXT,
                is_active INTEGER DEFAULT 1,
                FOREIGN KEY (program_id) REFERENCES programs(program_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                program_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                donation_date TEXT DEFAULT CURRENT_TIMESTAMP,
                payment_method TEXT,
                is_recurring INTEGER DEFAULT 0,
                notes TEXT,
                FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
                FOREIGN KEY (program_id) REFERENCES programs(program_id)
            )
        """)
        
        self.conn.commit()
    
    def add_donor(self, name: str, email: Optional[str] = None, 
                  phone: Optional[str] = None, address: Optional[str] = None) -> int:
        """
        Add a new donor to the system.
        
        Args:
            name: Donor's full name
            email: Donor's email address
            phone: Donor's phone number
            address: Donor's physical address
            
        Returns:
            The ID of the newly created donor
        """
        try:
            self.cursor.execute(
                "INSERT INTO donors (name, email, phone, address) VALUES (?, ?, ?, ?)",
                (name, email, phone, address)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A donor with this email already exists")
    
    def add_program(self, name: str, description: Optional[str] = None, 
                    start_date: Optional[str] = None, is_active: bool = True) -> int:
        """
        Add a new program to the system.
        
        Args:
            name: Program name (must be unique)
            description: Program description
            start_date: Program start date (YYYY-MM-DD format)
            is_active: Whether the program is currently active
            
        Returns:
            The ID of the newly created program
        """
        try:
            self.cursor.execute(
                "INSERT INTO programs (name, description, start_date, is_active) VALUES (?, ?, ?, ?)",
                (name, description, start_date, int(is_active))
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A program with this name already exists")
    
    def add_beneficiary(self, name: str, program_id: int, age: Optional[int] = None,
                        needs_description: Optional[str] = None, is_active: bool = True) -> int:
        """
        Add a new beneficiary to the system.
        
        Args:
            name: Beneficiary's name
            program_id: ID of the program they belong to
            age: Beneficiary's age
            needs_description: Description of their needs
            is_active: Whether they are currently active in the program
            
        Returns:
            The ID of the newly created beneficiary
        """
        self.cursor.execute(
            "INSERT INTO beneficiaries (name, age, program_id, needs_description, is_active) VALUES (?, ?, ?, ?, ?)",
            (name, age, program_id, needs_description, int(is_active))
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def record_donation(self, donor_id: int, program_id: int, amount: float,
                        payment_method: Optional[str] = None, is_recurring: bool = False,
                        notes: Optional[str] = None) -> int:
        """
        Record a new donation in the system.
        
        Args:
            donor_id: ID of the donor
            program_id: ID of the program being donated to
            amount: Donation amount
            payment_method: Payment method used
            is_recurring: Whether this is a recurring donation
            notes: Additional notes about the donation
            
        Returns:
            The ID of the newly recorded donation
        """
        self.cursor.execute(
            """INSERT INTO donations 
            (donor_id, program_id, amount, payment_method, is_recurring, notes) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (donor_id, program_id, amount, payment_method, int(is_recurring), notes)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_donor_donations(self, donor_id: int) -> List[Dict]:
        """
        Get all donations made by a specific donor.
        
        Args:
            donor_id: ID of the donor
            
        Returns:
            List of donation records as dictionaries
        """
        self.cursor.execute("""
            SELECT d.donation_id, p.name as program, d.amount, d.donation_date, 
                   d.payment_method, d.is_recurring, d.notes
            FROM donations d
            JOIN programs p ON d.program_id = p.program_id
            WHERE d.donor_id = ?
            ORDER BY d.donation_date DESC
        """, (donor_id,))
        
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_program_donations(self, program_id: int) -> List[Dict]:
        """
        Get all donations made to a specific program.
        
        Args:
            program_id: ID of the program
            
        Returns:
            List of donation records as dictionaries
        """
        self.cursor.execute("""
            SELECT d.donation_id, dn.name as donor_name, d.amount, d.donation_date, 
                   d.payment_method, d.is_recurring, d.notes
            FROM donations d
            JOIN donors dn ON d.donor_id = dn.donor_id
            WHERE d.program_id = ?
            ORDER BY d.donation_date DESC
        """, (program_id,))
        
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_program_beneficiaries(self, program_id: int) -> List[Dict]:
        """
        Get all beneficiaries of a specific program.
        
        Args:
            program_id: ID of the program
            
        Returns:
            List of beneficiary records as dictionaries
        """
        self.cursor.execute("""
            SELECT beneficiary_id, name, age, needs_description, is_active
            FROM beneficiaries
            WHERE program_id = ?
            ORDER BY name
        """, (program_id,))
        
        columns = [col[0] for col in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_donor_summary(self, donor_id: int) -> Dict:
        """
        Get summary information about a donor.
        
        Args:
            donor_id: ID of the donor
            
        Returns:
            Dictionary containing donor information and donation summary
        """
        # Get donor info
        self.cursor.execute("""
            SELECT name, email, phone, address, registration_date
            FROM donors
            WHERE donor_id = ?
        """, (donor_id,))
        
        donor_info = dict(zip(
            ['name', 'email', 'phone', 'address', 'registration_date'],
            self.cursor.fetchone()
        ))
        
        # Get donation summary
        self.cursor.execute("""
            SELECT COUNT(*) as total_donations, 
                   SUM(amount) as total_amount,
                   SUM(CASE WHEN is_recurring = 1 THEN 1 ELSE 0 END) as recurring_donations
            FROM donations
            WHERE donor_id = ?
        """, (donor_id,))
        
        donation_summary =
