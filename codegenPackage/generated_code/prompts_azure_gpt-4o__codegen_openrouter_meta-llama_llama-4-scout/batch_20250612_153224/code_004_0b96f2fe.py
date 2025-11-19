"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Create a database schema to manage patient records for a multidisciplinary healthcare center, including fields for psychological evaluations, logopedic assessments, and therapy session notes, as outlined on Centro Abakadabra's webpage.
Generated: DETERMINISTIC_0b96f2fed84d2c63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the healthcare center
CREATE DATABASE centro_abakadabra;

-- Use the created database
USE centro_abakadabra;

-- Create a table for patients
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  contact_number VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (patient_id)
);

-- Create a table for psychological evaluations
CREATE TABLE psychological_evaluations (
  evaluation_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  evaluation_date DATE NOT NULL,
  symptoms TEXT,
  diagnosis TEXT,
  treatment_plan TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (evaluation_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for logopedic assessments
CREATE TABLE logopedic_assessments (
  assessment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  assessment_date DATE NOT NULL,
  speech_issues TEXT,
  language_development TEXT,
  communication_skills TEXT,
  treatment_recommendations TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assessment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for therapy sessions
CREATE TABLE therapy_sessions (
  session_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  session_date DATE NOT NULL,
  session_type VARCHAR(100) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Create a table for therapy session notes
CREATE TABLE therapy_session_notes (
  note_id INT AUTO_INCREMENT,
  session_id INT NOT NULL,
  note_date DATE NOT NULL,
  note_text TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (note_id),
  FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE CASCADE
);

-- Create a table for multidisciplinary team members
CREATE TABLE team_members (
  member_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  role VARCHAR(100) NOT NULL,
  contact_number VARCHAR(20),
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (member_id)
);

-- Create a table for patient assignments to team members
CREATE TABLE patient_assignments (
  assignment_id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  member_id INT NOT NULL,
  assigned_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_patient_id ON psychological_evaluations (patient_id);
CREATE INDEX idx_patient_id ON logopedic_assessments (patient_id);
CREATE INDEX idx_patient_id ON therapy_sessions (patient_id);
CREATE INDEX idx_session_id ON therapy_session_notes (session_id);
CREATE INDEX idx_member_id ON patient_assignments (member_id);
```

```sql
-- Example stored procedure to insert a new patient
DELIMITER //
CREATE PROCEDURE insert_patient(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_date_of_birth DATE,
  IN p_contact_number VARCHAR(20),
  IN p_email VARCHAR(255),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO patients (first_name, last_name, date_of_birth, contact_number, email, address)
  VALUES (p_first_name, p_last_name, p_date_of_birth, p_contact_number, p_email, p_address);
END//
DELIMITER ;

-- Example stored procedure to get patient details
DELIMITER //
CREATE PROCEDURE get_patient_details(
  IN p_patient_id INT
)
BEGIN
  SELECT * FROM patients
  WHERE patient_id = p_patient_id;
END//
DELIMITER ;
```

```sql
-- Example trigger to update updated_at timestamp
DELIMITER //
CREATE TRIGGER update_updated_at
BEFORE UPDATE ON patients
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;
```
