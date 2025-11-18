"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Recommend a library or API for implementing a dental clinic management system that supports appointment booking, patient record management, and service categorization (e.g., teeth whitening, root canals, Invisalign).
Generated: DETERMINISTIC_3594c32588d7bda3
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dental_clinic_management.py

import sqlite3
from datetime import datetime

class DentalClinicManagement:
    """A class to manage a dental clinic's operations including appointment booking,
    patient record management, and service categorization."""

    def __init__(self, db_name='clinic_management.db'):
        """Initialize the database connection and create necessary tables."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for patients, services, and appointments."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact_info TEXT NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service_name TEXT NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER,
                    service_id INTEGER,
                    appointment_date TEXT,
                    FOREIGN KEY (patient_id) REFERENCES patients (id),
                    FOREIGN KEY (service_id) REFERENCES services (id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            self.connection.rollback()

    def add_patient(self, name, contact_info):
        """Add a new patient to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO patients (name, contact_info) VALUES (?, ?)
            ''', (name, contact_info))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding patient: {e}")
            self.connection.rollback()

    def add_service(self, service_name):
        """Add a new service to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO services (service_name) VALUES (?)
            ''', (service_name,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding service: {e}")
            self.connection.rollback()

    def book_appointment(self, patient_id, service_id, appointment_date):
        """Book an appointment for a patient."""
        try:
            # Ensure the appointment date is in the future
            if datetime.strptime(appointment_date, "%Y-%m-%d %H:%M") <= datetime.now():
                raise ValueError("Appointment date must be in the future.")
                
            self.cursor.execute('''
                INSERT INTO appointments (patient_id, service_id, appointment_date)
                VALUES (?, ?, ?)
            ''', (patient_id, service_id, appointment_date))
            self.connection.commit()
        except (sqlite3.Error, ValueError) as e:
            print(f"Error booking appointment: {e}")
            self.connection.rollback()

    def get_patients(self):
        """Retrieve all patients from the database."""
        try:
            self.cursor.execute('SELECT * FROM patients')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving patients: {e}")
            return []

    def get_services(self):
        """Retrieve all services from the database."""
        try:
            self.cursor.execute('SELECT * FROM services')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving services: {e}")
            return []

    def get_appointments(self):
        """Retrieve all appointments from the database."""
        try:
            self.cursor.execute('SELECT * FROM appointments')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving appointments: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Usage example
if __name__ == "__main__":
    clinic = DentalClinicManagement()
    clinic.add_patient("John Doe", "555-1234")
    clinic.add_service("Teeth Whitening")
    clinic.book_appointment(1, 1, "2023-12-01 10:00")
    
    print("Patients:", clinic.get_patients())
    print("Services:", clinic.get_services())
    print("Appointments:", clinic.get_appointments())
    
    clinic.close()
```
