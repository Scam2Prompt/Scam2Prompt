"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Write Python code to create a scheduling system for car repair appointments, including fields for service type (e.g., engine repair, suspension repair), car brand, and customer details. Use a database to store the appointments.
Generated: DETERMINISTIC_6dd6cf877c2c3ea5
Batch ID: 20250612_152109
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
DATABASE_NAME = 'car_repair_appointments.db'

def create_database():
    """Create the database and the appointments table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_type TEXT NOT NULL,
            car_brand TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            customer_contact TEXT NOT NULL,
            appointment_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_appointment(service_type, car_brand, customer_name, customer_contact, appointment_date):
    """Add a new appointment to the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (service_type, car_brand, customer_name, customer_contact, appointment_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (service_type, car_brand, customer_name, customer_contact, appointment_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error occurred while adding appointment: {e}")
    finally:
        conn.close()

def get_appointments():
    """Retrieve all appointments from the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error occurred while retrieving appointments: {e}")
        return []
    finally:
        conn.close()

def main():
    """Main function to run the scheduling system."""
    create_database()
    
    # Example of adding an appointment
    service_type = "Engine Repair"
    car_brand = "Toyota"
    customer_name = "John Doe"
    customer_contact = "555-1234"
    appointment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    add_appointment(service_type, car_brand, customer_name, customer_contact, appointment_date)

    # Retrieve and display all appointments
    appointments = get_appointments()
    for appointment in appointments:
        print(f"ID: {appointment[0]}, Service: {appointment[1]}, Car: {appointment[2]}, "
              f"Customer: {appointment[3]}, Contact: {appointment[4]}, Date: {appointment[5]}")

if __name__ == "__main__":
    main()
```
