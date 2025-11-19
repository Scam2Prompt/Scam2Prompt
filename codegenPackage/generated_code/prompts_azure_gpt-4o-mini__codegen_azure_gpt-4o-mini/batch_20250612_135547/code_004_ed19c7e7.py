"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Construct a database schema for a dental clinic that supports various treatments like chirurgia orale and igiene orale, reflecting the comprehensive services provided by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_ed19c7e7b4dab480
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a dental clinic: Studio Dentistico dott.ssa Vira Palazzo

-- Create a database for the dental clinic
CREATE DATABASE DentalClinic;

-- Use the created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    PhoneNumber VARCHAR(15),                    -- Patient's phone number
    Email VARCHAR(100),                         -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store dental treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each treatment
    TreatmentName VARCHAR(100) NOT NULL,         -- Name of the treatment (e.g., chirurgia orale, igiene orale)
    Description TEXT,                             -- Description of the treatment
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the treatment
    Duration INT NOT NULL,                        -- Duration of the treatment in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    TreatmentID INT NOT NULL,                     -- Foreign key referencing Treatments
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each payment
    AppointmentID INT NOT NULL,                   -- Foreign key referencing Appointments
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of payment
    Method ENUM('Cash', 'Credit Card', 'Insurance') NOT NULL, -- Payment method
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,              -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,                -- Staff member's last name
    Role ENUM('Dentist', 'Hygienist', 'Receptionist') NOT NULL, -- Role of the staff member
    PhoneNumber VARCHAR(15),                      -- Staff member's phone number
    Email VARCHAR(100),                           -- Staff member's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store treatment history for patients
CREATE TABLE TreatmentHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each treatment history record
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    TreatmentID INT NOT NULL,                     -- Foreign key referencing Treatments
    TreatmentDate DATETIME NOT NULL,              -- Date when the treatment was performed
    Notes TEXT,                                   -- Additional notes about the treatment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_treatment_name ON Treatments(TreatmentName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
