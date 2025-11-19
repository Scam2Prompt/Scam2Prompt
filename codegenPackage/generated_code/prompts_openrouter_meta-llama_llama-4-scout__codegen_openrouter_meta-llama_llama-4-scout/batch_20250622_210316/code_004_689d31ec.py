"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: "Design a database schema to store patient information and treatment plans for a dental clinic that practices integrative dentistry, including fields for tracking patient progress and outcomes."
Generated: DETERMINISTIC_689d31ece1d1214b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the dental clinic
CREATE DATABASE integrative_dental_clinic;

-- Use the database
USE integrative_dental_clinic;

-- Create a table to store patient information
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
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (treatment_plan_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table to store treatment plan procedures
CREATE TABLE treatment_plan_procedures (
  procedure_id INT AUTO_INCREMENT,
  treatment_plan_id INT NOT NULL,
  procedure_name VARCHAR(255) NOT NULL,
  procedure_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (procedure_id),
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE
);

-- Create a table to store patient progress and outcomes
CREATE TABLE patient_progress (
  progress_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  treatment_plan_id INT,
  progress_date DATE NOT NULL,
  description TEXT,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (progress_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE SET NULL
);

-- Create a table to store dental records
CREATE TABLE dental_records (
  record_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  treatment_plan_id INT,
  record_date DATE NOT NULL,
  dental_status VARCHAR(255) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (record_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE SET NULL
);

-- Create a stored procedure to insert a new patient
DELIMITER //
CREATE PROCEDURE insert_patient(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_date_of_birth DATE,
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_date_of_birth, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create a stored procedure to insert a new treatment plan
DELIMITER //
CREATE PROCEDURE insert_treatment_plan(
  IN p_patient_id INT,
  IN p_plan_name VARCHAR(255),
  IN p_description TEXT,
  IN p_start_date DATE,
  IN p_end_date DATE
)
BEGIN
  INSERT INTO treatment_plans (patient_id, plan_name, description, start_date, end_date)
  VALUES (p_patient_id, p_plan_name, p_description, p_start_date, p_end_date);
END//
DELIMITER ;

-- Example usage:
CALL insert_patient('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');
CALL insert_treatment_plan(1, 'Treatment Plan 1', 'This is a sample treatment plan', '2022-01-01', '2022-12-31');
```

```python
import mysql.connector
from mysql.connector import Error

class DentalClinicDatabase:
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

    def execute_read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")

# Example usage:
db = DentalClinicDatabase('localhost', 'integrative_dental_clinic', 'root', 'password')
db.create_connection()

query = "SELECT * FROM patients"
result = db.execute_read_query(query)
for row in result:
    print(row)
```
