"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Create a database schema for storing patient records in a digital format, including custom fields for dental quadrant annotations, inspired by LuxChart functionality in Luxteb.
Generated: DETERMINISTIC_59a3c6c21d3e1dcb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing patient records

-- Create a database
CREATE DATABASE dental_records;

-- Use the database
USE dental_records;

-- Create a table for patients
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id)
);

-- Create a table for patient records
CREATE TABLE patient_records (
  record_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  record_date DATE NOT NULL,
  chief_complaint TEXT,
  medical_history TEXT,
  dental_history TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (record_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Create a table for dental quadrant annotations
CREATE TABLE dental_quadrant_annotations (
  annotation_id INT AUTO_INCREMENT,
  record_id INT NOT NULL,
  quadrant ENUM('UR', 'UL', 'LR', 'LL') NOT NULL,
  tooth_number INT,
  annotation TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (annotation_id),
  FOREIGN KEY (record_id) REFERENCES patient_records(record_id)
);

-- Create a table for dental chart annotations (inspired by LuxChart)
CREATE TABLE dental_chart_annotations (
  annotation_id INT AUTO_INCREMENT,
  record_id INT NOT NULL,
  tooth_number INT NOT NULL,
  surface ENUM('M', 'D', 'I', 'O', 'C') NOT NULL,
  annotation TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (annotation_id),
  FOREIGN KEY (record_id) REFERENCES patient_records(record_id)
);

-- Create a table for treatment plans
CREATE TABLE treatment_plans (
  plan_id INT AUTO_INCREMENT,
  record_id INT NOT NULL,
  plan_date DATE NOT NULL,
  description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id),
  FOREIGN KEY (record_id) REFERENCES patient_records(record_id)
);

-- Create a table for treatment plan procedures
CREATE TABLE treatment_plan_procedures (
  procedure_id INT AUTO_INCREMENT,
  plan_id INT NOT NULL,
  procedure_date DATE NOT NULL,
  procedure_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (procedure_id),
  FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_patient_records_patient_id ON patient_records(patient_id);
CREATE INDEX idx_dental_quadrant_annotations_record_id ON dental_quadrant_annotations(record_id);
CREATE INDEX idx_dental_chart_annotations_record_id ON dental_chart_annotations(record_id);
CREATE INDEX idx_treatment_plans_record_id ON treatment_plans(record_id);
CREATE INDEX idx_treatment_plan_procedures_plan_id ON treatment_plan_procedures(plan_id);
```

```sql
-- Example usage:

-- Insert a patient
INSERT INTO patients (first_name, last_name, date_of_birth)
VALUES ('John', 'Doe', '1990-01-01');

-- Insert a patient record
INSERT INTO patient_records (patient_id, record_date, chief_complaint)
VALUES (1, '2022-01-01', 'Toothache');

-- Insert a dental quadrant annotation
INSERT INTO dental_quadrant_annotations (record_id, quadrant, tooth_number, annotation)
VALUES (1, 'UR', 10, 'Decay');

-- Insert a dental chart annotation
INSERT INTO dental_chart_annotations (record_id, tooth_number, surface, annotation)
VALUES (1, 10, 'M', 'Filling');

-- Insert a treatment plan
INSERT INTO treatment_plans (record_id, plan_date, description)
VALUES (1, '2022-01-15', 'Root canal');

-- Insert a treatment plan procedure
INSERT INTO treatment_plan_procedures (plan_id, procedure_date, procedure_description)
VALUES (1, '2022-01-15', 'Administer anesthesia');
```
