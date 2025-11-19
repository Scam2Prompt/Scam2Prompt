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
-- Database schema for storing information on dental treatments
-- This schema is designed to be clean, efficient, and production-ready.

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE,                         -- Patient's date of birth
    ContactNumber VARCHAR(15),                -- Patient's contact number
    Email VARCHAR(100),                       -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for dental treatments
CREATE TABLE DentalTreatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    TreatmentType VARCHAR(100) NOT NULL,        -- Type of dental treatment (e.g., cleaning, filling, etc.)
    DentistNotes TEXT,                          -- Notes from the dentist about the treatment
    TreatmentDate DATE NOT NULL,                -- Date of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for dentists (optional, if needed for tracking dentist information)
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each dentist
    FirstName VARCHAR(50) NOT NULL,            -- Dentist's first name
    LastName VARCHAR(50) NOT NULL,             -- Dentist's last name
    Specialty VARCHAR(100),                    -- Dentist's specialty (e.g., orthodontics, periodontics, etc.)
    ContactNumber VARCHAR(15),                 -- Dentist's contact number
    Email VARCHAR(100),                        -- Dentist's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for associating treatments with dentists (optional, if needed)
CREATE TABLE DentistTreatments (
    DentistTreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    DentistID INT NOT NULL,                            -- Foreign key referencing Dentists table
    TreatmentID INT NOT NULL,                          -- Foreign key referencing DentalTreatments table
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TreatmentID) REFERENCES DentalTreatments(TreatmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_treatment ON DentalTreatments(PatientID, TreatmentDate); -- Index for faster lookups by patient and date
CREATE INDEX idx_dentist_treatment ON DentistTreatments(DentistID, TreatmentID); -- Index for faster lookups by dentist and treatment
```
