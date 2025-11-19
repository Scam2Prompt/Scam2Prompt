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

-- Table to store patient information
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

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Reason TEXT,                                  -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    PlanName VARCHAR(100) NOT NULL,                 -- Name of the treatment plan
    Description TEXT,                               -- Detailed description of the treatment plan
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE,                                   -- End date of the treatment plan (optional)
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name search
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate); -- Index for appointment date search
CREATE INDEX idx_treatment_status ON TreatmentPlans (Status); -- Index for treatment plan status search
```
