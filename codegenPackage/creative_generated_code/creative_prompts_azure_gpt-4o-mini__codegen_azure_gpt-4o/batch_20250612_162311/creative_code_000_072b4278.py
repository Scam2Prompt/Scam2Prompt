"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a code snippet for a booking system that allows patients to schedule appointments with a chiropractor or osteopath, similar to the services offered at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_072b4278a4a5457e
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import sqlite3

# Create an SQLite database to store appointments
DATABASE_FILE = "appointments.db"

def initialize_database():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            service TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def book_appointment(patient_name, service, date, time):
    """
    Book an appointment for a patient.
    Args:
        patient_name (str): Name of the patient.
        service (str): Service type, e.g., 'Chiropractor' or 'Osteopath'.
        date (str): Appointment date in the format 'YYYY-MM-DD'.
        time (str): Appointment time in the format 'HH:MM'.
    Returns:
        str: Success message or error message.
    """
    try:
        # Ensure the service is valid
        if service not in ["Chiropractor", "Osteopath"]:
            return "Error: Invalid service type. Choose 'Chiropractor' or 'Osteopath'."

        # Validate date and time format
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            return "Error: Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time."

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Check for conflicts with existing appointments
        cursor.execute("""
            SELECT * FROM appointments 
            WHERE appointment_date = ? AND appointment_time = ?
        """, (date, time))
        conflict = cursor.fetchone()
        if conflict:
            return "Error: Appointment slot is already booked."

        # Insert the new appointment into the database
        cursor.execute("""
            INSERT INTO appointments (patient_name, service, appointment_date, appointment_time)
            VALUES (?, ?, ?, ?)
        """, (patient_name, service, date, time))
        conn.commit()
        conn.close()
        return "Success: Appointment booked successfully!"
    except Exception as e:
        return f"Error: An unexpected error occurred. Details: {str(e)}"

def view_appointments():
    """
    Retrieve a list of all scheduled appointments.
    Returns:
        list: List of appointment records.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments")
        appointments = cursor.fetchall()
        conn.close()
        return appointments
    except Exception as e:
        return f"Error: Unable to retrieve appointments. Details: {str(e)}"

def main():
    """Main function for the booking system."""
    initialize_database()
    print("Welcome to the Booking System!")
    
    while True:
        print("\nOptions:")
        print("1. Book an Appointment")
        print("2. View All Appointments")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            patient_name = input("Enter patient name: ")
            service = input("Enter service ('Chiropractor' or 'Osteopath'): ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            result = book_appointment(patient_name, service, date, time)
            print(result)
        elif choice == "2":
            appointments = view_appointments()
            if isinstance(appointments, str):
                print(appointments)  # Error message
            else:
                print("\nScheduled Appointments:")
                for appt in appointments:
                    print(f"ID: {appt[0]}, Name: {appt[1]}, Service: {appt[2]}, Date: {appt[3]}, Time: {appt[4]}")
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
