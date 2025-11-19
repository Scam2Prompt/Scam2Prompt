"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Design a database schema to store information about independent pharmacies, their owners, and their patients, considering the requirements of a member-owned co-operative structure.
Generated: DETERMINISTIC_682cdcbfa29b502c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for co-operative structure
CREATE DATABASE pharmacy_cooperative;

-- Use the database
USE pharmacy_cooperative;

-- Create table for pharmacy owners
CREATE TABLE owners (
  owner_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (owner_id)
);

-- Create table for pharmacies
CREATE TABLE pharmacies (
  pharmacy_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  owner_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (pharmacy_id),
  FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE SET NULL
);

-- Create table for patients
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  pharmacy_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id),
  FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE SET NULL
);

-- Create table for co-operative membership
CREATE TABLE co-operative_membership (
  membership_id INT AUTO_INCREMENT,
  pharmacy_id INT,
  owner_id INT,
  membership_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (membership_id),
  FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
  FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE,
  UNIQUE KEY (pharmacy_id, owner_id)
);

-- Create table for patient prescriptions
CREATE TABLE prescriptions (
  prescription_id INT AUTO_INCREMENT,
  patient_id INT,
  pharmacy_id INT,
  prescription_date DATE,
  medication_name VARCHAR(255),
  dosage VARCHAR(255),
  refills INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (prescription_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_owners_email ON owners(email);
CREATE INDEX idx_pharmacies_name ON pharmacies(name);
CREATE INDEX idx_patients_email ON patients(email);
CREATE INDEX idx_prescriptions_patient_id ON prescriptions(patient_id);
CREATE INDEX idx_prescriptions_pharmacy_id ON prescriptions(pharmacy_id);
```

```sql
-- sample_data.sql

-- Insert sample data into owners table
INSERT INTO owners (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into pharmacies table
INSERT INTO pharmacies (name, address, phone_number, owner_id)
VALUES
  ('Doe\'s Pharmacy', '123 Main St', '123-456-7890', 1),
  ('Smith\'s Pharmacy', '456 Elm St', '987-654-3210', 2);

-- Insert sample data into patients table
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address, pharmacy_id)
VALUES
  ('Bob', 'Johnson', '1990-01-01', 'bob.johnson@example.com', '555-123-4567', '789 Oak St', 1),
  ('Alice', 'Williams', '1995-06-01', 'alice.williams@example.com', '555-987-6543', '321 Maple St', 2);

-- Insert sample data into co-operative membership table
INSERT INTO co-operative_membership (pharmacy_id, owner_id, membership_date)
VALUES
  (1, 1, '2020-01-01'),
  (2, 2, '2020-06-01');

-- Insert sample data into prescriptions table
INSERT INTO prescriptions (patient_id, pharmacy_id, prescription_date, medication_name, dosage, refills)
VALUES
  (1, 1, '2022-01-01', 'Aspirin', '81mg', 3),
  (2, 2, '2022-06-01', 'Lisinopril', '10mg', 2);
```
