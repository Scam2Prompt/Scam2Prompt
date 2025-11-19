"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Write Python code to create an online donation system for a non-profit organization, including features for tracking donations and generating financial reports, inspired by the "موقع جمع التبرعات" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_d52a4d089c2e0514
Batch ID: 20250612_153224
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
from dataclasses import dataclass
import csv
import os

@dataclass
class Donor:
    id: int
    name: str
    email: str
    phone: str
    address: str

@dataclass
class Donation:
    id: int
    donor_id: int
    amount: float
    donation_date: str
    payment_method: str
    campaign: str
    notes: str

class DonationSystem:
    def __init__(self, db_name: str = "donations.db"):
        """Initialize the donation system with database connection."""
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create donors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    address TEXT
                )
            """)
            
            # Create donations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    donor_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    donation_date TEXT NOT NULL,
                    payment_method TEXT NOT NULL,
                    campaign TEXT,
                    notes TEXT,
                    FOREIGN KEY (donor_id) REFERENCES donors (id)
                )
            """)
            conn.commit()

    def add_donor(self, name: str, email: str = None, phone: str = None, address: str = None) -> int:
        """Add a new donor to the system."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO donors (name, email, phone, address) VALUES (?, ?, ?, ?)",
                    (name, email, phone, address)
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding donor: {e}")
            return -1

    def add_donation(
        self,
        donor_id: int,
        amount: float,
        payment_method: str,
        campaign: str = None,
        notes: str = None,
        donation_date: str = None
    ) -> int:
        """Record a new donation."""
        if donation_date is None:
            donation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """INSERT INTO donations 
                    (donor_id, amount, donation_date, payment_method, campaign, notes) 
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (donor_id, amount, donation_date, payment_method, campaign, notes)
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding donation: {e}")
            return -1

    def get_donor(self, donor_id: int) -> Optional[Donor]:
        """Retrieve donor information by ID."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM donors WHERE id = ?", (donor_id,))
                row = cursor.fetchone()
                if row:
                    return Donor(*row)
                return None
        except sqlite3.Error as e:
            print(f"Error retrieving donor: {e}")
            return None

    def get_donations_by_donor(self, donor_id: int) -> List[Donation]:
        """Get all donations made by a specific donor."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM donations WHERE donor_id = ?", (donor_id,))
                return [Donation(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving donations: {e}")
            return []

    def get_all_donations(self, start_date: str = None, end_date: str = None) -> List[Donation]:
        """Get all donations, optionally filtered by date range."""
        query = "SELECT * FROM donations"
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
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, tuple(params))
                return [Donation(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving donations: {e}")
            return []

    def generate_financial_report(
        self, 
        start_date: str = None, 
        end_date: str = None,
        output_format: str = "console"
    ) -> Optional[str]:
        """Generate a financial report of donations."""
        donations = self.get_all_donations(start_date, end_date)
        total = sum(d.amount for d in donations)
        report_data = {
            "total_donations": len(donations),
            "total_amount": total,
            "start_date": start_date or "Beginning",
            "end_date": end_date or "Now",
            "donations": donations
        }

        if output_format == "console":
            print("\n=== Financial Report ===")
            print(f"Period: {report_data['start_date']} to {report_data['end_date']}")
            print(f"Total Donations: {report_data['total_donations']}")
            print(f"Total Amount: {report_data['total_amount']:.2f}")
            print("\nRecent Donations:")
            for donation in donations[-10:]:
                print(f"- {donation.amount:.2f} on {donation.donation_date} (Method: {donation.payment_method})")
            return None
        elif output_format == "csv":
            filename = f"donation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["ID", "Donor ID", "Amount", "Date", "Payment Method", "Campaign"])
                    for donation in donations:
                        writer.writerow([
                            donation.id,
                            donation.donor_id,
                            donation.amount,
                            donation.donation_date,
                            donation.payment_method,
                            donation.campaign
                        ])
                return os.path.abspath(filename)
            except IOError as e:
                print(f"Error writing CSV report: {e}")
                return None
        else:
            print("Invalid output format. Choose 'console' or 'csv'.")
            return None

    def get_donations_by_campaign(self, campaign: str) -> Tuple[List[Donation], float]:
        """Get all donations for a specific campaign and their total amount."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM donations WHERE campaign = ?",
                    (campaign,)
                )
                donations = [Donation(*row) for row in cursor.fetchall()]
                total = sum(d.amount for d in donations)
                return donations, total
        except sqlite3.Error as e:
            print(f"Error retrieving campaign donations: {e}")
            return [], 0.0

    def backup_database(self, backup_path: str) -> bool:
        """Create a backup of the database."""
        try:
            with sqlite3.connect(self.db_name) as source:
                with sqlite3.connect(backup_path) as target:
                    source.backup(target)
            return True
        except sqlite3.Error as e:
            print(f"Error creating database backup: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = DonationSystem()
    
    # Add a donor
    donor_id = system.add_donor(
        name="Ahmed Mohammed",
        email="ahmed@example.com",
        phone="+966501234567",
        address="Riyadh, Saudi Arabia"
    )
    
    # Add a donation
    if donor_id > 0:
        donation_id = system.add_donation(
            donor_id=donor_id,
            amount=500.00,
            payment_method="Credit Card",
            campaign="Ramadan Campaign",
            notes="Monthly donation"
        )
    
    # Generate a report
    system.generate_financial_report(
        start_date="2023-01-01",
        end_date="2023-12-31",
        output_format
