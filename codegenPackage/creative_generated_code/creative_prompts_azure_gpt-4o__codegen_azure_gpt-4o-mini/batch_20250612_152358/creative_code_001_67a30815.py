"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Develop a database schema in SQL for managing patient records in a system modeled after SUS, including fields for patient demographics, health history, assigned healthcare team, and referral details for specialized care.
Generated: DETERMINISTIC_67a3081599dd82fc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing patient records in a healthcare system

-- Create a table to store patient demographics
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    Email VARCHAR(100),                         -- Patient's email address
    Phone VARCHAR(15),                          -- Patient's phone number
    Address VARCHAR(255),                       -- Patient's home address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store patient health history
CREATE TABLE HealthHistory (
    HealthHistoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for health history records
    PatientID INT NOT NULL,                         -- Foreign key to link to the Patients table
    MedicalCondition VARCHAR(255) NOT NULL,        -- Description of the medical condition
    DiagnosisDate DATE NOT NULL,                    -- Date when the condition was diagnosed
    Treatment VARCHAR(255),                         -- Details of the treatment prescribed
    Notes TEXT,                                     -- Additional notes about the patient's condition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table to store healthcare team information
CREATE TABLE HealthcareTeams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each healthcare team
    TeamName VARCHAR(100) NOT NULL,              -- Name of the healthcare team
    Specialization VARCHAR(100),                  -- Area of specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to assign healthcare teams to patients
CREATE TABLE PatientTeams (
    PatientTeamID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each patient-team assignment
    PatientID INT NOT NULL,                        -- Foreign key to link to the Patients table
    TeamID INT NOT NULL,                           -- Foreign key to link to the HealthcareTeams table
    AssignmentDate DATE NOT NULL,                  -- Date when the patient was assigned to the team
    Role VARCHAR(100),                             -- Role of the healthcare team in patient care
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Maintain referential integrity
    FOREIGN KEY (TeamID) REFERENCES HealthcareTeams(TeamID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table to manage referrals for specialized care
CREATE TABLE Referrals (
    ReferralID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each referral
    PatientID INT NOT NULL,                       -- Foreign key to link to the Patients table
    SpecialistName VARCHAR(100) NOT NULL,        -- Name of the specialist referred to
    ReferralDate DATE NOT NULL,                   -- Date of the referral
    ReasonForReferral TEXT NOT NULL,              -- Reason for the referral
    FollowUpDate DATE,                            -- Date for follow-up after referral
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Ensure indexes are created to optimize queries
CREATE INDEX idx_patient_email ON Patients (Email);
CREATE INDEX idx_healthhistory_patient ON HealthHistory (PatientID);
CREATE INDEX idx_patientteams_patient ON PatientTeams (PatientID);
CREATE INDEX idx_patientteams_team ON PatientTeams (TeamID);
CREATE INDEX idx_referrals_patient ON Referrals (PatientID);
```
