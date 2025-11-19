"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Design a database schema to store patient information, treatment plans, and therapy sessions for a center like Centro Abakadabra, including entities for patients, therapists, and services.
Generated: DETERMINISTIC_e6f2b962e0c00787
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

-- Create database
CREATE DATABASE centro_abakadabra;

-- Use database
USE centro_abakadabra;

-- Create table for therapists
CREATE TABLE therapists (
  therapist_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (therapist_id)
);

-- Create table for patients
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id)
);

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for treatment plans
CREATE TABLE treatment_plans (
  treatment_plan_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  therapist_id INT NOT NULL,
  service_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (treatment_plan_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for therapy sessions
CREATE TABLE therapy_sessions (
  session_id INT AUTO_INCREMENT,
  treatment_plan_id INT NOT NULL,
  session_date DATE NOT NULL,
  session_time TIME NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (treatment_plan_id) REFERENCES treatment_plans(treatment_plan_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_treatment_plans_patient_id ON treatment_plans (patient_id);
CREATE INDEX idx_treatment_plans_therapist_id ON treatment_plans (therapist_id);
CREATE INDEX idx_treatment_plans_service_id ON treatment_plans (service_id);
CREATE INDEX idx_therapy_sessions_treatment_plan_id ON therapy_sessions (treatment_plan_id);
```

```sql
-- insert_sample_data.sql

-- Insert sample data into therapists table
INSERT INTO therapists (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

-- Insert sample data into patients table
INSERT INTO patients (first_name, last_name, email, phone_number, date_of_birth)
VALUES
  ('Patient1', 'Lastname1', 'patient1@example.com', '111-111-1111', '1990-01-01'),
  ('Patient2', 'Lastname2', 'patient2@example.com', '222-222-2222', '1995-06-15');

-- Insert sample data into services table
INSERT INTO services (service_name, description)
VALUES
  ('Individual Therapy', 'One-on-one therapy sessions'),
  ('Group Therapy', 'Group therapy sessions');

-- Insert sample data into treatment_plans table
INSERT INTO treatment_plans (patient_id, therapist_id, service_id, plan_name, description, start_date, end_date)
VALUES
  (1, 1, 1, 'Plan1', 'This is plan 1', '2022-01-01', '2022-12-31'),
  (2, 2, 2, 'Plan2', 'This is plan 2', '2022-06-01', NULL);

-- Insert sample data into therapy_sessions table
INSERT INTO therapy_sessions (treatment_plan_id, session_date, session_time, notes)
VALUES
  (1, '2022-01-05', '10:00:00', 'Session notes 1'),
  (1, '2022-01-12', '10:00:00', 'Session notes 2'),
  (2, '2022-06-10', '14:00:00', 'Session notes 3');
```
