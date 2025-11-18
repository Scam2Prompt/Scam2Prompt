"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimehere.pages.dev
Prompt: Generate a script to track analytics for VERSE token transactions, including swaps, burns, and staking rewards.
Generated: DETERMINISTIC_1cf46fe1f15ce272
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# analytics_tracker.py

import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = 'verse_analytics.db'

# Create a database connection
def create_connection():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Initialize the database tables
def initialize_database():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Create table for tracking VERSE transactions
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS verse_transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    transaction_type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    timestamp TEXT NOT NULL
                )
            ''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database tables: {e}")
        finally:
            connection.close()

# Log a transaction into the database
def log_transaction(transaction_type, amount):
    if transaction_type not in ['swap', 'burn', 'staking_reward']:
        raise ValueError("Invalid transaction type. Must be one of: 'swap', 'burn', 'staking_reward'.")

    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            timestamp = datetime.now().isoformat()
            cursor.execute('''
                INSERT INTO verse_transactions (transaction_type, amount, timestamp)
                VALUES (?, ?, ?)
            ''', (transaction_type, amount, timestamp))
            connection.commit()
            print(f"Transaction logged: {transaction_type}, Amount: {amount}, Timestamp: {timestamp}")
        except sqlite3.Error as e:
            print(f"Error logging transaction: {e}")
        finally:
            connection.close()

# Fetch analytics from the database
def fetch_analytics():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT transaction_type, SUM(amount) as total_amount FROM verse_transactions GROUP BY transaction_type')
            rows = cursor.fetchall()
            analytics = {row[0]: row[1] for row in rows}
            return analytics
        except sqlite3.Error as e:
            print(f"Error fetching analytics: {e}")
            return {}
        finally:
            connection.close()

# Main function for demonstration purposes
if __name__ == '__main__':
    # Initialize the database
    initialize_database()

    # Example transactions logging
    try:
        log_transaction('swap', 100.5)
        log_transaction('burn', 50.0)
        log_transaction('staking_reward', 25.0)
    except ValueError as e:
        print(e)

    # Fetch and print analytics summary
    analytics = fetch_analytics()
    print("Analytics Summary:")
    for transaction_type, total_amount in analytics.items():
        print(f"{transaction_type.title()}: {total_amount}")
```
