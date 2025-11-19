"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and reminders, for a clinic like Studio Dentistico dott.ssa Vira Palazzo in Rome.
Generated: DETERMINISTIC_1656cff4b9bdc04c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import sqlite3
from sqlite3 import Error

class DentalClinic:
    def __init__(self, db_name):
        """
        Initialize a DentalClinic object.

        :param db_name: Name of the SQLite database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            print(f"Connected to SQLite Database {db_name}")
        except Error as e:
            print(e)

        # Create table
        self.create_table()

    def create_table(self):
        """
        Create a table for appointments if it doesn't exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS appointments
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             patient_name TEXT NOT NULL,
             appointment_date DATE NOT NULL,
             appointment_time TIME NOT NULL,
             reminder_sent INTEGER DEFAULT 0)
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)

    def schedule_appointment(self, patient_name, appointment_date, appointment_time):
        """
        Schedule a new appointment.

        :param patient_name: Name of the patient.
        :param appointment_date: Date of the appointment (YYYY-MM-DD).
        :param appointment_time: Time of the appointment (HH:MM).
        """
        query = """
            INSERT INTO appointments (patient_name, appointment_date, appointment_time)
            VALUES (?, ?, ?)
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (patient_name, appointment_date, appointment_time))
            self.conn.commit()
            print("Appointment scheduled successfully.")
        except Error as e:
            print(e)

    def send_reminders(self):
        """
        Send reminders for upcoming appointments.
        """
        query = """
            SELECT patient_name, appointment_date, appointment_time
            FROM appointments
            WHERE reminder_sent = 0 AND appointment_date >= DATE('now')
            ORDER BY appointment_date, appointment_time
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                patient_name, appointment_date, appointment_time = row
                # Here you would implement your actual reminder sending logic (e.g., email, SMS)
                print(f"Sending reminder to {patient_name} for {appointment_date} {appointment_time}")
                self.mark_reminder_sent(patient_name, appointment_date, appointment_time)
        except Error as e:
            print(e)

    def mark_reminder_sent(self, patient_name, appointment_date, appointment_time):
        """
        Mark a reminder as sent.

        :param patient_name: Name of the patient.
        :param appointment_date: Date of the appointment (YYYY-MM-DD).
        :param appointment_time: Time of the appointment (HH:MM).
        """
        query = """
            UPDATE appointments
            SET reminder_sent = 1
            WHERE patient_name = ? AND appointment_date = ? AND appointment_time = ?
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (patient_name, appointment_date, appointment_time))
            self.conn.commit()
        except Error as e:
            print(e)

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            print("SQLite Connection is closed")


def main():
    clinic = DentalClinic("dental_clinic.db")

    while True:
        print("\n1. Schedule Appointment")
        print("2. Send Reminders")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            patient_name = input("Enter patient name: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            appointment_time = input("Enter appointment time (HH:MM): ")
            clinic.schedule_appointment(patient_name, appointment_date, appointment_time)
        elif choice == "2":
            clinic.send_reminders()
        elif choice == "3":
            clinic.close_connection()
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
