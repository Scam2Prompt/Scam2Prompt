"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Generate a code snippet for a donation system that allows users to contribute to the Shiv Vedika Trust, ensuring secure transactions.
Generated: DETERMINISTIC_8e553906e00d2bbf
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from datetime import datetime

# Importing secure payment library (hypothetical for demonstration)
# In production, use a trusted payment gateway API (e.g., Stripe, PayPal)
import secure_payment_gateway

# Database initialization
DB_NAME = 'donations.db'

def init_db():
    """
    Initialize the SQLite database for storing donation records.
    Create the table if it doesn't already exist.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                transaction_id TEXT NOT NULL UNIQUE,
                date TEXT NOT NULL
            )
        ''')
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()

def generate_transaction_id(user_email, amount):
    """
    Generate a unique transaction ID using a hash of the user's email, amount, and timestamp.
    """
    data = f"{user_email}-{amount}-{datetime.now().isoformat()}"
    return hashlib.sha256(data.encode()).hexdigest()

def process_donation(name, email, amount):
    """
    Process a donation by verifying inputs, interacting with the payment gateway,
    and storing the transaction record in the database.
    """
    # Input validation
    if not name or not email or amount <= 0:
        raise ValueError("Invalid input: Name, email, and amount are required and must be valid.")

    # Generate unique transaction ID
    transaction_id = generate_transaction_id(email, amount)

    try:
        # Interact with the secure payment gateway (hypothetical API call)
        payment_status = secure_payment_gateway.process_payment(email=email, amount=amount)

        # If payment is successful, store the record in the database
        if payment_status['success']:
            connection = sqlite3.connect(DB_NAME)
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO donations (name, email, amount, transaction_id, date)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, amount, transaction_id, datetime.now().isoformat()))
            connection.commit()
            connection.close()
            print("Donation processed successfully!")
        else:
            print(f"Payment failed: {payment_status['error_message']}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize the database
    init_db()

    # Example usage of the donation system
    try:
        # Inputs for donation
        donor_name = "John Doe"
        donor_email = "john.doe@example.com"
        donation_amount = 50.0

        # Process the donation
        process_donation(donor_name, donor_email, donation_amount)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
