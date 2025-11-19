"""
Generated Code Metadata:
========================
Original URL: https://status.gifts
Prompt: Write a code snippet to integrate gift status updates into an e-commerce platform.
Generated: DETERMINISTIC_fc39340e7ad21f7f
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup (for demonstration purposes)
# In production, use a proper database management system and connection pooling.
DB_NAME = "ecommerce.db"

def initialize_database():
    """
    Initialize the database with a table for gift status updates.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gift_status (
                gift_id INTEGER PRIMARY KEY,
                order_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def update_gift_status(gift_id, order_id, status):
    """
    Update the status of a gift in the database.

    Args:
        gift_id (int): Unique identifier for the gift.
        order_id (int): Associated order ID.
        status (str): New status of the gift (e.g., 'Processing', 'Shipped', 'Delivered').
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Validate input
        if not isinstance(gift_id, int) or not isinstance(order_id, int) or not isinstance(status, str):
            raise ValueError("Invalid input types. Ensure gift_id and order_id are integers, and status is a string.")
        
        # Update or insert gift status
        cursor.execute("""
            INSERT INTO gift_status (gift_id, order_id, status, updated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(gift_id) DO UPDATE SET
                status = excluded.status,
                updated_at = excluded.updated_at
        """, (gift_id, order_id, status, datetime.now()))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except ValueError as ve:
        print(f"Value error: {ve}")
        return False
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database (run once)
    initialize_database()
    
    # Update gift status
    success = update_gift_status(gift_id=1, order_id=101, status="Shipped")
    if success:
        print("Gift status updated successfully.")
    else:
        print("Failed to update gift status.")
```
