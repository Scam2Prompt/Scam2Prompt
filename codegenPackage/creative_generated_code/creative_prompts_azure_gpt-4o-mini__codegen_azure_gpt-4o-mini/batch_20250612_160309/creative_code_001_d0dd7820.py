"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Write a Python script that implements a referral program for a cryptocurrency staking platform, allowing users to earn up to 0.50% on referral deposits.
Generated: DETERMINISTIC_d0dd7820b4dbe6fd
Batch ID: 20250612_160309
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
REFERRAL_BONUS_PERCENTAGE = Decimal('0.005')  # 0.50% referral bonus

class ReferralProgram:
    def __init__(self, db_name='referral_program.db'):
        """Initialize the ReferralProgram with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables in the database if they don't exist."""
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                referral_code TEXT UNIQUE NOT NULL,
                referred_by TEXT,
                balance DECIMAL NOT NULL DEFAULT 0
            )
            """)

    def add_user(self, username, referral_code, referred_by=None):
        """Add a new user to the database.
        
        Args:
            username (str): The username of the new user.
            referral_code (str): The unique referral code for the new user.
            referred_by (str): The referral code of the user who referred this user.
        
        Returns:
            str: A message indicating the result of the operation.
        """
        try:
            with self.connection:
                self.connection.execute("""
                INSERT INTO users (username, referral_code, referred_by)
                VALUES (?, ?, ?)
                """, (username, referral_code, referred_by))
            return f"User {username} added successfully."
        except sqlite3.IntegrityError:
            return "Error: Referral code already exists."

    def deposit(self, referral_code, amount):
        """Process a deposit for a user and apply referral bonus if applicable.
        
        Args:
            referral_code (str): The referral code of the user making the deposit.
            amount (Decimal): The deposit amount.

        Returns:
            str: A message indicating the result of the deposit operation.
        """
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")

            # Update the user's balance
            with self.connection:
                self.connection.execute("""
                UPDATE users SET balance = balance + ?
                WHERE referral_code = ?
                """, (amount, referral_code))

            # Apply referral bonus if the user was referred by someone
            referred_by = self.get_referrer(referral_code)
            if referred_by:
                self.apply_referral_bonus(referred_by, amount)

            return f"Deposit of {amount} processed successfully."
        except ValueError as ve:
            return str(ve)
        except Exception as e:
            return f"An error occurred during deposit: {str(e)}"

    def apply_referral_bonus(self, referred_by, amount):
        """Apply a referral bonus to the referrer.

        Args:
            referred_by (str): The referral code of the referrer.
            amount (Decimal): The deposit amount from the new user.
        """
        bonus = amount * REFERRAL_BONUS_PERCENTAGE
        with self.connection:
            self.connection.execute("""
            UPDATE users SET balance = balance + ?
            WHERE referral_code = ?
            """, (bonus, referred_by))

    def get_referrer(self, referral_code):
        """Get the referral code of the user who referred the current user.

        Args:
            referral_code (str): The referral code of the current user.

        Returns:
            str or None: The referral code of the referrer, or None if not applicable.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT referred_by FROM users WHERE referral_code = ?
        """, (referral_code,))
        result = cursor.fetchone()
        return result[0] if result else None

    def close(self):
        """Close the database connection."""
        self.connection.close()


if __name__ == "__main__":
    # Example usage of the ReferralProgram class
    referral_program = ReferralProgram()

    # Adding users
    print(referral_program.add_user("alice", "alice_referral"))
    print(referral_program.add_user("bob", "bob_referral", "alice_referral"))

    # Processing deposits
    print(referral_program.deposit("alice_referral", Decimal('1000.00')))
    print(referral_program.deposit("bob_referral", Decimal('2000.00')))

    # Closing the program
    referral_program.close()
```
