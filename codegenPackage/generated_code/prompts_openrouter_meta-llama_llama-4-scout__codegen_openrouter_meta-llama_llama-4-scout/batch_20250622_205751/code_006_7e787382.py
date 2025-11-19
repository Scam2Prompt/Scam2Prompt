"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Design a database schema for storing patient data, treatment plans, and medical records for a cardiology clinic.
Generated: DETERMINISTIC_7e7873822fb2fd0b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the cardiology clinic
CREATE DATABASE cardiology_clinic;

-- Use the cardiology clinic database
USE cardiology_clinic;

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

-- Create a table for doctors
CREATE TABLE doctors (
  doctor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  specialty VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (doctor_id)
);

-- Create a table for treatment plans
CREATE TABLE treatment_plans (
  treatment_plan_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (treatment_plan_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for medications
CREATE TABLE medications (
  medication_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  dosage VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (medication_id)
);

-- Create a table for treatment plan medications
CREATE TABLE treatment_plan_medications (
  treatment_plan_id INT NOT NULL,
  medication_id INT NOT NULL,
  dosage VARCHAR(100) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (treatment_plan_id, medication_id),
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE,
  FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
);

-- Create a table for medical records
CREATE TABLE medical_records (
  medical_record_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  visit_date DATE NOT NULL,
  description TEXT NOT NULL,
  diagnosis VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (medical_record_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for test results
CREATE TABLE test_results (
  test_result_id INT AUTO_INCREMENT,
  medical_record_id INT NOT NULL,
  test_name VARCHAR(255) NOT NULL,
  result VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (test_result_id),
  FOREIGN KEY (medical_record_id) REFERENCES medical_records(medical_record_id) ON DELETE CASCADE
);
```

```sql
-- Example usage:
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO doctors (first_name, last_name, email, phone_number, specialty)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'Cardiology');

INSERT INTO treatment_plans (patient_id, doctor_id, plan_name, description, start_date)
VALUES (1, 1, 'Treatment Plan 1', 'This is a treatment plan', '2022-01-01');

INSERT INTO medications (name, description, dosage)
VALUES ('Aspirin', 'Pain reliever', '81mg');

INSERT INTO treatment_plan_medications (treatment_plan_id, medication_id, dosage, start_date)
VALUES (1, 1, '81mg', '2022-01-01');

INSERT INTO medical_records (patient_id, doctor_id, visit_date, description, diagnosis)
VALUES (1, 1, '2022-01-01', 'Patient visit', 'Hypertension');

INSERT INTO test_results (medical_record_id, test_name, result)
VALUES (1, 'Blood Pressure', '140/90');
```
