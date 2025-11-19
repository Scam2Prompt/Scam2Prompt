"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Create a SQL database schema for storing patient information, treatment plans, and appointment schedules for a dental clinic like Odontoclinic Suzano.
Generated: DETERMINISTIC_dcf723483126006f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Odontoclinic Suzano

-- Create a database for the dental clinic
CREATE DATABASE OdontoclinicSuzano;

-- Use the created database
USE OdontoclinicSuzano;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Email VARCHAR(100),                        -- Patient's email address
    Address VARCHAR(255),                      -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    TreatmentDescription TEXT NOT NULL,              -- Description of the treatment
    StartDate DATE NOT NULL,                         -- Start date of the treatment
    EndDate DATE,                                   -- End date of the treatment (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- Current status of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    TreatmentPlanID INT,                          -- Foreign key referencing TreatmentPlans (nullable)
    Status ENUM('Scheduled', 'Cancelled', 'Completed') NOT NULL, -- Current status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_email ON Patients(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
