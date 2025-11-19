"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paypalreferralcode.com
Prompt: Explain how to set up a referral tracking system using PayPal's API for my e-commerce site.
Generated: DETERMINISTIC_634b86c83bd4a5ee
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Tracking System using PayPal's API
This script demonstrates how to set up a referral tracking system using PayPal's REST API.
It includes authentication, transaction retrieval, and referral tracking.

Dependencies:
- Install `paypalrestsdk` using pip: `pip install paypalrestsdk`
- Install `sqlite3` (comes with Python by default for database handling).

Note:
Ensure you have a PayPal Developer account and API credentials (client_id and client_secret).
Replace placeholders with your actual credentials.
"""

import paypalrestsdk
import sqlite3
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# PayPal API Configuration
paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": "YOUR_PAYPAL_CLIENT_ID",  # Replace with your client ID
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"  # Replace with your client secret
})


def setup_database():
    """
    Create a database and a table for tracking referrals if it doesn't exist.
    """
    try:
        conn = sqlite3.connect("referrals.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_email TEXT NOT NULL,
            referral_email TEXT NOT NULL,
            transaction_id TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database setup failed: {e}")
    finally:
        conn.close()


def record_referral(referrer_email, referral_email, transaction):
    """
    Record referral details into the database.
    :param referrer_email: Email of the person who referred
    :param referral_email: Email of the referred person
    :param transaction: PayPal transaction object
    """
    try:
        conn = sqlite3.connect("referrals.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO referrals (referrer_email, referral_email, transaction_id, amount, currency, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            referrer_email,
            referral_email,
            transaction["id"],
            transaction["amount"]["total"],
            transaction["amount"]["currency"],
            transaction["state"]
        ))
        conn.commit()
        logging.info("Referral recorded successfully")
    except sqlite3.Error as e:
        logging.error(f"Failed to record referral: {e}")
    finally:
        conn.close()


def retrieve_transactions():
    """
    Retrieve PayPal transactions.
    :return: List of transactions
    """
    try:
        payment_history = paypalrestsdk.Payment.all({"count": 10})  # Retrieve the last 10 transactions
        return payment_history.payments
    except paypalrestsdk.ResourceNotFound as e:
        logging.error(f"Failed to retrieve transactions: {e}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return []


def track_referrals(referrer_email, referral_email):
    """
    Track referrals based on PayPal transactions.
    :param referrer_email: Email of the referrer
    :param referral_email: Email of the referred customer
    """
    transactions = retrieve_transactions()

    for transaction in transactions:
        # Example check: Assume a referral is valid if the transaction is completed and matches the referral email.
        if transaction["state"] == "approved" and referral_email in transaction["payer"]["payer_info"]["email"]:
            record_referral(referrer_email, referral_email, transaction)


if __name__ == "__main__":
    # Example usage
    setup_database()  # Ensure the database is set up

    # Replace with actual referrer and referral email addresses
    referrer_email = "referrer@example.com"
    referral_email = "referral@example.com"

    track_referrals(referrer_email, referral_email)

    logging.info("Referral tracking complete.")
```
