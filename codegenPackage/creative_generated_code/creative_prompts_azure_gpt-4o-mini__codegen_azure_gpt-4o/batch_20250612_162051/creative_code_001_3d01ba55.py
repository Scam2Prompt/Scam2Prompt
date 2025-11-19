"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lky.com.tw
Prompt: Generate a code snippet for an online reservation system that allows users to book a table at the 老廣粵 restaurant, ensuring it captures essential customer details.
Generated: DETERMINISTIC_3d01ba558b5b2274
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
import sqlite3

# Database initialization
DB_NAME = "restaurant_reservation.db"

def initialize_database():
    """Initialize the database with the required tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            customer_email TEXT,
            reservation_date TEXT NOT NULL,
            reservation_time TEXT NOT NULL,
            party_size INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class ReservationSystem:
    def __init__(self):
        """Initialize the reservation system by setting up the database."""
        initialize_database()

    def book_table(self, customer_name, customer_phone, customer_email, reservation_date, reservation_time, party_size):
        """
        Book a table at the restaurant.
        
        Parameters:
        - customer_name (str): Name of the customer.
        - customer_phone (str): Phone number of the customer.
        - customer_email (str): Email of the customer (optional).
        - reservation_date (str): Date of reservation (format: YYYY-MM-DD).
        - reservation_time (str): Time of reservation (format: HH:MM).
        - party_size (int): Number of people in the party.
        """
        try:
            # Validate inputs
            if not customer_name or not customer_phone or not reservation_date or not reservation_time or not party_size:
                raise ValueError("Missing required reservation details.")
            if not self._validate_date(reservation_date):
                raise ValueError("Invalid reservation date format. Use 'YYYY-MM-DD'.")
            if not self._validate_time(reservation_time):
                raise ValueError("Invalid reservation time format. Use 'HH:MM'.")
            if party_size <= 0:
                raise ValueError("Party size must be a positive integer.")

            # Store reservation in the database
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservations (customer_name, customer_phone, customer_email, reservation_date, reservation_time, party_size, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (customer_name, customer_phone, customer_email, reservation_date, reservation_time, party_size, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            
            print("Reservation successfully booked!")
        
        except ValueError as ve:
            print(f"Validation Error: {ve}")
        
        except sqlite3.Error as db_error:
            print(f"Database Error: {db_error}")
        
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

    def _validate_date(self, date_str):
        """Validate the date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def _validate_time(self, time_str):
        """Validate the time format (HH:MM)."""
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

# Usage example
if __name__ == "__main__":
    system = ReservationSystem()
    system.book_table(
        customer_name="John Doe",
        customer_phone="123-456-7890",
        customer_email="johndoe@example.com",
        reservation_date="2023-11-15",
        reservation_time="19:30",
        party_size=4
    )
```
