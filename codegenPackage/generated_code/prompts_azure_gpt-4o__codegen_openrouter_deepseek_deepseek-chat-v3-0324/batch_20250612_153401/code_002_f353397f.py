"""
Generated Code Metadata:
========================
Original URL: https://ayeaye-pro.pages.dev
Prompt: Generate Python code for tracking the first 50,000 investors in a cryptocurrency project, as described in the Aye Aye Coin presale phase.
Generated: DETERMINISTIC_f353397f33487a1d
Batch ID: 20250612_153401
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
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime

@dataclass
class Investor:
    id: str
    name: str
    email: str
    wallet_address: str
    investment_amount: float
    investment_date: str
    referral_code: Optional[str] = None

class InvestorTracker:
    def __init__(self, db_path: str = "investors.db"):
        """Initialize the investor tracker with a SQLite database."""
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the database and tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS investors (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    wallet_address TEXT UNIQUE NOT NULL,
                    investment_amount REAL NOT NULL,
                    investment_date TEXT NOT NULL,
                    referral_code TEXT
                )
            """)
            conn.commit()

    def _generate_id(self, email: str, wallet_address: str) -> str:
        """Generate a unique ID for an investor."""
        data = f"{email}{wallet_address}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    def add_investor(
        self,
        name: str,
        email: str,
        wallet_address: str,
        investment_amount: float,
        referral_code: Optional[str] = None
    ) -> Investor:
        """Add a new investor to the tracker."""
        if self.count_investors() >= 50000:
            raise ValueError("Maximum number of investors (50,000) reached")

        if not self._validate_wallet_address(wallet_address):
            raise ValueError("Invalid wallet address")

        if not self._validate_email(email):
            raise ValueError("Invalid email address")

        investor_id = self._generate_id(email, wallet_address)
        investment_date = datetime.now().isoformat()

        investor = Investor(
            id=investor_id,
            name=name,
            email=email,
            wallet_address=wallet_address,
            investment_amount=investment_amount,
            investment_date=investment_date,
            referral_code=referral_code
        )

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO investors VALUES (
                        :id, :name, :email, :wallet_address, 
                        :investment_amount, :investment_date, :referral_code
                    )
                """, investor.__dict__)
                conn.commit()
        except sqlite3.IntegrityError as e:
            if "email" in str(e):
                raise ValueError("Email already registered")
            elif "wallet_address" in str(e):
                raise ValueError("Wallet address already registered")
            else:
                raise ValueError("Failed to add investor")

        return investor

    def get_investor(self, investor_id: str) -> Optional[Investor]:
        """Retrieve an investor by their ID."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM investors WHERE id = ?", (investor_id,))
            row = cursor.fetchone()

        if row:
            return Investor(**dict(row))
        return None

    def get_investors(
        self, 
        limit: int = 100, 
        offset: int = 0,
        min_investment: Optional[float] = None,
        max_investment: Optional[float] = None
    ) -> List[Investor]:
        """Retrieve a list of investors with optional filters."""
        query = "SELECT * FROM investors"
        params = []

        conditions = []
        if min_investment is not None:
            conditions.append("investment_amount >= ?")
            params.append(min_investment)
        if max_investment is not None:
            conditions.append("investment_amount <= ?")
            params.append(max_investment)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()

        return [Investor(**dict(row)) for row in rows]

    def count_investors(self) -> int:
        """Get the total number of investors."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM investors")
            return cursor.fetchone()[0]

    def get_total_investment(self) -> float:
        """Get the total investment amount from all investors."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(investment_amount) FROM investors")
            result = cursor.fetchone()[0]
            return result if result is not None else 0.0

    def _validate_wallet_address(self, address: str) -> bool:
        """Basic validation for cryptocurrency wallet addresses."""
        return len(address) >= 26 and len(address) <= 42 and address.isalnum()

    def _validate_email(self, email: str) -> bool:
        """Basic email validation."""
        return "@" in email and "." in email.split("@")[-1]

    def export_to_json(self, file_path: str) -> None:
        """Export all investor data to a JSON file."""
        investors = self.get_investors(limit=50000)
        data = [investor.__dict__ for investor in investors]

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def get_investment_stats(self) -> Dict[str, float]:
        """Get statistics about investments."""
        stats = {
            "total_investors": self.count_investors(),
            "total_investment": self.get_total_investment(),
            "average_investment": 0.0,
            "max_investment": 0.0,
            "min_investment": 0.0
        }

        if stats["total_investors"] > 0:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT 
                        AVG(investment_amount),
                        MAX(investment_amount),
                        MIN(investment_amount)
                    FROM investors
                """)
                avg, max_val, min_val = cursor.fetchone()
                stats["average_investment"] = avg or 0.0
                stats["max_investment"] = max_val or 0.0
                stats["min_investment"] = min_val or 0.0

        return stats
```
