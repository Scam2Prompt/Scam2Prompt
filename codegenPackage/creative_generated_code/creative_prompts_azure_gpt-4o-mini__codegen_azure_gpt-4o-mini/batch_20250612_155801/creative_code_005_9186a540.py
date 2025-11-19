"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Develop a script that automates the distribution of welcome bonuses for new users on a platform similar to venez888.
Generated: DETERMINISTIC_9186a540169edef3
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal
import logging

# Configure logging for debugging and production use
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WelcomeBonusDistributor:
    def __init__(self, db_name="users.db"):
        """Initialize the distributor with the database name."""
        self.db_name = db_name
        
    def connect_to_db(self):
        """Connect to the SQLite database."""
        try:
            connection = sqlite3.connect(self.db_name)
            logging.info("Successfully connected to the database.")
            return connection
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def create_users_table(self):
        """Create the users table if it doesn't exist."""
        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                              id INTEGER PRIMARY KEY,
                              username TEXT NOT NULL UNIQUE,
                              bonus DECIMAL(10, 2) DEFAULT 0.00,
                              is_new_user BOOLEAN NOT NULL DEFAULT 1)''')
            conn.commit()
            logging.info("Users table checked/created in the database.")

    def distribute_welcome_bonus(self, bonus_amount=10.00):
        """Distribute welcome bonuses to new users."""
        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            # Fetch new users who have not received a bonus yet
            cursor.execute("SELECT id, username FROM users WHERE is_new_user = 1")
            new_users = cursor.fetchall()
            
            if not new_users:
                logging.info("No new users to distribute bonuses to.")
                return

            for user_id, username in new_users:
                try:
                    # Update the user's bonus
                    cursor.execute("UPDATE users SET bonus = ?, is_new_user = 0 WHERE id = ?", (Decimal(bonus_amount), user_id))
                    logging.info(f"Distributed welcome bonus of ${bonus_amount} to user: {username}")
                
                except sqlite3.Error as e:
                    logging.error(f"Error distributing bonus to user {username}: {e}")
                    continue
            
            conn.commit()  # Commit all changes at once
            logging.info("All welcome bonuses distributed successfully.")

if __name__ == "__main__":
    distributor = WelcomeBonusDistributor()
    distributor.create_users_table()  # Ensure the table exists
    distributor.distribute_welcome_bonus(bonus_amount=10.00)  # Set the welcome bonus amount
```
