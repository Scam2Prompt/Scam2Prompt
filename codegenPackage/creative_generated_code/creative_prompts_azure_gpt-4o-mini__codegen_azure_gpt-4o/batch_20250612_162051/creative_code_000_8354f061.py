"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Generate a Python script that utilizes a library for managing patient information related to cosmetic and reconstructive surgery, similar to the practices of Dr. Gareth September.
Generated: DETERMINISTIC_8354f061278afc20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Patient Information Management System for Cosmetic and Reconstructive Surgery

This script provides a management system for patient information, including 
their personal details and medical history. It leverages SQLite for data storage 
and is designed to be extensible for larger applications.

Author: [Your Name]
Date: [Date]
"""

import sqlite3
from datetime import datetime

# Database file name
DB_FILE = "patients.db"

# Initialize the database connection and create required tables
def initialize_database():
    """
    Initializes the SQLite database and sets up the necessary tables.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the patient table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT,
            medical_history TEXT,
            created_at TEXT NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

# Add new patient to the database
def add_patient(first_name, last_name, date_of_birth, phone_number, email=None, medical_history=None):
    """
    Adds a new patient record to the database.

    Args:
        first_name (str): The first name of the patient.
        last_name (str): The last name of the patient.
        date_of_birth (str): The patient's date of birth (format: YYYY-MM-DD).
        phone_number (str): The patient's phone number.
        email (str, optional): The patient's email address.
        medical_history (str, optional): Notes on the patient's medical history.

    Returns:
        bool: True if patient is added successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Insert the patient record
        cursor.execute("""
        INSERT INTO patients (first_name, last_name, date_of_birth, phone_number, email, medical_history, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, date_of_birth, phone_number, email, medical_history, datetime.now().isoformat()))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error adding patient: {e}")
        return False
    finally:
        conn.close()

# Retrieve all patients from the database
def get_all_patients():
    """
    Retrieves all patient records from the database.

    Returns:
        list[dict]: A list of dictionaries containing patient information.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Query all patient records
        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()

        # Map rows to dictionaries
        patients = [
            {
                "patient_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "date_of_birth": row[3],
                "phone_number": row[4],
                "email": row[5],
                "medical_history": row[6],
                "created_at": row[7],
            }
            for row in rows
        ]

        return patients
    except sqlite3.Error as e:
        print(f"Error retrieving patients: {e}")
        return []
    finally:
        conn.close()

# Main function to demonstrate functionality
if __name__ == "__main__":
    initialize_database()

    print("Adding a new patient...")
    success = add_patient(
        first_name="Jane",
        last_name="Doe",
        date_of_birth="1985-07-15",
        phone_number="123-456-7890",
        email="jane.doe@example.com",
        medical_history="No known allergies."
    )

    if success:
        print("Patient added successfully!")

    print("\nRetrieving all patients...")
    patients = get_all_patients()
    for patient in patients:
        print(patient)
```
