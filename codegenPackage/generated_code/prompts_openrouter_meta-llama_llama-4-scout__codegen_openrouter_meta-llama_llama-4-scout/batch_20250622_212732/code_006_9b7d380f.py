"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Design a system to track and manage home loan applications, including applicant profiles, offer comparisons, and cashback rewards, using a database or data storage solution.
Generated: DETERMINISTIC_9b7d380f9a244b42
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_loan_management_system.py

import sqlite3
from dataclasses import dataclass
from enum import Enum
from typing import List

class LoanStatus(str, Enum):
    """Loan application status"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
class Applicant:
    """Applicant profile"""
    id: int
    name: str
    email: str
    phone: str
    income: float

@dataclass
class LoanOffer:
    """Loan offer details"""
    id: int
    applicant_id: int
    interest_rate: float
    loan_amount: float
    cashback_reward: float

class HomeLoanManagementSystem:
    """Home loan management system"""

    def __init__(self, db_name: str):
        """Initialize the system with a database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables in the database"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                income REAL NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS loan_offers (
                id INTEGER PRIMARY KEY,
                applicant_id INTEGER NOT NULL,
                interest_rate REAL NOT NULL,
                loan_amount REAL NOT NULL,
                cashback_reward REAL NOT NULL,
                FOREIGN KEY (applicant_id) REFERENCES applicants (id)
            )
        """)
        self.conn.commit()

    def add_applicant(self, applicant: Applicant):
        """Add an applicant to the system"""
        try:
            self.cursor.execute("""
                INSERT INTO applicants (name, email, phone, income)
                VALUES (?, ?, ?, ?)
            """, (applicant.name, applicant.email, applicant.phone, applicant.income))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding applicant: {e}")
            return None

    def add_loan_offer(self, loan_offer: LoanOffer):
        """Add a loan offer to the system"""
        try:
            self.cursor.execute("""
                INSERT INTO loan_offers (applicant_id, interest_rate, loan_amount, cashback_reward)
                VALUES (?, ?, ?, ?)
            """, (loan_offer.applicant_id, loan_offer.interest_rate, loan_offer.loan_amount, loan_offer.cashback_reward))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding loan offer: {e}")
            return None

    def get_applicant(self, applicant_id: int) -> Applicant:
        """Get an applicant's profile"""
        try:
            self.cursor.execute("""
                SELECT * FROM applicants
                WHERE id = ?
            """, (applicant_id,))
            applicant_data = self.cursor.fetchone()
            if applicant_data:
                return Applicant(*applicant_data)
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting applicant: {e}")
            return None

    def get_loan_offers(self, applicant_id: int) -> List[LoanOffer]:
        """Get loan offers for an applicant"""
        try:
            self.cursor.execute("""
                SELECT * FROM loan_offers
                WHERE applicant_id = ?
            """, (applicant_id,))
            loan_offers_data = self.cursor.fetchall()
            loan_offers = []
            for loan_offer_data in loan_offers_data:
                loan_offers.append(LoanOffer(*loan_offer_data))
            return loan_offers
        except sqlite3.Error as e:
            print(f"Error getting loan offers: {e}")
            return []

    def compare_loan_offers(self, applicant_id: int):
        """Compare loan offers for an applicant"""
        loan_offers = self.get_loan_offers(applicant_id)
        if loan_offers:
            best_offer = min(loan_offers, key=lambda x: x.interest_rate)
            print(f"Best loan offer for applicant {applicant_id}:")
            print(f"Interest Rate: {best_offer.interest_rate}%")
            print(f"Loan Amount: {best_offer.loan_amount}")
            print(f"Cashback Reward: {best_offer.cashback_reward}")
        else:
            print(f"No loan offers found for applicant {applicant_id}")

def main():
    system = HomeLoanManagementSystem("home_loan.db")

    # Create applicants
    applicant1 = Applicant(1, "John Doe", "john@example.com", "1234567890", 50000.0)
    applicant2 = Applicant(2, "Jane Doe", "jane@example.com", "9876543210", 60000.0)

    applicant1_id = system.add_applicant(applicant1)
    applicant2_id = system.add_applicant(applicant2)

    # Create loan offers
    loan_offer1 = LoanOffer(1, applicant1_id, 5.0, 100000.0, 1000.0)
    loan_offer2 = LoanOffer(2, applicant1_id, 6.0, 150000.0, 2000.0)
    loan_offer3 = LoanOffer(3, applicant2_id, 4.0, 200000.0, 3000.0)

    system.add_loan_offer(loan_offer1)
    system.add_loan_offer(loan_offer2)
    system.add_loan_offer(loan_offer3)

    # Get applicant profiles
    print("Applicant 1 Profile:")
    applicant1_profile = system.get_applicant(applicant1_id)
    print(applicant1_profile)

    # Compare loan offers
    system.compare_loan_offers(applicant1_id)

if __name__ == "__main__":
    main()
```
