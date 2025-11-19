"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Design a database schema for storing patient medical records and information, inspired by the features and functionality of myLoyola.
Generated: DETERMINISTIC_203f3c09b357dcbe
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient medical records and information

CREATE DATABASE PatientRecordsDB;

USE PatientRecordsDB;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                  -- Patient's email address
    Address VARCHAR(255),                        -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each medical record
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients table
    VisitDate DATE NOT NULL,                     -- Date of the medical visit
    Diagnosis VARCHAR(255),                      -- Diagnosis information
    Treatment VARCHAR(255),                      -- Treatment details
    Prescriptions TEXT,                          -- Prescriptions given to the patient
    Notes TEXT,                                  -- Additional notes from the healthcare provider
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor
    ReasonForVisit VARCHAR(255),                   -- Reason for the visit
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each billing record
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount billed
    BillingDate DATE NOT NULL,                     -- Date of billing
    PaymentStatus ENUM('Paid', 'Pending', 'Failed') DEFAULT 'Pending',  -- Payment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_email ON Patients(Email);
CREATE INDEX idx_patient_visit_date ON MedicalRecords(VisitDate);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_billing_date ON Billing(BillingDate);
```
