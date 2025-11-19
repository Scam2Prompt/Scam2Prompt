"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: Create a simple database schema to store information about eye surgeries, including LASIK, cataract, and keratoconus treatments, with fields for patient details and surgery specifics.
Generated: DETERMINISTIC_708827ae14198170
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about eye surgeries

-- Table to store patient details
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                -- Patient's contact number
    Email VARCHAR(100),                       -- Patient's email address
    Address TEXT                              -- Patient's residential address
);

-- Table to store surgery details
CREATE TABLE Surgeries (
    SurgeryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each surgery
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    SurgeryType ENUM('LASIK', 'Cataract', 'Keratoconus') NOT NULL, -- Type of surgery
    SurgeryDate DATE NOT NULL,                -- Date of the surgery
    SurgeonName VARCHAR(100) NOT NULL,        -- Name of the surgeon performing the surgery
    HospitalName VARCHAR(100) NOT NULL,       -- Name of the hospital where surgery is performed
    Notes TEXT,                               -- Additional notes about the surgery
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) -- Establish relationship with Patients table
);

-- Table to store follow-up details
CREATE TABLE FollowUps (
    FollowUpID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each follow-up
    SurgeryID INT NOT NULL,                    -- Foreign key referencing Surgeries table
    FollowUpDate DATE NOT NULL,                -- Date of the follow-up appointment
    DoctorName VARCHAR(100) NOT NULL,          -- Name of the doctor conducting the follow-up
    Observations TEXT,                         -- Observations made during the follow-up
    FOREIGN KEY (SurgeryID) REFERENCES Surgeries(SurgeryID) -- Establish relationship with Surgeries table
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_surgery_date ON Surgeries (SurgeryDate);        -- Index for surgery date search
CREATE INDEX idx_followup_date ON FollowUps (FollowUpDate);      -- Index for follow-up date search
```
