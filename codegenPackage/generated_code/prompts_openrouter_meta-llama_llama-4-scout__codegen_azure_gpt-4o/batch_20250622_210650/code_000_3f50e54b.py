"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Generate a Python code snippet for managing polygraph test results, including patient information, test dates, and results, using a SQLite database."
Generated: DETERMINISTIC_3f50e54ba6f36d16
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "polygraph_tests.db"

def initialize_database():
    """
    Initialize the SQLite database and create necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create table for storing patient information
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL
        )
        """)
        
        # Create table for storing polygraph test results
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS polygraph_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            test_date TEXT NOT NULL,
            result TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients (id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_patient(name, age, gender):
    """
    Add a new patient to the database.
    :param name: Name of the patient
    :param age: Age of the patient
    :param gender: Gender of the patient
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO patients (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding patient: {e}")
    finally:
        conn.close()

def add_polygraph_test(patient_id, test_date, result):
    """
    Add a polygraph test result for a specific patient.
    :param patient_id: ID of the patient
    :param test_date: Date of the test (YYYY-MM-DD format)
    :param result: Result of the test (e.g., 'Pass', 'Fail')
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO polygraph_tests (patient_id, test_date, result) VALUES (?, ?, ?)", 
                       (patient_id, test_date, result))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding polygraph test: {e}")
    finally:
        conn.close()

def get_patient_tests(patient_id):
    """
    Retrieve all polygraph test results for a specific patient.
    :param patient_id: ID of the patient
    :return: List of test results
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT test_date, result FROM polygraph_tests WHERE patient_id = ?", (patient_id,))
        tests = cursor.fetchall()
        return tests
    except sqlite3.Error as e:
        print(f"Error retrieving test results: {e}")
        return []
    finally:
        conn.close()

def get_all_patients():
    """
    Retrieve all patients from the database.
    :return: List of patients
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, age, gender FROM patients")
        patients = cursor.fetchall()
        return patients
    except sqlite3.Error as e:
        print(f"Error retrieving patients: {e}")
        return []
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    
    # Add sample patients
    add_patient("John Doe", 30, "Male")
    add_patient("Jane Smith", 25, "Female")
    
    # Add sample polygraph tests
    add_polygraph_test(1, "2023-10-01", "Pass")
    add_polygraph_test(1, "2023-10-15", "Fail")
    add_polygraph_test(2, "2023-10-10", "Pass")
    
    # Retrieve and display all patients
    print("Patients:")
    for patient in get_all_patients():
        print(patient)
    
    # Retrieve and display test results for a specific patient
    print("\nPolygraph Tests for Patient ID 1:")
    for test in get_patient_tests(1):
        print(test)
```
