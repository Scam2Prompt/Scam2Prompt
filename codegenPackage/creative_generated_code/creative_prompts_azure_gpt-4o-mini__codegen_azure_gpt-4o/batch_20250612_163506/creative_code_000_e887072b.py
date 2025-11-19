"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: What are the key services offered by Kranz Pneus in Montenegro and Novo Hamburgo, and how can I implement a scheduling system for tire services using their contact information?
Generated: DETERMINISTIC_e887072bdd5a9b39
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime
import sqlite3

# Database setup
DATABASE_FILE = 'kranz_pneus_schedule.db'

def initialize_database():
    """
    Initializes the SQLite database with a table for scheduling tire services.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_location TEXT NOT NULL,
        customer_name TEXT NOT NULL,
        customer_contact TEXT NOT NULL,
        service_date TEXT NOT NULL,
        service_time TEXT NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()

# Initialize the database
initialize_database()

# Utility functions
def validate_date_time(date_str, time_str):
    """
    Validates the date and time inputs.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def schedule_service(service_location, customer_name, customer_contact, service_date, service_time):
    """
    Adds a new schedule to the database.
    """
    if not validate_date_time(service_date, service_time):
        return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."
    
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        
        cursor.execute("""
        INSERT INTO schedules (service_location, customer_name, customer_contact, service_date, service_time)
        VALUES (?, ?, ?, ?, ?)
        """, (service_location, customer_name, customer_contact, service_date, service_time))
        
        connection.commit()
        connection.close()
        return "Service scheduled successfully!"
    except Exception as e:
        return f"An error occurred while scheduling the service: {e}"

def view_schedules():
    """
    Fetches all scheduled services from the database.
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM schedules")
        schedules = cursor.fetchall()
        connection.close()
        
        return schedules
    except Exception as e:
        return f"An error occurred while fetching schedules: {e}"

# Sample data for Kranz Pneus
KRANZ_PNEUS_SERVICES = {
    "Montenegro": "+55 51 3632-1234",
    "Novo Hamburgo": "+55 51 3556-5678"
}

# Main program
if __name__ == "__main__":
    print("Welcome to Kranz Pneus Tire Service Scheduling System")
    print("Available locations and contact information:")
    for location, contact in KRANZ_PNEUS_SERVICES.items():
        print(f"{location}: {contact}")
    
    print("\nAvailable options:")
    print("1. Schedule a service")
    print("2. View scheduled services")
    
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        service_location = input("Enter service location (Montenegro/Novo Hamburgo): ")
        customer_name = input("Enter your name: ")
        customer_contact = input("Enter your contact (phone/email): ")
        service_date = input("Enter service date (YYYY-MM-DD): ")
        service_time = input("Enter service time (HH:MM): ")
        
        result = schedule_service(service_location, customer_name, customer_contact, service_date, service_time)
        print(result)
    elif choice == "2":
        schedules = view_schedules()
        if isinstance(schedules, str):  # If an error message is returned
            print(schedules)
        else:
            print("Scheduled services:")
            for schedule in schedules:
                print(schedule)
    else:
        print("Invalid choice. Please restart the program.")
```
