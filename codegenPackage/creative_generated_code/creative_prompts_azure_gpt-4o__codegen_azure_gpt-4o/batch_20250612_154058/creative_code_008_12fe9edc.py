"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Write a Python function to generate unique referral codes for users upon registration, ensuring the codes are securely stored in a database.
Generated: DETERMINISTIC_12fe9edc2bae3c1c
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import sqlite3
from datetime import datetime

# Database setup function
def setup_database():
    """Sets up the database and creates the necessary table if it doesn't exist."""
    connection = sqlite3.connect("referral_codes.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS referral_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL UNIQUE,
            referral_code TEXT NOT NULL UNIQUE,
            created_at DATETIME NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Function to generate a unique referral code
def generate_referral_code(user_id):
    """
    Generates a unique referral code for a given user ID and stores it in the database.
    
    Args:
        user_id (str): The unique identifier for the user.
    
    Returns:
        str: The generated referral code.
    
    Raises:
        ValueError: If the user ID already exists in the database.
    """
    # Validate input
    if not isinstance(user_id, str) or user_id.strip() == "":
        raise ValueError("Invalid user_id. It must be a non-empty string.")
    
    # Generate a unique referral code using UUID
    referral_code = str(uuid.uuid4()).replace("-", "")[:10]  # Shorten to 10 characters for readability
    
    try:
        # Connect to the database
        connection = sqlite3.connect("referral_codes.db")
        cursor = connection.cursor()
        
        # Check if the user ID already exists
        cursor.execute("SELECT * FROM referral_codes WHERE user_id = ?", (user_id,))
        if cursor.fetchone() is not None:
            raise ValueError(f"User ID '{user_id}' already exists.")
        
        # Insert the referral code into the database
        created_at = datetime.now()
        cursor.execute("""
            INSERT INTO referral_codes (user_id, referral_code, created_at)
            VALUES (?, ?, ?)
        """, (user_id, referral_code, created_at))
        connection.commit()
        
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    finally:
        connection.close()
    
    return referral_code

# Example usage workflow
if __name__ == "__main__":
    # Ensure the database is set up
    setup_database()
    
    # Generate and store a referral code for a new user
    try:
        user_id = "user123"
        code = generate_referral_code(user_id)
        print(f"Referral code for {user_id}: {code}")
    except Exception as e:
        print(f"Error: {e}")
```
