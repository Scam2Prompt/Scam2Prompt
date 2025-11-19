"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Write a Python script to manage membership subscriptions for a professional organization like RMP.
Generated: DETERMINISTIC_33876db7f776b609
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Tuple, List, Dict

class MembershipManager:
    """A class to manage membership subscriptions for a professional organization."""
    
    def __init__(self, db_name: str = "membership.db"):
        """Initialize the MembershipManager with a database connection.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create the necessary database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create members table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS members (
                    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    join_date DATE NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE
                )
            """)
            
            # Create subscriptions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS subscriptions (
                    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    plan_type TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    payment_status TEXT DEFAULT 'pending',
                    FOREIGN KEY (member_id) REFERENCES members (member_id)
                )
            """)
            
            # Create payments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subscription_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    payment_date DATE NOT NULL,
                    transaction_id TEXT,
                    payment_method TEXT NOT NULL,
                    FOREIGN KEY (subscription_id) REFERENCES subscriptions (subscription_id)
                )
            """)
            
            conn.commit()
    
    def add_member(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: Optional[str] = None
    ) -> int:
        """Add a new member to the database.
        
        Args:
            first_name: Member's first name.
            last_name: Member's last name.
            email: Member's email address (must be unique).
            phone: Member's phone number (optional).
            
        Returns:
            The member_id of the newly added member.
            
        Raises:
            ValueError: If email already exists in database.
            sqlite3.Error: For database errors.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Check if email already exists
                cursor.execute("SELECT member_id FROM members WHERE email = ?", (email,))
                if cursor.fetchone():
                    raise ValueError("Email already exists in the system")
                
                # Insert new member
                cursor.execute("""
                    INSERT INTO members (first_name, last_name, email, phone, join_date)
                    VALUES (?, ?, ?, ?, ?)
                """, (first_name, last_name, email, phone, datetime.now().date()))
                
                member_id = cursor.lastrowid
                conn.commit()
                return member_id
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {e}")
    
    def create_subscription(
        self,
        member_id: int,
        plan_type: str,
        duration_months: int,
        amount: float,
        payment_method: str,
        transaction_id: Optional[str] = None
    ) -> Tuple[int, int]:
        """Create a new subscription for a member and record the payment.
        
        Args:
            member_id: ID of the member subscribing.
            plan_type: Type of subscription plan (e.g., 'annual', 'monthly').
            duration_months: Duration of subscription in months.
            amount: Payment amount.
            payment_method: Payment method used (e.g., 'credit_card', 'bank_transfer').
            transaction_id: Optional transaction ID from payment processor.
            
        Returns:
            A tuple of (subscription_id, payment_id).
            
        Raises:
            ValueError: If member doesn't exist or invalid duration.
            sqlite3.Error: For database errors.
        """
        if duration_months <= 0:
            raise ValueError("Duration must be positive")
            
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Verify member exists
                cursor.execute("SELECT member_id FROM members WHERE member_id = ?", (member_id,))
                if not cursor.fetchone():
                    raise ValueError("Member does not exist")
                
                # Calculate dates
                start_date = datetime.now().date()
                end_date = start_date + timedelta(days=30 * duration_months)
                
                # Create subscription
                cursor.execute("""
                    INSERT INTO subscriptions (
                        member_id, plan_type, start_date, end_date, payment_status
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (member_id, plan_type, start_date, end_date, 'paid'))
                
                subscription_id = cursor.lastrowid
                
                # Record payment
                cursor.execute("""
                    INSERT INTO payments (
                        subscription_id, amount, payment_date, transaction_id, payment_method
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (subscription_id, amount, start_date, transaction_id, payment_method))
                
                payment_id = cursor.lastrowid
                conn.commit()
                
                return (subscription_id, payment_id)
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {e}")
    
    def renew_subscription(
        self,
        subscription_id: int,
        duration_months: int,
        amount: float,
        payment_method: str,
        transaction_id: Optional[str] = None
    ) -> Tuple[int, int]:
        """Renew an existing subscription.
        
        Args:
            subscription_id: ID of subscription to renew.
            duration_months: Duration of renewal in months.
            amount: Payment amount.
            payment_method: Payment method used.
            transaction_id: Optional transaction ID from payment processor.
            
        Returns:
            A tuple of (new_subscription_id, payment_id).
            
        Raises:
            ValueError: If subscription doesn't exist or invalid duration.
            sqlite3.Error: For database errors.
        """
        if duration_months <= 0:
            raise ValueError("Duration must be positive")
            
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Get current subscription details
                cursor.execute("""
                    SELECT member_id, end_date FROM subscriptions
                    WHERE subscription_id = ?
                """, (subscription_id,))
                result = cursor.fetchone()
                
                if not result:
                    raise ValueError("Subscription does not exist")
                
                member_id, current_end_date = result
                
                # Calculate new dates
                start_date = current_end_date
                end_date = start_date + timedelta(days=30 * duration_months)
                
                # Create new subscription record
                cursor.execute("""
                    INSERT INTO subscriptions (
                        member_id, plan_type, start_date, end_date, payment_status
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (member_id, 'renewal', start_date, end_date, 'paid'))
                
                new_subscription_id = cursor.lastrowid
                
                # Record payment
                cursor.execute("""
                    INSERT INTO payments (
                        subscription_id, amount, payment_date, transaction_id, payment_method
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (new_subscription_id, amount, datetime.now().date(), transaction_id, payment_method))
                
                payment_id = cursor.lastrowid
                conn.commit()
                
                return (new_subscription_id, payment_id)
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {e}")
    
    def cancel_subscription(self, subscription_id: int) -> None:
        """Cancel a subscription by setting its end date to today.
        
        Args:
            subscription_id: ID of subscription to cancel.
            
        Raises:
            ValueError: If subscription doesn't exist.
            sqlite3.Error: For database errors.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Verify subscription exists
                cursor.execute("""
                    SELECT subscription_id FROM subscriptions
                    WHERE subscription_id = ?
                """, (subscription_id,))
                if not cursor.fetchone():
                    raise ValueError("Subscription does not exist")
                
                # Update end date to today
                cursor.execute("""
                    UPDATE subscriptions
                    SET end_date = ?, payment_status = 'cancelled'
                    WHERE subscription_id = ?
                """, (datetime.now().date(), subscription_id))
                
                conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {e}")
    
    def get_member_subscriptions(self, member_id: int) -> List[Dict]:
        """Get all subscriptions for a member.
        
        Args:
            member_id: ID of the member.
            
        Returns:
            List of dictionaries containing subscription details.
            
        Raises:
            sqlite3.Error: For database errors.
        """
        try
