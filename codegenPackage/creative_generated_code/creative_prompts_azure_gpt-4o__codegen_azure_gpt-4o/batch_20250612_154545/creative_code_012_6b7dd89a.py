"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Develop a program to manage bookings for airbrush nail art courses and master classes offered by AirstyleArt.
Generated: DETERMINISTIC_6b7dd89a625ffe3e
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to manage bookings for airbrush nail art courses and master classes offered by AirstyleArt.
This program allows users to add, view, update, and delete bookings. It uses an SQLite database for persistence.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "airstyleart_bookings.db"


def initialize_database():
    """
    Initializes the database and creates the bookings table if it doesn't exist.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        course_type TEXT NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Confirmed'
    )
    """)

    connection.commit()
    connection.close()


def add_booking(name, email, phone, course_type, date):
    """
    Adds a new booking to the database.
    :param name: Name of the participant.
    :param email: Email address of the participant.
    :param phone: Phone number of the participant.
    :param course_type: Type of course (e.g., "Beginner Airbrush Art", "Master Class").
    :param date: Date of the course in YYYY-MM-DD format.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO bookings (name, email, phone, course_type, date)
        VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, course_type, date))

        connection.commit()
        print("Booking added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding booking: {e}")
    finally:
        connection.close()


def view_bookings():
    """
    Retrieves and displays all bookings from the database.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()

        if bookings:
            print("Current Bookings:")
            for booking in bookings:
                print(f"ID: {booking[0]}, Name: {booking[1]}, Email: {booking[2]}, Phone: {booking[3]}, "
                      f"Course Type: {booking[4]}, Date: {booking[5]}, Status: {booking[6]}")
        else:
            print("No bookings found.")
    except sqlite3.Error as e:
        print(f"Error retrieving bookings: {e}")
    finally:
        connection.close()


def update_booking(booking_id, status):
    """
    Updates the status of an existing booking.
    :param booking_id: ID of the booking to update.
    :param status: New status for the booking (e.g., "Confirmed", "Cancelled").
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE bookings
        SET status = ?
        WHERE id = ?
        """, (status, booking_id))

        if cursor.rowcount > 0:
            print("Booking updated successfully!")
        else:
            print("Booking not found.")
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error updating booking: {e}")
    finally:
        connection.close()


def delete_booking(booking_id):
    """
    Deletes an existing booking.
    :param booking_id: ID of the booking to delete.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM bookings
        WHERE id = ?
        """, (booking_id,))

        if cursor.rowcount > 0:
            print("Booking deleted successfully!")
        else:
            print("Booking not found.")
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error deleting booking: {e}")
    finally:
        connection.close()


def main():
    """
    Main function to interact with the booking system.
    """
    initialize_database()

    while True:
        print("\nAirstyleArt Booking System")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Update Booking")
        print("4. Delete Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter participant's name: ")
            email = input("Enter participant's email: ")
            phone = input("Enter participant's phone (optional): ")
            course_type = input("Enter course type (e.g., Beginner Airbrush Art, Master Class): ")
            date = input("Enter course date (YYYY-MM-DD): ")

            try:
                # Validate date format
                datetime.strptime(date, "%Y-%m-%d")
                add_booking(name, email, phone, course_type, date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "2":
            view_bookings()

        elif choice == "3":
            booking_id = input("Enter booking ID to update: ")
            status = input("Enter new status (e.g., Confirmed, Cancelled): ")
            update_booking(booking_id, status)

        elif choice == "4":
            booking_id = input("Enter booking ID to delete: ")
            delete_booking(booking_id)

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
