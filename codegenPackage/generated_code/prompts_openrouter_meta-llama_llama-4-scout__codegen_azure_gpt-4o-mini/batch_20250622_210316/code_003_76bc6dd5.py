"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Design a simple database schema for storing patient records, appointments, and treatment plans, inspired by the digital chart features of Luxteb.
Generated: DETERMINISTIC_76bc6dd5191290d1
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient records, appointments, and treatment plans

-- Create a table for storing patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                     -- Patient's phone number
    Email VARCHAR(100),                          -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing appointment information
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Reason VARCHAR(255),                           -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,               -- Description of the treatment plan
    StartDate DATE NOT NULL,                          -- Start date of the treatment
    EndDate DATE,                                    -- End date of the treatment (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the Appointments table for faster querying by PatientID
CREATE INDEX idx_patient_appointments ON Appointments(PatientID);

-- Create an index on the TreatmentPlans table for faster querying by PatientID
CREATE INDEX idx_patient_treatmentplans ON TreatmentPlans(PatientID);
```
