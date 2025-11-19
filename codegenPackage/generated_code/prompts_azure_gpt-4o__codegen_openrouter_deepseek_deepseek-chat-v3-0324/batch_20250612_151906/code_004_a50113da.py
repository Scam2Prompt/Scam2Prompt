"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Develop a Python function that integrates with a database to manage consumer debt portfolios, as described in the B2C debt collection services on Arbitrium.sk.
Generated: DETERMINISTIC_a50113da0beb1945
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional, Tuple
from datetime import datetime

class DebtPortfolioManager:
    """
    A class to manage consumer debt portfolios in a SQLite database.
    Provides CRUD operations for debt records and portfolio management.
    """
    
    def __init__(self, db_path: str = "debt_portfolio.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create the necessary tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create debtors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS debtors (
                    debtor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create debts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS debts (
                    debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    debtor_id INTEGER NOT NULL,
                    original_amount REAL NOT NULL,
                    current_amount REAL NOT NULL,
                    currency TEXT DEFAULT 'EUR',
                    due_date DATE,
                    status TEXT DEFAULT 'active',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (debtor_id) REFERENCES debtors (debtor_id)
                )
            """)
            
            # Create payment_history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS payment_history (
                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    debt_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    payment_method TEXT,
                    notes TEXT,
                    FOREIGN KEY (debt_id) REFERENCES debts (debt_id)
                )
            """)
            
            conn.commit()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(self.db_path)
    
    def add_debtor(
        self,
        first_name: str,
        last_name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None
    ) -> int:
        """
        Add a new debtor to the database.
        
        Args:
            first_name (str): Debtor's first name
            last_name (str): Debtor's last name
            email (str, optional): Debtor's email
            phone (str, optional): Debtor's phone number
            address (str, optional): Debtor's address
            
        Returns:
            int: The ID of the newly created debtor
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO debtors (
                        first_name, last_name, email, phone, address
                    ) VALUES (?, ?, ?, ?, ?)
                """, (first_name, last_name, email, phone, address))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to add debtor: {str(e)}")
    
    def add_debt(
        self,
        debtor_id: int,
        original_amount: float,
        current_amount: float,
        currency: str = "EUR",
        due_date: Optional[str] = None,
        status: str = "active"
    ) -> int:
        """
        Add a new debt record for a debtor.
        
        Args:
            debtor_id (int): ID of the debtor
            original_amount (float): Original debt amount
            current_amount (float): Current debt amount
            currency (str, optional): Currency code (default: EUR)
            due_date (str, optional): Due date in YYYY-MM-DD format
            status (str, optional): Debt status (default: active)
            
        Returns:
            int: The ID of the newly created debt
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO debts (
                        debtor_id, original_amount, current_amount,
                        currency, due_date, status
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (debtor_id, original_amount, current_amount, currency, due_date, status))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to add debt: {str(e)}")
    
    def record_payment(
        self,
        debt_id: int,
        amount: float,
        payment_method: Optional[str] = None,
        notes: Optional[str] = None
    ) -> int:
        """
        Record a payment made against a debt.
        
        Args:
            debt_id (int): ID of the debt being paid
            amount (float): Payment amount
            payment_method (str, optional): Payment method used
            notes (str, optional): Additional notes about the payment
            
        Returns:
            int: The ID of the payment record
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # Record the payment
                cursor.execute("""
                    INSERT INTO payment_history (
                        debt_id, amount, payment_method, notes
                    ) VALUES (?, ?, ?, ?)
                """, (debt_id, amount, payment_method, notes))
                
                # Update the current amount in the debt record
                cursor.execute("""
                    UPDATE debts
                    SET current_amount = current_amount - ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE debt_id = ?
                """, (amount, debt_id))
                
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to record payment: {str(e)}")
    
    def get_debtor_debts(self, debtor_id: int) -> List[Dict]:
        """
        Get all debts for a specific debtor.
        
        Args:
            debtor_id (int): ID of the debtor
            
        Returns:
            List[Dict]: List of debt records as dictionaries
        """
        try:
            with self._get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM debts
                    WHERE debtor_id = ?
                """, (debtor_id,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get debtor debts: {str(e)}")
    
    def get_debt_payment_history(self, debt_id: int) -> List[Dict]:
        """
        Get payment history for a specific debt.
        
        Args:
            debt_id (int): ID of the debt
            
        Returns:
            List[Dict]: List of payment records as dictionaries
        """
        try:
            with self._get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM payment_history
                    WHERE debt_id = ?
                    ORDER BY payment_date DESC
                """, (debt_id,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get payment history: {str(e)}")
    
    def update_debt_status(self, debt_id: int, new_status: str) -> None:
        """
        Update the status of a debt.
        
        Args:
            debt_id (int): ID of the debt to update
            new_status (str): New status value
        """
        valid_statuses = ["active", "paid", "written_off", "in_collection"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE debts
                    SET status = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE debt_id = ?
                """, (new_status, debt_id))
                conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to update debt status: {str(e)}")
    
    def search_debtors(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> List[Dict]:
        """
        Search for debtors based on various criteria.
        
        Args:
            first_name (str, optional): First name to search for
            last_name (str, optional): Last name to search for
            email (str, optional): Email to search for
            phone (str, optional): Phone number to search for
            
        Returns:
            List[Dict]: List of
