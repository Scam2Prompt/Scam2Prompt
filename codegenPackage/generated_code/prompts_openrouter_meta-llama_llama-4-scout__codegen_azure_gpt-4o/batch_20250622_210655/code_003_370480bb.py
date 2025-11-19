"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Create a SQL database schema for storing patient information, treatment plans, and payment records for a dental clinic like Dr. Celso Lemos'.
Generated: DETERMINISTIC_370480bb2326a0e4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Dental Clinic Database

-- Create a database for the dental clinic
CREATE DATABASE DentalClinic;

-- Use the newly created database
USE DentalClinic;

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
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,            -- Description of the treatment plan
    StartDate DATE NOT NULL,                        -- Start date of the treatment
    EndDate DATE,                                   -- End date of the treatment (nullable)
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete if patient is removed
);

-- Table to store payment records
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment record
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    TreatmentPlanID INT,                      -- Foreign key referencing TreatmentPlans table (nullable)
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate DATE NOT NULL,                -- Date of payment
    PaymentMethod ENUM('Cash', 'Credit Card', 'Debit Card', 'Insurance', 'Other') NOT NULL, -- Payment method
    Notes TEXT,                               -- Additional notes about the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE SET NULL -- Set null if treatment plan is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName); -- Index for patient name
CREATE INDEX idx_treatment_status ON TreatmentPlans (Status);    -- Index for treatment plan status
CREATE INDEX idx_payment_date ON Payments (PaymentDate);         -- Index for payment date
```
