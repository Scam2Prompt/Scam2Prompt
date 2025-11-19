"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Generate a code snippet to create a reservation system for a restaurant that includes wine pairing options, similar to the offerings at Bodega Jean Bousquet.
Generated: DETERMINISTIC_abdd120c84a27a32
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
import sqlite3


# Database setup: Create tables if they don't exist
def setup_database():
    try:
        connection = sqlite3.connect("restaurant_reservation.db")
        cursor = connection.cursor()

        # Create the reservations table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                reservation_date TEXT NOT NULL,
                number_of_guests INTEGER NOT NULL,
                wine_pairing TEXT NOT NULL
            )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error setting up the database: {e}")
    finally:
        connection.close()


# Function to create a reservation
def create_reservation(name, contact, reservation_date, number_of_guests, wine_pairing):
    try:
        # Validate inputs
        if not name or not contact or not reservation_date or not wine_pairing:
            raise ValueError("All fields are required.")
        
        if number_of_guests <= 0:
            raise ValueError("Number of guests must be greater than zero.")
        
        # Parse and validate reservation date
        parsed_date = datetime.strptime(reservation_date, "%Y-%m-%d %H:%M")
        current_time = datetime.now()

        if parsed_date < current_time:
            raise ValueError("Reservation date must be in the future.")

        # Insert reservation into the database
        connection = sqlite3.connect("restaurant_reservation.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO reservations (name, contact, reservation_date, number_of_guests, wine_pairing)
            VALUES (?, ?, ?, ?, ?)
        """, (name, contact, reservation_date, number_of_guests, wine_pairing))

        connection.commit()
        print("Reservation created successfully!")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    finally:
        connection.close()


# Function to view all reservations
def view_reservations():
    try:
        connection = sqlite3.connect("restaurant_reservation.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()

        if reservations:
            for reservation in reservations:
                print(f"ID: {reservation[0]}, Name: {reservation[1]}, Contact: {reservation[2]}, "
                      f"Date: {reservation[3]}, Guests: {reservation[4]}, Wine Pairing: {reservation[5]}")
        else:
            print("No reservations found.")
    except sqlite3.Error as e:
        print(f"Error retrieving reservations: {e}")
    finally:
        connection.close()


# Main function to demonstrate functionality
def main():
    setup_database()

    print("Welcome to the Restaurant Reservation System!")

    while True:
        print("\nOptions:")
        print("1. Create a Reservation")
        print("2. View Reservations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Gather reservation details
            name = input("Enter your name: ")
            contact = input("Enter your contact information: ")
            reservation_date = input("Enter reservation date (YYYY-MM-DD HH:MM): ")
            number_of_guests = int(input("Enter number of guests: "))
            wine_pairing = input("Enter wine pairing option (e.g., Red, White, None): ")

            create_reservation(name, contact, reservation_date, number_of_guests, wine_pairing)

        elif choice == "2":
            view_reservations()

        elif choice == "3":
            print("Thank you for using the Restaurant Reservation System!")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point for script execution
if __name__ == "__main__":
    main()
```
