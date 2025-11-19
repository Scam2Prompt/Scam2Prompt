"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a database schema to store information about surgical procedures, including cosmetic surgical, non-surgical, and reconstructive surgery details.
Generated: DETERMINISTIC_e55ddcecf73f5ba7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for surgical procedures
CREATE DATABASE surgical_procedures;

-- Use the database
USE surgical_procedures;

-- Create a table for surgeons
CREATE TABLE surgeons (
  surgeon_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (surgeon_id)
);

-- Create a table for surgical procedures
CREATE TABLE surgical_procedures (
  procedure_id INT AUTO_INCREMENT,
  procedure_name VARCHAR(255) NOT NULL,
  procedure_type ENUM('cosmetic', 'non-surgical', 'reconstructive') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (procedure_id)
);

-- Create a table for patients
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id)
);

-- Create a table for procedure details
CREATE TABLE procedure_details (
  detail_id INT AUTO_INCREMENT,
  procedure_id INT NOT NULL,
  patient_id INT NOT NULL,
  surgeon_id INT NOT NULL,
  procedure_date DATE NOT NULL,
  procedure_outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (detail_id),
  FOREIGN KEY (procedure_id) REFERENCES surgical_procedures(procedure_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (surgeon_id) REFERENCES surgeons(surgeon_id)
);

-- Create a table for non-surgical procedure details
CREATE TABLE non_surgical_procedure_details (
  detail_id INT NOT NULL,
  treatment_area VARCHAR(255) NOT NULL,
  treatment_type VARCHAR(255) NOT NULL,
  PRIMARY KEY (detail_id),
  FOREIGN KEY (detail_id) REFERENCES procedure_details(detail_id)
);

-- Create a table for cosmetic surgical procedure details
CREATE TABLE cosmetic_surgical_procedure_details (
  detail_id INT NOT NULL,
  surgery_type VARCHAR(255) NOT NULL,
  incision_site VARCHAR(255) NOT NULL,
  PRIMARY KEY (detail_id),
  FOREIGN KEY (detail_id) REFERENCES procedure_details(detail_id)
);

-- Create a table for reconstructive surgical procedure details
CREATE TABLE reconstructive_surgical_procedure_details (
  detail_id INT NOT NULL,
  reconstruction_type VARCHAR(255) NOT NULL,
  affected_area VARCHAR(255) NOT NULL,
  PRIMARY KEY (detail_id),
  FOREIGN KEY (detail_id) REFERENCES procedure_details(detail_id)
);
```

```sql
-- insert_sample_data.sql

-- Insert sample data into the database
INSERT INTO surgeons (first_name, last_name, email)
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com');

INSERT INTO surgical_procedures (procedure_name, procedure_type, description)
VALUES 
('Facelift', 'cosmetic', 'A surgical procedure to lift and tighten the facial skin'),
('Botox', 'non-surgical', 'A non-surgical procedure to temporarily relax facial muscles'),
('Breast Reconstruction', 'reconstructive', 'A surgical procedure to reconstruct the breast tissue');

INSERT INTO patients (first_name, last_name, date_of_birth, email)
VALUES 
('Bob', 'Johnson', '1990-01-01', 'bob.johnson@example.com'),
('Alice', 'Williams', '1995-06-01', 'alice.williams@example.com');

INSERT INTO procedure_details (procedure_id, patient_id, surgeon_id, procedure_date, procedure_outcome)
VALUES 
(1, 1, 1, '2022-01-01', 'Successful'),
(2, 2, 2, '2022-06-01', 'Successful'),
(3, 1, 1, '2022-12-01', 'Successful');

INSERT INTO non_surgical_procedure_details (detail_id, treatment_area, treatment_type)
VALUES 
(2, 'Forehead', 'Botox Injection');

INSERT INTO cosmetic_surgical_procedure_details (detail_id, surgery_type, incision_site)
VALUES 
(1, 'Facelift', 'Hairline');

INSERT INTO reconstructive_surgical_procedure_details (detail_id, reconstruction_type, affected_area)
VALUES 
(3, 'Breast Implant', 'Breast');
```
