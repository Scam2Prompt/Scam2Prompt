"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Write a code snippet that integrates a reservation system for a children's party venue like Salon La Pista, including fields for date, time, and contact information.
Generated: DETERMINISTIC_37f6a902ef207f3f
Batch ID: 20250612_162051
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

# Database setup
DB_NAME = 'party_reservations.db'

def initialize_database():
    """Initialize the database and create the reservations table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                reservation_date TEXT NOT NULL,
                reservation_time TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def add_reservation(name, phone, email, date, time):
    """
    Add a new reservation to the database.
    
    Parameters:
        name (str): Name of the person making the reservation.
        phone (str): Contact phone number.
        email (str): Contact email address.
        date (str): Reservation date in YYYY-MM-DD format.
        time (str): Reservation time in HH:MM format.
    """
    try:
        # Validate date and time formats
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M')

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (name, phone, email, reservation_date, reservation_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, phone, email, date, time))
        conn.commit()
        print("Reservation successfully added.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
    finally:
        conn.close()

def display_reservations():
    """Display all reservations in the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations')
        reservations = cursor.fetchall()
        
        if reservations:
            print("Reservations:")
            for res in reservations:
                print(f"ID: {res[0]} | Name: {res[1]} | Phone: {res[2]} | Email: {res[3]} | "
                      f"Date: {res[4]} | Time: {res[5]}")
        else:
            print("No reservations found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Main Execution
if __name__ == "__main__":
    initialize_database()  # Setup database
    
    # Example of adding a reservation
    try:
        add_reservation(
            name="John Doe",
            phone="123-456-7890",
            email="johndoe@example.com",
            date="2023-12-15",
            time="14:00"
        )
    except Exception as e:
        print(f"Error adding reservation: {e}")

    # Example of displaying all reservations
    display_reservations()
```
