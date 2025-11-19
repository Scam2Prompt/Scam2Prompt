"""
Generated Code Metadata:
========================
Original URL: https://institutovidaesportiva.com.br
Prompt: Develop a SQL database schema to store information about patients, medical professionals, and services offered by Instituto Vida Esportiva, including tables for appointments, medical records, and billing.
Generated: DETERMINISTIC_f2105c058cf589c9
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Instituto Vida Esportiva

-- Table to store information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT                              -- Patient's address
);

-- Table to store information about medical professionals
CREATE TABLE MedicalProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,                -- Professional's first name
    LastName VARCHAR(50) NOT NULL,                 -- Professional's last name
    Specialty VARCHAR(100) NOT NULL,               -- Area of expertise or specialty
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Email VARCHAR(100),                            -- Contact email
    LicenseNumber VARCHAR(50) NOT NULL UNIQUE      -- Unique medical license number
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL             -- Cost of the service
);

-- Table to store appointment details
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    ProfessionalID INT NOT NULL,                  -- Foreign key referencing MedicalProfessionals table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL, -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medical record
    PatientID INT NOT NULL,                  -- Foreign key referencing Patients table
    ProfessionalID INT NOT NULL,             -- Foreign key referencing MedicalProfessionals table
    RecordDate DATETIME NOT NULL,            -- Date and time of the record entry
    Diagnosis TEXT NOT NULL,                 -- Diagnosis details
    TreatmentPlan TEXT,                      -- Treatment plan details
    Notes TEXT,                              -- Additional notes
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID)
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each billing record
    AppointmentID INT NOT NULL,               -- Foreign key referencing Appointments table
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount billed
    PaymentStatus ENUM('Pending', 'Paid', 'Overdue') NOT NULL, -- Payment status
    PaymentDate DATE,                         -- Date of payment (if applicable)
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Ensure all tables are created successfully
-- Use appropriate indexes for performance optimization
-- Add constraints to enforce data integrity
```
