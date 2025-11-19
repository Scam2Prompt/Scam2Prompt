"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Develop a simple database schema for storing information on dental treatments, including fields for treatment type, patient ID, and dentist notes, based on Tiziano Testori's clinical activities.
Generated: DETERMINISTIC_95479af5908dce49
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing dental treatment information

-- Create a database for dental treatments
CREATE DATABASE DentalClinic;

-- Use the created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    ContactNumber VARCHAR(15)                   -- Patient's contact number
);

-- Table to store dentist information
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each dentist
    FirstName VARCHAR(50) NOT NULL,            -- Dentist's first name
    LastName VARCHAR(50) NOT NULL,             -- Dentist's last name
    LicenseNumber VARCHAR(20) NOT NULL UNIQUE   -- Dentist's license number
);

-- Table to store dental treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    DentistID INT NOT NULL,                     -- Foreign key referencing Dentists table
    TreatmentType VARCHAR(100) NOT NULL,       -- Type of dental treatment
    TreatmentDate DATE NOT NULL,                -- Date of the treatment
    DentistNotes TEXT,                          -- Notes from the dentist regarding the treatment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_id ON Treatments(PatientID);
CREATE INDEX idx_dentist_id ON Treatments(DentistID);
```
