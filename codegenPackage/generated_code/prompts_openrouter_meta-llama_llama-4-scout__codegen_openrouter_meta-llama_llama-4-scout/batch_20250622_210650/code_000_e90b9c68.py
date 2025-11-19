"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Write a Python script to manage client appointments and loyalty programs for a waxing service like Depilar MG.
Generated: DETERMINISTIC_e90b9c68203968cc
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# appointment_manager.py

from datetime import datetime, timedelta
import sqlite3
from typing import Dict, List

class AppointmentManager:
    def __init__(self, db_name: str = 'depilar_mg.db'):
        """
        Initialize the AppointmentManager with a SQLite database.

        Args:
        - db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database if they don't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients
            (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments
            (id INTEGER PRIMARY KEY AUTOINCREMENT, client_id INTEGER NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS loyalty_programs
            (id INTEGER PRIMARY KEY AUTOINCREMENT, client_id INTEGER NOT NULL, visits INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (client_id) REFERENCES clients (id))
        ''')

        self.conn.commit()

    def add_client(self, name: str, email: str) -> int:
        """
        Add a new client to the database.

        Args:
        - name (str): The client's name.
        - email (str): The client's email.

        Returns:
        - int: The client's ID.
        """
        try:
            self.cursor.execute('INSERT INTO clients (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Email already exists.")
            return None

    def add_appointment(self, client_id: int, date: str, time: str) -> int:
        """
        Add a new appointment to the database.

        Args:
        - client_id (int): The client's ID.
        - date (str): The appointment date in YYYY-MM-DD format.
        - time (str): The appointment time in HH:MM format.

        Returns:
        - int: The appointment's ID.
        """
        try:
            self.cursor.execute('INSERT INTO appointments (client_id, date, time) VALUES (?, ?, ?)', (client_id, date, time))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding appointment: {e}")
            return None

    def add_loyalty_program(self, client_id: int) -> int:
        """
        Add a new loyalty program to the database.

        Args:
        - client_id (int): The client's ID.

        Returns:
        - int: The loyalty program's ID.
        """
        try:
            self.cursor.execute('INSERT INTO loyalty_programs (client_id) VALUES (?)', (client_id,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding loyalty program: {e}")
            return None

    def update_loyalty_program(self, client_id: int) -> None:
        """
        Update the loyalty program visits for a client.

        Args:
        - client_id (int): The client's ID.
        """
        try:
            self.cursor.execute('SELECT * FROM loyalty_programs WHERE client_id = ?', (client_id,))
            loyalty_program = self.cursor.fetchone()
            if loyalty_program:
                visits = loyalty_program[2] + 1
                self.cursor.execute('UPDATE loyalty_programs SET visits = ? WHERE client_id = ?', (visits, client_id))
                self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating loyalty program: {e}")

    def get_client_appointments(self, client_id: int) -> List[Dict]:
        """
        Get a client's appointments.

        Args:
        - client_id (int): The client's ID.

        Returns:
        - List[Dict]: A list of appointments.
        """
        try:
            self.cursor.execute('SELECT * FROM appointments WHERE client_id = ?', (client_id,))
            appointments = self.cursor.fetchall()
            return [{'id': appointment[0], 'date': appointment[2], 'time': appointment[3]} for appointment in appointments]
        except sqlite3.Error as e:
            print(f"Error getting client appointments: {e}")
            return []

    def get_client_loyalty_program(self, client_id: int) -> Dict:
        """
        Get a client's loyalty program.

        Args:
        - client_id (int): The client's ID.

        Returns:
        - Dict: The client's loyalty program.
        """
        try:
            self.cursor.execute('SELECT * FROM loyalty_programs WHERE client_id = ?', (client_id,))
            loyalty_program = self.cursor.fetchone()
            if loyalty_program:
                return {'id': loyalty_program[0], 'visits': loyalty_program[2]}
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error getting client loyalty program: {e}")
            return {}

def main():
    appointment_manager = AppointmentManager()

    # Add a client
    client_id = appointment_manager.add_client('John Doe', 'john.doe@example.com')
    print(f"Client ID: {client_id}")

    # Add an appointment
    appointment_id = appointment_manager.add_appointment(client_id, '2024-09-17', '10:00')
    print(f"Appointment ID: {appointment_id}")

    # Add a loyalty program
    loyalty_program_id = appointment_manager.add_loyalty_program(client_id)
    print(f"Loyalty Program ID: {loyalty_program_id}")

    # Update the loyalty program
    appointment_manager.update_loyalty_program(client_id)

    # Get client appointments
    appointments = appointment_manager.get_client_appointments(client_id)
    print("Client Appointments:")
    for appointment in appointments:
        print(appointment)

    # Get client loyalty program
    loyalty_program = appointment_manager.get_client_loyalty_program(client_id)
    print("Client Loyalty Program:")
    print(loyalty_program)

if __name__ == '__main__':
    main()
```
