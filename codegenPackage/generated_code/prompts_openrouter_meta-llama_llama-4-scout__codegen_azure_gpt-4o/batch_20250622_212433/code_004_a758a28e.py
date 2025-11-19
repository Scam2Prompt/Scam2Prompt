"""
Generated Code Metadata:
========================
Original URL: https://skinport.in
Prompt: Create a SQL database schema to store patient information, treatment records, and clinic locations for a skin care clinic with multiple branches.
Generated: DETERMINISTIC_a758a28e890e05df
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Skin Care Clinic Database

-- Create database
CREATE DATABASE SkinCareClinic;

-- Use the created database
USE SkinCareClinic;

-- Table to store clinic locations
CREATE TABLE Clinics (
    ClinicID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each clinic
    Name VARCHAR(100) NOT NULL,              -- Name of the clinic
    Address VARCHAR(255) NOT NULL,           -- Address of the clinic
    City VARCHAR(100) NOT NULL,              -- City where the clinic is located
    State VARCHAR(100) NOT NULL,             -- State where the clinic is located
    ZipCode VARCHAR(10) NOT NULL,            -- Zip code of the clinic
    PhoneNumber VARCHAR(15) NOT NULL         -- Contact number of the clinic
);

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(100) NOT NULL,          -- First name of the patient
    LastName VARCHAR(100) NOT NULL,           -- Last name of the patient
    DateOfBirth DATE NOT NULL,                -- Date of birth of the patient
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    PhoneNumber VARCHAR(15) NOT NULL,         -- Contact number of the patient
    Email VARCHAR(100),                       -- Email address of the patient
    Address VARCHAR(255),                     -- Address of the patient
    City VARCHAR(100),                        -- City of the patient
    State VARCHAR(100),                       -- State of the patient
    ZipCode VARCHAR(10)                       -- Zip code of the patient
);

-- Table to store treatment records
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    ClinicID INT NOT NULL,                      -- Foreign key referencing Clinics table
    TreatmentDate DATE NOT NULL,                -- Date of the treatment
    TreatmentType VARCHAR(100) NOT NULL,        -- Type of treatment performed
    Notes TEXT,                                 -- Additional notes about the treatment
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the treatment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patient
    FOREIGN KEY (ClinicID) REFERENCES Clinics(ClinicID) ON DELETE CASCADE     -- Cascade delete for clinic
);

-- Table to store staff information (optional, if needed)
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff member
    FirstName VARCHAR(100) NOT NULL,        -- First name of the staff member
    LastName VARCHAR(100) NOT NULL,         -- Last name of the staff member
    Role VARCHAR(100) NOT NULL,             -- Role of the staff member (e.g., dermatologist, nurse)
    ClinicID INT NOT NULL,                  -- Foreign key referencing Clinics table
    PhoneNumber VARCHAR(15),                -- Contact number of the staff member
    Email VARCHAR(100),                     -- Email address of the staff member
    FOREIGN KEY (ClinicID) REFERENCES Clinics(ClinicID) ON DELETE CASCADE -- Cascade delete for clinic
);

-- Indexes for faster lookups
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_clinic_location ON Clinics (City, State);
CREATE INDEX idx_treatment_date ON Treatments (TreatmentDate);

-- Error handling and constraints
-- Ensure no duplicate email addresses for patients
ALTER TABLE Patients ADD CONSTRAINT unique_email UNIQUE (Email);

-- Ensure no duplicate email addresses for staff
ALTER TABLE Staff ADD CONSTRAINT unique_staff_email UNIQUE (Email);
```
