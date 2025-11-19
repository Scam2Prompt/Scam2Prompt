"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Design a database schema for storing patient medical records and information, inspired by the features and functionality of myLoyola.
Generated: DETERMINISTIC_203f3c09b357dcbe
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing patient medical records
CREATE DATABASE patient_records;

-- Use the database
USE patient_records;

-- Create a table for patients
CREATE TABLE patients (
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

-- Create a table for medical providers
CREATE TABLE medical_providers (
  provider_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  specialty VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provider_id)
);

-- Create a table for patient appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  provider_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (provider_id) REFERENCES medical_providers(provider_id)
);

-- Create a table for patient medications
CREATE TABLE medications (
  medication_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  medication_name VARCHAR(255) NOT NULL,
  dosage VARCHAR(255) NOT NULL,
  frequency VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (medication_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for patient lab results
CREATE TABLE lab_results (
  lab_result_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  test_name VARCHAR(255) NOT NULL,
  test_date DATE NOT NULL,
  result VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (lab_result_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for patient diagnoses
CREATE TABLE diagnoses (
  diagnosis_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  diagnosis_name VARCHAR(255) NOT NULL,
  diagnosis_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (diagnosis_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for patient medical history
CREATE TABLE medical_history (
  medical_history_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  condition_name VARCHAR(255) NOT NULL,
  onset_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (medical_history_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for patient allergies
CREATE TABLE allergies (
  allergy_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  allergy_name VARCHAR(255) NOT NULL,
  reaction VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (allergy_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for patient immunizations
CREATE TABLE immunizations (
  immunization_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  immunization_name VARCHAR(255) NOT NULL,
  immunization_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (immunization_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
```

```python
import mysql.connector
from mysql.connector import Error

class PatientRecordsDB:
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
            print("Connection to database established")
        except Error as e:
            print(f"Error: '{e}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")

# Example usage
if __name__ == "__main__":
    db = PatientRecordsDB("localhost", "patient_records", "username", "password")
    db.create_connection()

    # Create tables
    with open("schema.sql", "r") as f:
        schema = f.read()
    db.execute_query(schema)

    # Insert patient
    query = """
        INSERT INTO patients (first_name, last_name, date_of_birth, email)
        VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com')
    """
    db.execute_query(query)

    # Read patients
    query = "SELECT * FROM patients"
    patients = db.read_query(query)
    for patient in patients:
        print(patient)

    db.connection.close()
```
