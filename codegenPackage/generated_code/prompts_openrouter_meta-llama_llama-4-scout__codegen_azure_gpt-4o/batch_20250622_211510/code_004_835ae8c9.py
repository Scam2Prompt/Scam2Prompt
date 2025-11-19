"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Design a system for managing patient records at Amar Hospital, including features like electronic health records, patient registration, and secure data storage.
Generated: DETERMINISTIC_835ae8c99a07709e
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_management_system.py

import sqlite3
import hashlib
import os
from datetime import datetime

# Constants for database and security
DATABASE_FILE = "amar_hospital.db"
SALT = os.urandom(16)  # Random salt for hashing passwords

# Utility function to hash sensitive data (e.g., passwords)
def hash_data(data: str) -> str:
    return hashlib.sha256(SALT + data.encode('utf-8')).hexdigest()

# Initialize the database
def initialize_database():
    """Creates the necessary tables for the patient management system."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Create patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            medical_history TEXT,
            created_at TEXT NOT NULL
        )
    ''')

    # Create users table for secure access (e.g., admin, doctors)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'doctor', 'nurse')),
            created_at TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Register a new patient
def register_patient(first_name: str, last_name: str, date_of_birth: str, contact_number: str, email: str, address: str, medical_history: str = None):
    """Registers a new patient in the system."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Insert patient record
        cursor.execute('''
            INSERT INTO patients (first_name, last_name, date_of_birth, contact_number, email, address, medical_history, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, date_of_birth, contact_number, email, address, medical_history, datetime.now().isoformat()))

        connection.commit()
        print("Patient registered successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. Email must be unique.")
    finally:
        connection.close()

# Retrieve patient records
def get_patient_records():
    """Fetches all patient records from the database."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Fetch all patient records
        cursor.execute('SELECT * FROM patients')
        records = cursor.fetchall()

        return records
    finally:
        connection.close()

# Register a new user (e.g., admin, doctor)
def register_user(username: str, password: str, role: str):
    """Registers a new user for secure access."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Hash the password before storing
        password_hash = hash_data(password)

        # Insert user record
        cursor.execute('''
            INSERT INTO users (username, password_hash, role, created_at)
            VALUES (?, ?, ?, ?)
        ''', (username, password_hash, role, datetime.now().isoformat()))

        connection.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. Username must be unique.")
    finally:
        connection.close()

# Authenticate user
def authenticate_user(username: str, password: str) -> bool:
    """Authenticates a user by verifying their username and password."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Fetch the stored password hash
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()

        if result:
            stored_password_hash = result[0]
            return stored_password_hash == hash_data(password)
        else:
            return False
    finally:
        connection.close()

# Main function for testing
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    # Register a new user
    register_user("admin", "securepassword123", "admin")

    # Authenticate the user
    if authenticate_user("admin", "securepassword123"):
        print("Authentication successful.")
    else:
        print("Authentication failed.")

    # Register a new patient
    register_patient(
        first_name="John",
        last_name="Doe",
        date_of_birth="1980-01-01",
        contact_number="1234567890",
        email="john.doe@example.com",
        address="123 Main St, Springfield",
        medical_history="No known allergies."
    )

    # Fetch and display all patient records
    patients = get_patient_records()
    for patient in patients:
        print(patient)
```
