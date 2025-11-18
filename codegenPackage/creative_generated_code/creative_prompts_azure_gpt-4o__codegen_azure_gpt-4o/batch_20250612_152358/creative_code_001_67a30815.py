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
-- Database schema for managing patient records in a healthcare system modeled after SUS

-- Table to store patient demographic information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(100) NOT NULL,           -- Patient's first name
    LastName VARCHAR(100) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    Email VARCHAR(255),                        -- Patient's email address
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Address TEXT NOT NULL,                     -- Patient's residential address
    City VARCHAR(100) NOT NULL,                -- City of residence
    State VARCHAR(100) NOT NULL,               -- State of residence
    PostalCode VARCHAR(10)                     -- Postal code
);

-- Table to store patient health history
CREATE TABLE HealthHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each health history record
    PatientID INT NOT NULL,                    -- Foreign key linking to the Patients table
    Condition VARCHAR(255) NOT NULL,           -- Description of a medical condition
    DiagnosisDate DATE,                        -- Date of diagnosis
    TreatmentDetails TEXT,                     -- Details about treatments or procedures
    Notes TEXT,                                -- Additional notes about the condition
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store information about the healthcare team
CREATE TABLE HealthcareTeam (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the healthcare team
    TeamName VARCHAR(100) NOT NULL,            -- Name of the healthcare team
    Description TEXT                           -- Description or notes about the team
);

-- Table to map patients to their assigned healthcare teams
CREATE TABLE PatientHealthcareTeam (
    PatientTeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    PatientID INT NOT NULL,                        -- Foreign key linking to the Patients table
    TeamID INT NOT NULL,                           -- Foreign key linking to the HealthcareTeam table
    AssignedDate DATE NOT NULL,                    -- Date the team was assigned to the patient
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (TeamID) REFERENCES HealthcareTeam(TeamID) ON DELETE CASCADE
);

-- Table to store referral information for specialized care
CREATE TABLE Referrals (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each referral
    PatientID INT NOT NULL,                     -- Foreign key linking to the Patients table
    SpecialistName VARCHAR(100) NOT NULL,       -- Name of the specialist referred to
    Specialty VARCHAR(100) NOT NULL,            -- Specialty of the referred specialist
    ReferralDate DATE NOT NULL,                 -- Date of referral
    Reason TEXT NOT NULL,                       -- Reason for referral
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the referral
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- End of schema
```
