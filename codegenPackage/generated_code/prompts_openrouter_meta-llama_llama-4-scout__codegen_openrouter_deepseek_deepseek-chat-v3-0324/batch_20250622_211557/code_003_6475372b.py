"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Develop a donation tracking system using a suitable programming language, incorporating features like donor information, contribution amounts, and vehicle specifications, inspired by Dysnix's fundraising efforts.
Generated: DETERMINISTIC_6475372bf6900e82
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Donation Tracking System

This system tracks donor information, contribution amounts, and vehicle specifications
for fundraising efforts inspired by Dysnix's initiatives.

Features:
- Add, update, and view donor records
- Track donation amounts and dates
- Store vehicle specifications for vehicle donation programs
- Generate reports on donations
"""

import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class DonationTracker:
    """Main class for handling donation tracking operations."""

    def __init__(self, db_name: str = "donations.db"):
        """Initialize the tracker with a SQLite database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip_code TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                donation_date DATE NOT NULL,
                payment_method TEXT,
                is_recurring BOOLEAN DEFAULT 0,
                notes TEXT,
                FOREIGN KEY (donor_id) REFERENCES donors(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                vin TEXT UNIQUE,
                condition TEXT,
                estimated_value REAL,
                donation_date DATE NOT NULL,
                FOREIGN KEY (donor_id) REFERENCES donors(id)
            )
        """)
        
        self.conn.commit()

    def add_donor(
        self,
        first_name: str,
        last_name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip_code: Optional[str] = None
    ) -> int:
        """Add a new donor to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO donors (
                    first_name, last_name, email, phone, address, city, state, zip_code
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, email, phone, address, city, state, zip_code))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError("Email already exists in the system") from e

    def add_donation(
        self,
        donor_id: int,
        amount: float,
        donation_date: Optional[str] = None,
        payment_method: Optional[str] = None,
        is_recurring: bool = False,
        notes: Optional[str] = None
    ) -> int:
        """Record a new donation."""
        if donation_date is None:
            donation_date = datetime.now().strftime("%Y-%m-%d")
            
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO donations (
                    donor_id, amount, donation_date, payment_method, is_recurring, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (donor_id, amount, donation_date, payment_method, is_recurring, notes))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError("Invalid donor ID") from e

    def add_vehicle(
        self,
        donor_id: int,
        make: str,
        model: str,
        year: int,
        vin: Optional[str] = None,
        condition: Optional[str] = None,
        estimated_value: Optional[float] = None,
        donation_date: Optional[str] = None
    ) -> int:
        """Record a vehicle donation."""
        if donation_date is None:
            donation_date = datetime.now().strftime("%Y-%m-%d")
            
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO vehicles (
                    donor_id, make, model, year, vin, condition, estimated_value, donation_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (donor_id, make, model, year, vin, condition, estimated_value, donation_date))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError("VIN already exists in the system") from e
            raise ValueError("Invalid donor ID") from e

    def get_donor(self, donor_id: int) -> Optional[Dict]:
        """Retrieve donor information by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM donors WHERE id = ?", (donor_id,))
        row = cursor.fetchone()
        
        if row is None:
            return None
            
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))

    def get_donations_by_donor(self, donor_id: int) -> List[Dict]:
        """Get all donations for a specific donor."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM donations WHERE donor_id = ?", (donor_id,))
        rows = cursor.fetchall()
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def get_vehicles_by_donor(self, donor_id: int) -> List[Dict]:
        """Get all vehicle donations for a specific donor."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM vehicles WHERE donor_id = ?", (donor_id,))
        rows = cursor.fetchall()
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def get_total_donations(self) -> float:
        """Calculate the total amount of all donations."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM donations")
        total = cursor.fetchone()[0]
        return total if total is not None else 0.0

    def generate_donation_report(self, start_date: str, end_date: str) -> List[Dict]:
        """Generate a report of donations between two dates."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT d.id, dn.first_name, dn.last_name, d.amount, d.donation_date, d.payment_method
            FROM donations d
            JOIN donors dn ON d.donor_id = dn.id
            WHERE d.donation_date BETWEEN ? AND ?
            ORDER BY d.donation_date DESC
        """, (start_date, end_date))
        
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Support for context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting context."""
        self.close()


# Example usage
if __name__ == "__main__":
    with DonationTracker() as tracker:
        # Add a donor
        donor_id = tracker.add_donor(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        
        # Add a donation
        tracker.add_donation(
            donor_id=donor_id,
            amount=100.00,
            payment_method="Credit Card"
        )
        
        # Add a vehicle donation
        tracker.add_vehicle(
            donor_id=donor_id,
            make="Toyota",
            model="Camry",
            year=2015,
            vin="1234567890ABCDEFG"
        )
        
        # Generate a report
        today = datetime.now().strftime("%Y-%m-%d")
        report = tracker.generate_donation_report("2023-01-01", today)
        print("Donation Report:")
        for donation in report:
            print(f"{donation['first_name']} {donation['last_name']}: ${donation['amount']} on {donation['donation_date']}")
        
        print(f"Total donations: ${tracker.get_total_donations():.2f}")
```
