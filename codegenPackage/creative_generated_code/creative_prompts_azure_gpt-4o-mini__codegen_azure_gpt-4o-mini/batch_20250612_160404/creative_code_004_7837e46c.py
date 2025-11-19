"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainecotrust.cc
Prompt: Illustrate how to implement a referral commission tracking system in Python, inspired by the 10% referral commission structure mentioned on mainecotrust.cc.
Generated: DETERMINISTIC_7837e46c294c9658
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal, InvalidOperation

# Constants
REFERRAL_COMMISSION_RATE = Decimal('0.10')  # 10% commission rate

class ReferralCommissionSystem:
    def __init__(self, db_name='referral_commissions.db'):
        """Initialize the referral commission system with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        
    def create_tables(self):
        """Create the necessary tables for tracking referrals and commissions."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY,
                    referrer TEXT NOT NULL,
                    referred TEXT NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    commission DECIMAL(10, 2) NOT NULL
                )
            ''')
    
    def add_referral(self, referrer, referred, amount):
        """Add a new referral and calculate the commission.
        
        Args:
            referrer (str): The identifier of the referrer.
            referred (str): The identifier of the referred person.
            amount (str): The transaction amount as a string.

        Raises:
            ValueError: If the amount is not a valid decimal.
        """
        try:
            amount = Decimal(amount)
        except InvalidOperation:
            raise ValueError("Invalid amount format. Please provide a valid number.")
        
        commission = amount * REFERRAL_COMMISSION_RATE
        
        with self.conn:
            self.conn.execute('''
                INSERT INTO referrals (referrer, referred, amount, commission)
                VALUES (?, ?, ?, ?)
            ''', (referrer, referred, amount, commission))
        
    def get_total_commission(self, referrer):
        """Retrieve the total commission earned by a referrer.
        
        Args:
            referrer (str): The identifier of the referrer.

        Returns:
            Decimal: The total commission earned by the referrer.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT SUM(commission) FROM referrals WHERE referrer = ?
        ''', (referrer,))
        result = cursor.fetchone()[0]
        return Decimal(result) if result is not None else Decimal('0.00')
    
    def close(self):
        """Close the database connection."""
        self.conn.close()

def main():
    """Main function to demonstrate the referral commission system."""
    system = ReferralCommissionSystem()

    # Example usage
    try:
        system.add_referral('user123', 'user456', '100.00')
        system.add_referral('user123', 'user789', '200.00')
        
        total_commission = system.get_total_commission('user123')
        print(f"Total commission earned by user123: ${total_commission:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        system.close()

if __name__ == '__main__':
    main()
```
