"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Generate a Python script that utilizes a library for managing patient information related to cosmetic and reconstructive surgery, similar to the practices of Dr. Gareth September.
Generated: DETERMINISTIC_8354f061278afc20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Patient Management System for Cosmetic and Reconstructive Surgery
This script provides functionality to manage patient information, including adding, updating, retrieving, and deleting patient records.
It uses SQLite for database management and follows best practices for error handling and code organization.
"""

import sqlite3
from sqlite3 import Error

# Database file name
DATABASE_FILE = "patients.db"

class PatientDatabase:
    """
    A class to manage patient information using SQLite.
    """

    def __init__(self, db_file):
        """
        Initialize the database connection.
        :param db_file: Path to the SQLite database file.
        """
        self.db_file = db_file
        self.connection = None
        self._connect_to_database()

    def _connect_to_database(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_file)
            self._create_table()
        except Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _create_table(self):
        """
        Create the patients table if it does not exist.
        """
        try:
            query = """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                procedure TEXT NOT NULL,
                contact_info TEXT NOT NULL
            );
            """
            self.connection.execute(query)
        except Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_patient(self, name, age, gender, procedure, contact_info):
        """
        Add a new patient record to the database.
        :param name: Patient's name.
        :param age: Patient's age.
        :param gender: Patient's gender.
        :param procedure: Procedure the patient is undergoing.
        :param contact_info: Patient's contact information.
        """
        try:
            query = """
            INSERT INTO patients (name, age, gender, procedure, contact_info)
            VALUES (?, ?, ?, ?, ?);
            """
            self.connection.execute(query, (name, age, gender, procedure, contact_info))
            self.connection.commit()
            print("Patient added successfully.")
        except Error as e:
            print(f"Error adding patient: {e}")
            raise

    def update_patient(self, patient_id, name=None, age=None, gender=None, procedure=None, contact_info=None):
        """
        Update an existing patient record in the database.
        :param patient_id: ID of the patient to update.
        :param name: Updated name (optional).
        :param age: Updated age (optional).
        :param gender: Updated gender (optional).
        :param procedure: Updated procedure (optional).
        :param contact_info: Updated contact information (optional).
        """
        try:
            query = "UPDATE patients SET "
            updates = []
            params = []

            if name:
                updates.append("name = ?")
                params.append(name)
            if age:
                updates.append("age = ?")
                params.append(age)
            if gender:
                updates.append("gender = ?")
                params.append(gender)
            if procedure:
                updates.append("procedure = ?")
                params.append(procedure)
            if contact_info:
                updates.append("contact_info = ?")
                params.append(contact_info)

            query += ", ".join(updates) + " WHERE id = ?;"
            params.append(patient_id)

            self.connection.execute(query, tuple(params))
            self.connection.commit()
            print("Patient updated successfully.")
        except Error as e:
            print(f"Error updating patient: {e}")
            raise

    def get_patient(self, patient_id):
        """
        Retrieve a patient record by ID.
        :param patient_id: ID of the patient to retrieve.
        :return: Patient record as a dictionary.
        """
        try:
            query = "SELECT * FROM patients WHERE id = ?;"
            cursor = self.connection.execute(query, (patient_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "age": row[2],
                    "gender": row[3],
                    "procedure": row[4],
                    "contact_info": row[5]
                }
            else:
                print("Patient not found.")
                return None
        except Error as e:
            print(f"Error retrieving patient: {e}")
            raise

    def delete_patient(self, patient_id):
        """
        Delete a patient record by ID.
        :param patient_id: ID of the patient to delete.
        """
        try:
            query = "DELETE FROM patients WHERE id = ?;"
            self.connection.execute(query, (patient_id,))
            self.connection.commit()
            print("Patient deleted successfully.")
        except Error as e:
            print(f"Error deleting patient: {e}")
            raise

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = PatientDatabase(DATABASE_FILE)

    # Add a new patient
    db.add_patient("John Doe", 35, "Male", "Rhinoplasty", "john.doe@example.com")

    # Retrieve a patient record
    patient = db.get_patient(1)
    if patient:
        print("Retrieved Patient:", patient)

    # Update a patient record
    db.update_patient(1, age=36, procedure="Facelift")

    # Delete a patient record
    db.delete_patient(1)

    # Close the database connection
    db.close_connection()
```
