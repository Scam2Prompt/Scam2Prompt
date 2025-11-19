"""
Generated Code Metadata:
========================
Original URL: https://draisabelanobre.com.br
Prompt: "Generate a SQL database schema to store information about patients, procedures, and appointments for a facial harmonization clinic like Dra. Isabela Nobre's."
Generated: DETERMINISTIC_ec6dd14fe0626da0
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Facial Harmonization Clinic Database

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store procedure information
CREATE TABLE Procedures (
    ProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procedure
    Name VARCHAR(100) NOT NULL,                 -- Name of the procedure
    Description TEXT,                           -- Detailed description of the procedure
    Price DECIMAL(10, 2) NOT NULL,              -- Cost of the procedure
    DurationMinutes INT NOT NULL,               -- Duration of the procedure in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    ProcedureID INT NOT NULL,                     -- Foreign key referencing Procedures table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL, -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patient
    FOREIGN KEY (ProcedureID) REFERENCES Procedures(ProcedureID) ON DELETE CASCADE -- Cascade delete for procedure
);

-- Create indexes for faster lookups
CREATE INDEX idx_patient_id ON Appointments(PatientID);
CREATE INDEX idx_procedure_id ON Appointments(ProcedureID);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
