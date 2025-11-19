"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Illustrate how to implement a booking system for RIB rentals in Greece, incorporating user authentication and payment processing features.
Generated: DETERMINISTIC_2d69d3d50a1120a4
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

import sqlite3
from datetime import datetime
import hashlib
import stripe

# Database setup
DB_FILE = "rib_rental.db"

# Stripe API key for payment processing
STRIPE_API_KEY = "your_stripe_api_key_here"
stripe.api_key = STRIPE_API_KEY


def create_tables():
    """
    Create the necessary tables for the booking system.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)

    # RIB (Rigid Inflatable Boat) Rentals Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rib_rentals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price_per_day REAL NOT NULL
    )
    """)

    # Bookings Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        rib_id INTEGER NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        payment_status TEXT NOT NULL DEFAULT 'Pending',
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (rib_id) REFERENCES rib_rentals (id)
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    """
    Hash a password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, email, password):
    """
    Register a new user in the system.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        hashed_password = hash_password(password)
        cursor.execute("""
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
        """, (username, email, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def authenticate_user(username, password):
    """
    Authenticate a user based on their username and password.
    Returns True if authentication is successful, else False.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    hashed_password = hash_password(password)
    cursor.execute("""
    SELECT id FROM users WHERE username = ? AND password_hash = ?
    """, (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return user[0]  # Return user ID
    else:
        print("Authentication failed.")
        return None


def list_rib_rentals():
    """
    List all available RIB rentals.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description, price_per_day FROM rib_rentals")
    ribs = cursor.fetchall()
    conn.close()

    print("Available RIB Rentals:")
    for rib in ribs:
        print(f"ID: {rib[0]}, Title: {rib[1]}, Description: {rib[2]}, Price per Day: €{rib[3]}")


def create_booking(user_id, rib_id, start_date, end_date, payment_token):
    """
    Create a booking for a RIB rental.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Process payment using Stripe
        stripe.PaymentIntent.create(
            amount=int(100 * calculate_booking_cost(rib_id, start_date, end_date)),
            currency="eur",
            payment_method=payment_token,
            confirm=True
        )

        # Insert booking into database
        cursor.execute("""
        INSERT INTO bookings (user_id, rib_id, start_date, end_date, payment_status)
        VALUES (?, ?, ?, ?, 'Completed')
        """, (user_id, rib_id, start_date, end_date))
        conn.commit()
        print("Booking created successfully!")
    except stripe.error.StripeError as e:
        print(f"Payment failed: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def calculate_booking_cost(rib_id, start_date, end_date):
    """
    Calculate the total cost of a booking.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT price_per_day FROM rib_rentals WHERE id = ?", (rib_id,))
    rib = cursor.fetchone()
    conn.close()

    if not rib:
        raise ValueError("RIB ID not found.")

    price_per_day = rib[0]
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    num_days = (end_date_obj - start_date_obj).days

    return price_per_day * num_days


# Main application logic
if __name__ == "__main__":
    create_tables()
    print("Database tables initialized.")

    # Uncomment the following lines for testing:

    # Register a user
    # register_user("john_doe", "john@example.com", "securepassword123")

    # Authenticate a user
    # user_id = authenticate_user("john_doe", "securepassword123")
    # if user_id:
    #     print(f"Authenticated User ID: {user_id}")

    # List available RIBs
    # list_rib_rentals()

    # Create a booking (requires valid Stripe payment token)
    # create_booking(user_id, rib_id=1, start_date="2023-10-01", end_date="2023-10-05", payment_token="tok_visa")
```
