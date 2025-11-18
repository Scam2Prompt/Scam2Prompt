"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Design a database schema for storing patient records at an integrative dental clinic, including fields for oral health data, digestive health assessments, and emotional well-being metrics.
Generated: DETERMINISTIC_d86f71c1ac3ad90b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing patient records at an integrative dental clinic
-- Includes fields for oral health data, digestive health assessments, and emotional well-being metrics

-- Create table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,                -- Patient's first name
    LastName VARCHAR(50) NOT NULL,                 -- Patient's last name
    DateOfBirth DATE NOT NULL,                     -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                     -- Patient's contact phone number
    EmailAddress VARCHAR(100),                     -- Patient's email address
    Address TEXT                                    -- Patient's residential address
);

-- Create table for oral health data
CREATE TABLE OralHealthRecords (
    OralHealthID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for oral health record
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    LastDentalExam DATE,                           -- Date of the last dental examination
    ToothDecay BOOLEAN DEFAULT FALSE,             -- Indicates presence of tooth decay
    GumDisease BOOLEAN DEFAULT FALSE,             -- Indicates presence of gum disease
    OrthodonticIssues TEXT,                       -- Description of orthodontic issues (if any)
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create table for digestive health assessments
CREATE TABLE DigestiveHealthRecords (
    DigestiveHealthID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for digestive health record
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    DietaryHabits TEXT,                               -- Description of dietary habits
    DigestiveIssues TEXT,                             -- Description of digestive issues (if any)
    LastDigestiveHealthExam DATE,                    -- Date of the last digestive health examination
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create table for emotional well-being metrics
CREATE TABLE EmotionalWellbeingRecords (
    EmotionalWellbeingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for emotional well-being record
    PatientID INT NOT NULL,                              -- Foreign key referencing Patients table
    StressLevel ENUM('Low', 'Moderate', 'High') DEFAULT 'Moderate', -- Patient's stress level
    SleepQuality ENUM('Poor', 'Average', 'Good') DEFAULT 'Average', -- Patient's sleep quality
    AnxietyLevel ENUM('Low', 'Moderate', 'High') DEFAULT 'Moderate', -- Patient's anxiety level
    LastMentalHealthAssessment DATE,                    -- Date of the last mental health assessment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Add indexing for better query performance (optional but recommended in production)
CREATE INDEX idx_patient_oral ON OralHealthRecords(PatientID);
CREATE INDEX idx_patient_digestive ON DigestiveHealthRecords(PatientID);
CREATE INDEX idx_patient_emotional ON EmotionalWellbeingRecords(PatientID);
```
