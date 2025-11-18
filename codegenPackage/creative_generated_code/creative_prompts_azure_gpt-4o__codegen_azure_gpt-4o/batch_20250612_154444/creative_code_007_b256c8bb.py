"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Generate a script to monitor and log user activity on Gempa777, particularly focusing on deposit amounts and game preferences.
Generated: DETERMINISTIC_b256c8bb65bfaddd
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that monitors and logs user activity for deposit amounts and game preferences. It assumes access to a database or API for Gempa777 user activity data. Replace placeholders with actual implementation details or database credentials.

```python
import logging
import time
from datetime import datetime
import sqlite3

# Configure logging
logging.basicConfig(
    filename='user_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database connection parameters (example uses SQLite; replace as needed)
DB_PATH = 'gempa777_data.db'

def setup_database():
    """
    Ensures the database and necessary tables exist.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Create a table to simulate Gempa777 user activity data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                deposit_amount REAL NOT NULL,
                game_preference TEXT NOT NULL,
                activity_timestamp TEXT NOT NULL
            )
        ''')
        
        # Insert dummy data for simulation purposes
        cursor.execute('''
            INSERT INTO user_activity (username, deposit_amount, game_preference, activity_timestamp)
            VALUES
            ('user1', 100.0, 'Poker', '2023-03-01 14:00:00'),
            ('user2', 250.0, 'Blackjack', '2023-03-01 14:05:00'),
            ('user3', 50.0, 'Slots', '2023-03-01 14:10:00')
        ''')
        conn.commit()
        
    except sqlite3.Error as e:
        logging.error(f"Database setup failed: {e}")
    finally:
        conn.close()

def fetch_user_activity():
    """
    Fetches user activity data from the database.
    Returns:
        list: A list of user activity records.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("SELECT username, deposit_amount, game_preference, activity_timestamp FROM user_activity")
        activity_data = cursor.fetchall()
        
        return activity_data
    except sqlite3.Error as e:
        logging.error(f"Failed to fetch user activity: {e}")
        return []
    finally:
        conn.close()

def log_user_activity():
    """
    Monitors and logs user activity based on deposit amounts and game preferences.
    """
    while True:
        logging.info("Starting user activity monitoring...")
        
        activity_records = fetch_user_activity()
        if not activity_records:
            logging.warning("No activity records found.")
        
        for record in activity_records:
            username, deposit_amount, game_preference, activity_timestamp = record
            logging.info(
                f"User: {username}, Deposit Amount: {deposit_amount}, "
                f"Game Preference: {game_preference}, Timestamp: {activity_timestamp}"
            )
        
        logging.info("User activity monitoring finished. Waiting for next cycle...")
        time.sleep(60)  # Wait for 60 seconds before the next monitoring cycle.

if __name__ == '__main__':
    # Setup database (only needed for simulation; skip if using a real database)
    setup_database()
    
    # Start monitoring and logging user activity
    try:
        log_user_activity()
    except KeyboardInterrupt:
        logging.info("User activity monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

### Notes:
- Replace the SQLite database setup and dummy data insertion with your actual Gempa777 data source (e.g., MySQL, PostgreSQL, or API calls).
- Adjust the monitoring frequency (`time.sleep(60)`) as needed for your use case.
- Ensure proper database credentials and security practices are applied in production.
