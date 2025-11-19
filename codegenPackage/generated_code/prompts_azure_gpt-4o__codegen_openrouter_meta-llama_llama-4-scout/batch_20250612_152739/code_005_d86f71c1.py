"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Design a database schema for storing patient records at an integrative dental clinic, including fields for oral health data, digestive health assessments, and emotional well-being metrics.
Generated: DETERMINISTIC_d86f71c1ac3ad90b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the integrative dental clinic
CREATE DATABASE integrative_dental_clinic;

-- Use the database
USE integrative_dental_clinic;

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

-- Create a table for oral health data
CREATE TABLE oral_health_data (
  oral_health_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  dental_history TEXT,
  current_medications TEXT,
  allergies TEXT,
  oral_hygiene_habits TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (oral_health_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for digestive health assessments
CREATE TABLE digestive_health_assessments (
  assessment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  gut_health_score INT,
  digestive_symptoms TEXT,
  dietary_habits TEXT,
  probiotic_supplementation BOOLEAN,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assessment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for emotional well-being metrics
CREATE TABLE emotional_wellbeing_metrics (
  metric_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  stress_level INT,
  anxiety_score INT,
  depression_score INT,
  mindfulness_practices TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (metric_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for dental appointments
CREATE TABLE dental_appointments (
  appointment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  appointment_type VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for treatment plans
CREATE TABLE treatment_plans (
  plan_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  plan_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for lab results
CREATE TABLE lab_results (
  result_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  test_name VARCHAR(255) NOT NULL,
  test_result VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (result_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO patients (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO oral_health_data (patient_id, dental_history, current_medications, allergies, oral_hygiene_habits)
VALUES (1, 'Regular cleanings', 'None', 'None', 'Brushes and flosses daily');

INSERT INTO digestive_health_assessments (patient_id, gut_health_score, digestive_symptoms, dietary_habits, probiotic_supplementation)
VALUES (1, 50, 'Occasional bloating', 'Omnivore', TRUE);

INSERT INTO emotional_wellbeing_metrics (patient_id, stress_level, anxiety_score, depression_score, mindfulness_practices)
VALUES (1, 3, 2, 1, 'Meditates weekly');

INSERT INTO dental_appointments (patient_id, appointment_date, appointment_time, appointment_type)
VALUES (1, '2024-09-16', '10:00:00', 'Checkup');

INSERT INTO treatment_plans (patient_id, plan_description)
VALUES (1, 'Regular cleanings and checkups');

INSERT INTO lab_results (patient_id, test_name, test_result)
VALUES (1, 'Blood test', 'Normal');
```
