"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: Create a simple database schema to store information about eye surgeries, including LASIK, cataract, and keratoconus treatments, with fields for patient details and surgery specifics.
Generated: DETERMINISTIC_708827ae14198170
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for eye surgery information
CREATE DATABASE eye_surgery_db;

-- Use the database
USE eye_surgery_db;

-- Create table for patients
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

-- Create table for surgeons
CREATE TABLE surgeons (
  surgeon_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (surgeon_id)
);

-- Create table for surgeries
CREATE TABLE surgeries (
  surgery_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  surgeon_id INT NOT NULL,
  surgery_date DATE NOT NULL,
  surgery_type ENUM('LASIK', 'cataract', 'keratoconus') NOT NULL,
  eye VARCHAR(10) CHECK (eye IN ('left', 'right', 'both')),
  pre_op_visual_acuity DECIMAL(4, 2),
  post_op_visual_acuity DECIMAL(4, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (surgery_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (surgeon_id) REFERENCES surgeons(surgeon_id) ON DELETE CASCADE
);

-- Create table for surgery details (additional information)
CREATE TABLE surgery_details (
  detail_id INT AUTO_INCREMENT,
  surgery_id INT NOT NULL,
  treatment_details TEXT,
  complications TEXT,
  follow_up_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (detail_id),
  FOREIGN KEY (surgery_id) REFERENCES surgeries(surgery_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO surgeons (first_name, last_name, email, phone_number)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO surgeries (patient_id, surgeon_id, surgery_date, surgery_type, eye, pre_op_visual_acuity, post_op_visual_acuity)
VALUES (1, 1, '2022-01-01', 'LASIK', 'both', 0.50, 1.00);

INSERT INTO surgery_details (surgery_id, treatment_details, complications, follow_up_date)
VALUES (1, 'Patient underwent LASIK surgery without complications.', NULL, '2022-01-15');
```
