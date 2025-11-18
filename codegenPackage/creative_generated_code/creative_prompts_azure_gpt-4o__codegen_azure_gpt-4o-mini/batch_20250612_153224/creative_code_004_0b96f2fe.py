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
-- Database schema for managing patient records in a multidisciplinary healthcare center
CREATE DATABASE IF NOT EXISTS CentroAbakadabra;

USE CentroAbakadabra;

-- Table to store patient information
CREATE TABLE IF NOT EXISTS Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    ContactNumber VARCHAR(15),
    Email VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store psychological evaluations
CREATE TABLE IF NOT EXISTS PsychologicalEvaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    EvaluationDate DATE NOT NULL,
    EvaluatorName VARCHAR(100) NOT NULL,
    EvaluationDetails TEXT,
    Recommendations TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store logopedic assessments
CREATE TABLE IF NOT EXISTS LogopedicAssessments (
    AssessmentID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    AssessmentDate DATE NOT NULL,
    AssessorName VARCHAR(100) NOT NULL,
    AssessmentDetails TEXT,
    Recommendations TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store therapy session notes
CREATE TABLE IF NOT EXISTS TherapySessionNotes (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    SessionDate DATE NOT NULL,
    TherapistName VARCHAR(100) NOT NULL,
    SessionNotes TEXT,
    FollowUpDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Indexing for improved performance
CREATE INDEX idx_patient_name ON Patients (LastName, FirstName);
CREATE INDEX idx_evaluation_patient ON PsychologicalEvaluations (PatientID);
CREATE INDEX idx_assessment_patient ON LogopedicAssessments (PatientID);
CREATE INDEX idx_session_patient ON TherapySessionNotes (PatientID);
```
