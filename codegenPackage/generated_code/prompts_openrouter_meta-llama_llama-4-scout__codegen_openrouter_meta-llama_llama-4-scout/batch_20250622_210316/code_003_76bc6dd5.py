"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Design a simple database schema for storing patient records, appointments, and treatment plans, inspired by the digital chart features of Luxteb.
Generated: DETERMINISTIC_76bc6dd5191290d1
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for patient records
CREATE DATABASE IF NOT EXISTS patient_records;

-- Use the patient_records database
USE patient_records;

-- Create a table for patients
CREATE TABLE IF NOT EXISTS patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id)
);

-- Create a table for doctors
CREATE TABLE IF NOT EXISTS doctors (
  doctor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  specialty VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (doctor_id)
);

-- Create a table for appointments
CREATE TABLE IF NOT EXISTS appointments (
  appointment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for treatment plans
CREATE TABLE IF NOT EXISTS treatment_plans (
  treatment_plan_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (treatment_plan_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for medications
CREATE TABLE IF NOT EXISTS medications (
  medication_id INT AUTO_INCREMENT,
  treatment_plan_id INT NOT NULL,
  medication_name VARCHAR(255) NOT NULL,
  dosage VARCHAR(100) NOT NULL,
  frequency VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (medication_id),
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE
);

-- Create a table for lab tests
CREATE TABLE IF NOT EXISTS lab_tests (
  lab_test_id INT AUTO_INCREMENT,
  treatment_plan_id INT NOT NULL,
  test_name VARCHAR(255) NOT NULL,
  test_date DATE NOT NULL,
  results TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (lab_test_id),
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE
);
```

```python
# patient_records.py

import mysql.connector
from mysql.connector import Error

class PatientRecords:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connection to MySQL DB successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as err:
            print(f"Error: '{err}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

# Example usage
if __name__ == "__main__":
    patient_records = PatientRecords("localhost", "patient_records", "root", "password")
    patient_records.create_connection()

    # Create tables
    with open("schema.sql", "r") as file:
        queries = file.read().split(";")
        for query in queries:
            if query.strip():
                patient_records.execute_query(query)

    # Insert a patient
    query = "INSERT INTO patients (first_name, last_name, date_of_birth, email) VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com')"
    patient_records.execute_query(query)

    # Read patients
    query = "SELECT * FROM patients"
    patients = patient_records.read_query(query)
    for patient in patients:
        print(patient)

    patient_records.connection.close()
```
