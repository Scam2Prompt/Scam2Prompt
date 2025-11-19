"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Design a database schema to store patient data and therapy outcomes for a DBT clinic, and provide a SQL code example for data querying and analysis."
Generated: DETERMINISTIC_0583b3eae5a9ec88
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for DBT clinic
CREATE DATABASE dbt_clinic;

-- Use the database
USE dbt_clinic;

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

-- Create table for therapists
CREATE TABLE therapists (
  therapist_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (therapist_id)
);

-- Create table for therapy sessions
CREATE TABLE therapy_sessions (
  session_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  therapist_id INT NOT NULL,
  session_date DATE NOT NULL,
  session_type VARCHAR(255) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id)
);

-- Create table for therapy outcomes
CREATE TABLE therapy_outcomes (
  outcome_id INT AUTO_INCREMENT,
  session_id INT NOT NULL,
  outcome_date DATE NOT NULL,
  outcome_type VARCHAR(255) NOT NULL,
  score DECIMAL(3, 2) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (outcome_id),
  FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id)
);

-- Insert sample data
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', '1995-06-01', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO therapists (first_name, last_name, email, phone_number)
VALUES 
('Therapist', 'One', 'therapist1@example.com', '555-123-4567'),
('Therapist', 'Two', 'therapist2@example.com', '555-901-2345');

INSERT INTO therapy_sessions (patient_id, therapist_id, session_date, session_type, notes)
VALUES 
(1, 1, '2022-01-01', 'Individual', 'Initial assessment'),
(1, 1, '2022-01-08', 'Individual', 'Follow-up session'),
(2, 2, '2022-06-01', 'Group', 'Initial group session');

INSERT INTO therapy_outcomes (session_id, outcome_date, outcome_type, score, notes)
VALUES 
(1, '2022-01-01', 'PHQ-9', 10.0, 'Baseline score'),
(2, '2022-01-08', 'PHQ-9', 8.0, 'Improved score'),
(3, '2022-06-01', 'GAD-7', 12.0, 'Group session score');

-- Query patient data and therapy outcomes
SELECT 
  p.patient_id, 
  p.first_name, 
  p.last_name, 
  ts.session_date, 
  to.outcome_type, 
  to.score
FROM 
  patients p
  JOIN therapy_sessions ts ON p.patient_id = ts.patient_id
  JOIN therapy_outcomes to ON ts.session_id = to.session_id
ORDER BY 
  p.patient_id, 
  ts.session_date;

-- Analyze therapy outcomes for a specific patient
SELECT 
  p.patient_id, 
  p.first_name, 
  p.last_name, 
  AVG(to.score) AS average_score
FROM 
  patients p
  JOIN therapy_sessions ts ON p.patient_id = ts.patient_id
  JOIN therapy_outcomes to ON ts.session_id = to.session_id
WHERE 
  p.patient_id = 1
GROUP BY 
  p.patient_id, 
  p.first_name, 
  p.last_name;

-- Analyze therapy outcomes for a specific therapist
SELECT 
  t.therapist_id, 
  t.first_name, 
  t.last_name, 
  AVG(to.score) AS average_score
FROM 
  therapists t
  JOIN therapy_sessions ts ON t.therapist_id = ts.therapist_id
  JOIN therapy_outcomes to ON ts.session_id = to.session_id
GROUP BY 
  t.therapist_id, 
  t.first_name, 
  t.last_name;
```
