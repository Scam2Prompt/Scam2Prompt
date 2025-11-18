"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Generate code using a database management system to store and retrieve occupational health examination records, including tests like electrocardiograms and radiology results, as outlined on Medicid IPS's services page.
Generated: DETERMINISTIC_ad492c79a2b284b5
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database management system for storing and retrieving occupational health examination records.

# Establish database connection
def connect_to_db(db_name="health_records.db"):
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Create necessary tables
def create_tables(connection):
    try:
        cursor = connection.cursor()
        # Table for storing patient information
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dob DATE NOT NULL,
                gender TEXT NOT NULL,
                contact_info TEXT
            )
        """)
        # Table for storing examination records
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS examinations (
                exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                exam_type TEXT NOT NULL,
                exam_date DATE NOT NULL,
                results TEXT,
                FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
            )
        """)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# Insert patient information
def insert_patient(connection, name, dob, gender, contact_info):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO patients (name, dob, gender, contact_info)
            VALUES (?, ?, ?, ?)
        """, (name, dob, gender, contact_info))
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting patient: {e}")
        return None

# Insert examination record
def insert_examination(connection, patient_id, exam_type, exam_date, results):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO examinations (patient_id, exam_type, exam_date, results)
            VALUES (?, ?, ?, ?)
        """, (patient_id, exam_type, exam_date, results))
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting examination: {e}")
        return None

# Retrieve all records for a specific patient
def get_patient_records(connection, patient_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT e.exam_id, e.exam_type, e.exam_date, e.results
            FROM examinations e
            WHERE e.patient_id = ?
        """, (patient_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving records: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Connect to database
    db_connection = connect_to_db()
    if db_connection is None:
        exit(1)

    # Create tables
    create_tables(db_connection)

    # Add a sample patient
    patient_id = insert_patient(db_connection, "John Doe", "1985-07-12", "Male", "555-1234")
    if patient_id:
        print(f"Inserted patient with ID: {patient_id}")

    # Add sample examination records for the patient
    exam_id1 = insert_examination(db_connection, patient_id, "Electrocardiogram", "2023-10-10", "Normal ECG")
    exam_id2 = insert_examination(db_connection, patient_id, "Radiology", "2023-10-11", "No abnormalities detected")

    if exam_id1 and exam_id2:
        print(f"Inserted examinations with IDs: {exam_id1} and {exam_id2}")

    # Retrieve and display all records for the patient
    records = get_patient_records(db_connection, patient_id)
    if records:
        print("Patient Examination Records:")
        for record in records:
            print(record)

    # Close database connection
    db_connection.close()
```
