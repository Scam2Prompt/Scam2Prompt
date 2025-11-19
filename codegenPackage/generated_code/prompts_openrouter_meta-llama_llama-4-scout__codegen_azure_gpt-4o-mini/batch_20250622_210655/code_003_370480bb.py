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
-- SQL Database Schema for a Dental Clinic

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS PaymentRecords;
DROP TABLE IF EXISTS TreatmentPlans;
DROP TABLE IF EXISTS Patients;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    PhoneNumber VARCHAR(15),                    -- Patient's contact number
    Email VARCHAR(100),                         -- Patient's email address
    Address VARCHAR(255),                       -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store treatment plans for patients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                           -- Foreign key referencing Patients table
    TreatmentDescription TEXT NOT NULL,               -- Description of the treatment
    TreatmentDate DATE NOT NULL,                      -- Date of the treatment
    Cost DECIMAL(10, 2) NOT NULL,                    -- Cost of the treatment
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Status of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store payment records for treatments
CREATE TABLE PaymentRecords (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each payment record
    TreatmentPlanID INT NOT NULL,                    -- Foreign key referencing TreatmentPlans table
    PaymentDate DATE NOT NULL,                       -- Date of the payment
    Amount DECIMAL(10, 2) NOT NULL,                 -- Amount paid
    PaymentMethod ENUM('Cash', 'Credit Card', 'Insurance') NOT NULL,  -- Method of payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_treatment_patient ON TreatmentPlans(PatientID);
CREATE INDEX idx_payment_treatment ON PaymentRecords(TreatmentPlanID);
```
