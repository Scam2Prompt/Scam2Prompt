"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Generate a donation and volunteer management system for an animal shelter, referencing the programs offered by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_84598647d317c27e
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_volunteer_system.py
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class AnimalShelterDB:
    """Database handler for the animal shelter donation and volunteer system."""
    
    def __init__(self, db_name: str = "animal_shelter.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                donation_type TEXT NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_recurring BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (donor_id) REFERENCES donors (id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                skills TEXT,
                availability TEXT,
                joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteer_shifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER NOT NULL,
                shift_date DATE NOT NULL,
                shift_type TEXT NOT NULL,
                hours_worked REAL NOT NULL,
                notes TEXT,
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS programs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                active BOOLEAN DEFAULT TRUE
            )
        """)
        
        self.conn.commit()
    
    def add_donor(self, name: str, email: str, phone: str = None, address: str = None) -> int:
        """Add a new donor to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO donors (name, email, phone, address) VALUES (?, ?, ?, ?)",
                (name, email, phone, address)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A donor with this email already exists.")
    
    def record_donation(self, donor_id: int, amount: float, donation_type: str, is_recurring: bool = False) -> int:
        """Record a new donation."""
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        
        self.cursor.execute(
            "INSERT INTO donations (donor_id, amount, donation_type, is_recurring) VALUES (?, ?, ?, ?)",
            (donor_id, amount, donation_type, is_recurring)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_volunteer(self, name: str, email: str, phone: str, skills: str = None, availability: str = None) -> int:
        """Add a new volunteer to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO volunteers (name, email, phone, skills, availability) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, skills, availability)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A volunteer with this email already exists.")
    
    def record_volunteer_shift(self, volunteer_id: int, shift_date: str, shift_type: str, hours_worked: float, notes: str = None) -> int:
        """Record a volunteer shift."""
        if hours_worked <= 0:
            raise ValueError("Hours worked must be positive.")
        
        try:
            parsed_date = datetime.strptime(shift_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        self.cursor.execute(
            "INSERT INTO volunteer_shifts (volunteer_id, shift_date, shift_type, hours_worked, notes) VALUES (?, ?, ?, ?, ?)",
            (volunteer_id, shift_date, shift_type, hours_worked, notes)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_program(self, name: str, description: str = None) -> int:
        """Add a new program offered by the shelter."""
        try:
            self.cursor.execute(
                "INSERT INTO programs (name, description) VALUES (?, ?)",
                (name, description)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A program with this name already exists.")
    
    def get_donor_donations(self, donor_id: int) -> List[Dict]:
        """Get all donations for a specific donor."""
        self.cursor.execute(
            "SELECT id, amount, donation_type, date, is_recurring FROM donations WHERE donor_id = ?",
            (donor_id,)
        )
        return [dict(zip(['id', 'amount', 'type', 'date', 'is_recurring'], row)) for row in self.cursor.fetchall()]
    
    def get_volunteer_shifts(self, volunteer_id: int) -> List[Dict]:
        """Get all shifts for a specific volunteer."""
        self.cursor.execute(
            "SELECT id, shift_date, shift_type, hours_worked, notes FROM volunteer_shifts WHERE volunteer_id = ?",
            (volunteer_id,)
        )
        return [dict(zip(['id', 'date', 'type', 'hours', 'notes'], row)) for row in self.cursor.fetchall()]
    
    def get_total_donations(self) -> float:
        """Get the total amount of donations received."""
        self.cursor.execute("SELECT SUM(amount) FROM donations")
        result = self.cursor.fetchone()[0]
        return result if result is not None else 0.0
    
    def get_total_volunteer_hours(self) -> float:
        """Get the total number of volunteer hours logged."""
        self.cursor.execute("SELECT SUM(hours_worked) FROM volunteer_shifts")
        result = self.cursor.fetchone()[0]
        return result if result is not None else 0.0
    
    def get_donors(self) -> List[Dict]:
        """Get all donors."""
        self.cursor.execute("SELECT id, name, email, phone, address FROM donors")
        return [dict(zip(['id', 'name', 'email', 'phone', 'address'], row)) for row in self.cursor.fetchall()]
    
    def get_volunteers(self) -> List[Dict]:
        """Get all volunteers."""
        self.cursor.execute("SELECT id, name, email, phone, skills, availability FROM volunteers")
        return [dict(zip(['id', 'name', 'email', 'phone', 'skills', 'availability'], row)) for row in self.cursor.fetchall()]
    
    def get_programs(self) -> List[Dict]:
        """Get all programs."""
        self.cursor.execute("SELECT id, name, description, active FROM programs")
        return [dict(zip(['id', 'name', 'description', 'active'], row)) for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

class DonationVolunteerSystem:
    """Main class for the animal shelter donation and volunteer management system."""
    
    def __init__(self):
        self.db = AnimalShelterDB()
    
    def add_donor(self, name: str, email: str, phone: str = None, address: str = None) -> int:
        """Add a new donor."""
        return self.db.add_donor(name, email, phone, address)
    
    def record_donation(self, donor_id: int, amount: float, donation_type: str, is_recurring: bool = False) -> int:
        """Record a new donation."""
        return self.db.record_donation(donor_id, amount, donation_type, is_recurring)
    
    def add_volunteer(self, name: str, email: str, phone: str, skills: str = None, availability: str = None) -> int:
        """Add a new volunteer."""
        return self.db.add_volunteer(name, email, phone, skills, availability)
    
    def record_volunteer_shift(self, volunteer_id: int, shift_date: str, shift_type: str, hours_worked: float, notes: str = None) ->
