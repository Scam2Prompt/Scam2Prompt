"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: Design a database schema to store patient information and treatment plans for an orthopedic practice like Gelenkzentrum Mönchengladbach.
Generated: DETERMINISTIC_8cb7614a8c3f0c60
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient information and treatment plans
CREATE DATABASE OrthopedicPractice;

USE OrthopedicPractice;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    Address VARCHAR(255),                       -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients table
    TreatmentDate DATE NOT NULL,                     -- Date of the treatment
    Diagnosis VARCHAR(255) NOT NULL,                -- Diagnosis details
    TreatmentDescription TEXT NOT NULL,              -- Description of the treatment plan
    FollowUpDate DATE,                              -- Date for follow-up appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store medical history for patients
CREATE TABLE MedicalHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each medical history record
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    Condition VARCHAR(255) NOT NULL,               -- Medical condition
    Treatment VARCHAR(255),                         -- Treatment received
    DateDiagnosed DATE,                            -- Date when the condition was diagnosed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each appointment
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    ReasonForVisit VARCHAR(255),                    -- Reason for the visit
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
