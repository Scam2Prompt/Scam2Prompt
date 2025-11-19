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

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,          -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                   -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                 -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical professional information
CREATE TABLE MedicalProfessionals (
    ProfessionalID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,               -- Professional's first name
    LastName VARCHAR(50) NOT NULL,                 -- Professional's last name
    Specialty VARCHAR(100) NOT NULL,               -- Professional's specialty
    PhoneNumber VARCHAR(15),                        -- Professional's phone number
    Email VARCHAR(100) UNIQUE,                      -- Professional's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                          -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    ProfessionalID INT NOT NULL,                  -- Foreign key referencing MedicalProfessionals
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patients
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID) ON DELETE CASCADE, -- Cascade delete for professionals
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for services
);

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each medical record
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients
    ProfessionalID INT NOT NULL,               -- Foreign key referencing MedicalProfessionals
    RecordDate DATETIME NOT NULL,             -- Date of the medical record
    Notes TEXT,                               -- Notes from the medical professional
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patients
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID) ON DELETE CASCADE -- Cascade delete for professionals
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each billing record
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients
    AppointmentID INT NOT NULL,               -- Foreign key referencing Appointments
    Amount DECIMAL(10, 2) NOT NULL,          -- Amount billed
    PaymentStatus ENUM('Paid', 'Pending', 'Failed') DEFAULT 'Pending', -- Payment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patients
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete for appointments
);
```
