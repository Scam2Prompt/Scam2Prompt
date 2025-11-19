"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Write Python code to implement a teleconsultation scheduling system for a speech-language pathology clinic, incorporating features like user authentication and appointment management, inspired by the services offered by Open Minds Instituto.
Generated: DETERMINISTIC_ecd53d3c428f9cea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import getpass
import hashlib
import sqlite3

class TeleconsultationSystem:
    def __init__(self, db_name):
        # Initialize the database connection
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create tables for users and appointments
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments
            (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL, 
            description TEXT, FOREIGN KEY (user_id) REFERENCES users (id))
        ''')

        self.conn.commit()

    def register_user(self, username, password, role):
        # Register a new user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                            (username, hashed_password, role))
        self.conn.commit()

    def login_user(self, username, password):
        # Login an existing user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                            (username, hashed_password))
        user = self.cursor.fetchone()
        return user

    def schedule_appointment(self, user_id, date, time, description):
        # Schedule a new appointment
        self.cursor.execute('INSERT INTO appointments (user_id, date, time, description) VALUES (?, ?, ?, ?)', 
                            (user_id, date, time, description))
        self.conn.commit()

    def get_appointments(self, user_id):
        # Get all appointments for a user
        self.cursor.execute('SELECT * FROM appointments WHERE user_id = ?', (user_id,))
        appointments = self.cursor.fetchall()
        return appointments

    def close_connection(self):
        # Close the database connection
        self.conn.close()


def main():
    system = TeleconsultationSystem('teleconsultation.db')

    while True:
        print("1. Register User")
        print("2. Login User")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            role = input("Enter role (patient/therapist): ")
            system.register_user(username, password, role)
            print("User registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = system.login_user(username, password)
            if user:
                print("Login successful!")
                user_id = user[0]
                while True:
                    print("1. Schedule Appointment")
                    print("2. View Appointments")
                    print("3. Logout")

                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        date = input("Enter date (YYYY-MM-DD): ")
                        time = input("Enter time (HH:MM): ")
                        description = input("Enter description: ")
                        system.schedule_appointment(user_id, date, time, description)
                        print("Appointment scheduled successfully!")

                    elif user_choice == "2":
                        appointments = system.get_appointments(user_id)
                        for appointment in appointments:
                            print(f"Appointment ID: {appointment[0]}")
                            print(f"Date: {appointment[2]}")
                            print(f"Time: {appointment[3]}")
                            print(f"Description: {appointment[4]}")
                            print("------------------------")

                    elif user_choice == "3":
                        break

                    else:
                        print("Invalid option. Please choose again.")

            else:
                print("Invalid username or password.")

        elif choice == "3":
            print("Please login first.")

        elif choice == "4":
            print("Please login first.")

        elif choice == "5":
            system.close_connection()
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
```
