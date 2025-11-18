"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxbinaryinvestpro.com
Prompt: Generate code to create a referral program system that matches the structure outlined by Fxbinaryinvestpro, including referral income tracking.
Generated: DETERMINISTIC_70c6c0b0b181d689
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class ReferralProgram:
    def __init__(self, db_file):
        """Initialize the referral program with the specified database file."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database successful.")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def create_tables(self):
        """Create tables for users and referrals in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    referral_code TEXT NOT NULL UNIQUE,
                    referred_by TEXT,
                    earned_income REAL DEFAULT 0.0
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    referral_user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (referral_user_id) REFERENCES users (id)
                );
            """)
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while creating tables.")

    def add_user(self, username, referral_code, referred_by=None):
        """Add a new user to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users (username, referral_code, referred_by) 
                VALUES (?, ?, ?);
            """, (username, referral_code, referred_by))
            self.connection.commit()
            print(f"User '{username}' added successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while adding user.")

    def add_referral(self, user_id, referral_user_id):
        """Record a referral made by a user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO referrals (user_id, referral_user_id) 
                VALUES (?, ?);
            """, (user_id, referral_user_id))
            self.connection.commit()
            print("Referral recorded successfully.")
            self.update_earned_income(referral_user_id)
        except Error as e:
            print(f"Error '{e}' occurred while adding referral.")

    def update_earned_income(self, user_id):
        """Update the earned income for a user based on referrals."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE users
                SET earned_income = earned_income + 10.0
                WHERE id = ?;
            """, (user_id,))
            self.connection.commit()
            print(f"Income updated for user ID: {user_id}.")
        except Error as e:
            print(f"Error '{e}' occurred while updating earned income.")

    def get_user_income(self, user_id):
        """Retrieve the earned income for a specific user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT earned_income FROM users WHERE id = ?;
            """, (user_id,))
            income = cursor.fetchone()
            return income[0] if income else None
        except Error as e:
            print(f"Error '{e}' occurred while fetching user income.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    referral_system = ReferralProgram("referral_program.db")
    
    # Adding users
    referral_system.add_user("Alice", "ALICE123")
    referral_system.add_user("Bob", "BOB123", "ALICE123")
    
    # Adding referral
    referral_system.add_referral(1, 2)  # Bob was referred by Alice
    
    # Getting user income
    income = referral_system.get_user_income(1)
    print(f"Alice's earned income: {income}")
    
    # Close the connection
    referral_system.close_connection()
```
