"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinjoin.cc
Prompt: Write code to securely store and manage CoinJoin IDs for tracking transactions, ensuring compliance with the 48-hour record removal policy.
Generated: DETERMINISTIC_ac7b361ea5d7735e
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import os
import time
from datetime import datetime, timedelta

# Constants
DB_FILE = "coinjoin_records.db"
RETENTION_PERIOD_HOURS = 48

# Ensure database file is stored securely
os.umask(0o077)  # Restrict file permissions for security

# Initialize the database
def initialize_database():
    """Create the database and table if not already present."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CoinJoinRecords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coinjoin_id TEXT NOT NULL UNIQUE,
            timestamp DATETIME NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add a CoinJoin ID to the database
def add_coinjoin_id(coinjoin_id):
    """
    Add a new CoinJoin ID to the database with the current timestamp.
    Args:
        coinjoin_id (str): The unique CoinJoin ID.
    Raises:
        ValueError: If the coinjoin_id is empty or None.
    """
    if not coinjoin_id:
        raise ValueError("CoinJoin ID cannot be empty or None.")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO CoinJoinRecords (coinjoin_id, timestamp)
            VALUES (?, ?)
        """, (coinjoin_id, datetime.now()))
        conn.commit()
    except sqlite3.IntegrityError:
        # Handle duplicate CoinJoin ID error
        print(f"CoinJoin ID '{coinjoin_id}' already exists in the database.")
    finally:
        conn.close()

# Remove old CoinJoin IDs that fall outside the retention period
def cleanup_old_records():
    """Delete records older than the retention period."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cutoff_time = datetime.now() - timedelta(hours=RETENTION_PERIOD_HOURS)
    cursor.execute("""
        DELETE FROM CoinJoinRecords
        WHERE timestamp < ?
    """, (cutoff_time,))
    conn.commit()
    conn.close()

# Retrieve all stored CoinJoin IDs
def get_all_coinjoin_ids():
    """
    Fetch all CoinJoin IDs from the database.
    Returns:
        list of tuple: Each tuple contains (coinjoin_id, timestamp).
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT coinjoin_id, timestamp
        FROM CoinJoinRecords
    """)
    records = cursor.fetchall()
    conn.close()
    return records

# Main entry point for testing the script functionality
if __name__ == "__main__":
    initialize_database()
    
    # Example usage (replace with actual application logic)
    try:
        add_coinjoin_id("test-coinjoin-id-123")
        add_coinjoin_id("test-coinjoin-id-456")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("Stored CoinJoin IDs:")
    for record in get_all_coinjoin_ids():
        print(record)
    
    print("Cleaning up old records...")
    cleanup_old_records()
    
    print("Remaining CoinJoin IDs after cleanup:")
    for record in get_all_coinjoin_ids():
        print(record)
```
