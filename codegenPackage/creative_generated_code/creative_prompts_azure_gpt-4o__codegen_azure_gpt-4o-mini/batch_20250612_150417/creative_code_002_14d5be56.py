"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.name
Prompt: Generate code for tracking referral analytics in a cryptocurrency exchange platform, inspired by Changelly's referral program that provides detailed analytics and passive income opportunities.
Generated: DETERMINISTIC_14d5be5674999db9
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralAnalytics:
    def __init__(self, db_name='referral_analytics.db'):
        """Initialize the referral analytics system with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for tracking referrals and earnings."""
        try:
            with self.connection:
                self.connection.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referrer_id TEXT NOT NULL,
                    referred_id TEXT NOT NULL,
                    referral_date TEXT NOT NULL,
                    UNIQUE(referrer_id, referred_id)
                );
                ''')
                
                self.connection.execute('''
                CREATE TABLE IF NOT EXISTS earnings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referral_id INTEGER,
                    amount REAL NOT NULL,
                    earning_date TEXT NOT NULL,
                    FOREIGN KEY (referral_id) REFERENCES referrals (id)
                );
                ''')
            logging.info("Tables created successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error creating tables: {e}")

    def add_referral(self, referrer_id, referred_id):
        """Record a new referral in the database."""
        try:
            referral_date = datetime.now().isoformat()
            with self.connection:
                self.connection.execute('''
                INSERT INTO referrals (referrer_id, referred_id, referral_date)
                VALUES (?, ?, ?);
                ''', (referrer_id, referred_id, referral_date))
            logging.info(f"Referral added: {referrer_id} referred {referred_id}.")
        except sqlite3.IntegrityError:
            logging.warning("This referral already exists.")
        except sqlite3.Error as e:
            logging.error(f"Error adding referral: {e}")

    def add_earning(self, referral_id, amount):
        """Record earnings from a referral."""
        try:
            earning_date = datetime.now().isoformat()
            with self.connection:
                self.connection.execute('''
                INSERT INTO earnings (referral_id, amount, earning_date)
                VALUES (?, ?, ?);
                ''', (referral_id, amount, earning_date))
            logging.info(f"Earning added for referral ID {referral_id}: {amount}.")
        except sqlite3.Error as e:
            logging.error(f"Error adding earning: {e}")

    def get_referral_analytics(self, referrer_id):
        """Retrieve the analytics for a specific referrer."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
            SELECT r.referred_id, r.referral_date, COALESCE(SUM(e.amount), 0) AS total_earnings
            FROM referrals r
            LEFT JOIN earnings e ON r.id = e.referral_id
            WHERE r.referrer_id = ?
            GROUP BY r.referred_id, r.referral_date;
            ''', (referrer_id,))
            
            analytics = cursor.fetchall()
            logging.info(f"Analytics retrieved for referrer ID {referrer_id}.")
            return analytics
        except sqlite3.Error as e:
            logging.error(f"Error retrieving analytics: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    analytics = ReferralAnalytics()
    analytics.add_referral('user123', 'user456')
    analytics.add_earning(1, 50.0)  # Assuming referral ID 1 is valid
    print(analytics.get_referral_analytics('user123'))
    analytics.close()
```
