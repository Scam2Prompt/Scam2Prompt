"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Design a simple database schema to store patient data, treatment plans, and outcomes for obesity and metabolic surgery patients at Dr. Utku Tantoğlu's clinic.
Generated: DETERMINISTIC_825fcd4b5b1e9a08
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Dr. Utku Tantoğlu's clinic
CREATE DATABASE obesity_clinic;

-- Use the obesity_clinic database
USE obesity_clinic;

-- Create a table to store patient data
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

-- Create a table to store treatment plans
CREATE TABLE treatment_plans (
    treatment_plan_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    plan_name VARCHAR(255) NOT NULL,
    plan_description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (treatment_plan_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table to store medications
CREATE TABLE medications (
    medication_id INT AUTO_INCREMENT,
    medication_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(255) NOT NULL,
    frequency VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (medication_id)
);

-- Create a table to store treatment plan medications
CREATE TABLE treatment_plan_medications (
    treatment_plan_id INT NOT NULL,
    medication_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (treatment_plan_id, medication_id),
    FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
);

-- Create a table to store surgical procedures
CREATE TABLE surgical_procedures (
    surgical_procedure_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    procedure_name VARCHAR(255) NOT NULL,
    procedure_date DATE NOT NULL,
    procedure_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (surgical_procedure_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table to store patient outcomes
CREATE TABLE patient_outcomes (
    patient_outcome_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    outcome_date DATE NOT NULL,
    weight DECIMAL(10, 2) NOT NULL,
    blood_pressure DECIMAL(10, 2) NOT NULL,
    blood_glucose DECIMAL(10, 2) NOT NULL,
    outcome_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (patient_outcome_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table to store follow-up appointments
CREATE TABLE follow_up_appointments (
    follow_up_appointment_id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    appointment_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (follow_up_appointment_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);
```

```python
import mysql.connector
from mysql.connector import Error

class ObesityClinicDatabase:
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
            print("Connection to Obesity Clinic database was successful")
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
    db = ObesityClinicDatabase("localhost", "obesity_clinic", "root", "password")
    db.create_connection()

    # Create tables
    create_patient_table_query = """
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
    """
    db.execute_query(create_patient_table_query)

    # Insert patient data
    insert_patient_query = """
        INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
        VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');
    """
    db.execute_query(insert_patient_query)

    # Read patient data
    read_patient_query = "SELECT * FROM patients;"
    patients = db.read_query(read_patient_query)
    for patient in patients:
        print(patient)

    db.connection.close()
```
