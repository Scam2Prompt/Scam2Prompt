"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Create a database schema to manage patient records for a multidisciplinary healthcare center, including fields for psychological evaluations, logopedic assessments, and therapy session notes, as outlined on Centro Abakadabra's webpage.
Generated: DETERMINISTIC_0b96f2fed84d2c63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for managing patient records in a multidisciplinary healthcare center

CREATE DATABASE HealthcareCenter;

USE HealthcareCenter;

-- Table for storing basic patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,               -- Patient's first name
    LastName VARCHAR(50) NOT NULL,                -- Patient's last name
    DateOfBirth DATE NOT NULL,                    -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                    -- Patient's contact number
    Email VARCHAR(100),                           -- Patient's email address
    Address TEXT,                                 -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of patient record creation
);

-- Table for storing psychological evaluations
CREATE TABLE PsychologicalEvaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each evaluation
    PatientID INT NOT NULL,                       -- Foreign key linking to Patients table
    EvaluationDate DATE NOT NULL,                 -- Date of psychological evaluation
    EvaluatorName VARCHAR(100) NOT NULL,          -- Name of the psychologist performing the evaluation
    EvaluationNotes TEXT NOT NULL,                -- Detailed notes from the evaluation
    Diagnosis TEXT,                               -- Psychological diagnosis, if applicable
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing logopedic assessments
CREATE TABLE LogopedicAssessments (
    AssessmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each assessment
    PatientID INT NOT NULL,                       -- Foreign key linking to Patients table
    AssessmentDate DATE NOT NULL,                 -- Date of logopedic assessment
    AssessorName VARCHAR(100) NOT NULL,           -- Name of the logopedist performing the assessment
    AssessmentNotes TEXT NOT NULL,                -- Detailed notes from the assessment
    TherapyPlan TEXT,                             -- Proposed therapy plan, if applicable
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing therapy session notes
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each therapy session
    PatientID INT NOT NULL,                       -- Foreign key linking to Patients table
    SessionDate DATE NOT NULL,                    -- Date of the therapy session
    TherapistName VARCHAR(100) NOT NULL,          -- Name of the therapist conducting the session
    SessionNotes TEXT NOT NULL,                   -- Detailed notes from the session
    SessionType ENUM('Psychological', 'Logopedic', 'Other'), -- Type of therapy session
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients(FirstName, LastName);
CREATE INDEX idx_psych_eval_date ON PsychologicalEvaluations(EvaluationDate);
CREATE INDEX idx_logo_assess_date ON LogopedicAssessments(AssessmentDate);
CREATE INDEX idx_therapy_date ON TherapySessions(SessionDate);

-- Ensure consistent storage engine
SET default_storage_engine=INNODB;
```
