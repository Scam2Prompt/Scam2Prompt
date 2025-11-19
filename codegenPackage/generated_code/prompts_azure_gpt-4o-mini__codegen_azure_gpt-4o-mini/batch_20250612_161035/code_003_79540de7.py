"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Describe how to create a database schema for managing health records in a SUS-based healthcare system, including tables for patients, health professionals, and services.
Generated: DETERMINISTIC_79540de79ff6728e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing health records in a SUS-based healthcare system

-- Create a table for storing patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                     -- Patient's phone number
    Email VARCHAR(100),                          -- Patient's email address
    Address VARCHAR(255),                        -- Patient's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing health professional information
CREATE TABLE HealthProfessionals (
    ProfessionalID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each health professional
    FirstName VARCHAR(50) NOT NULL,                -- Professional's first name
    LastName VARCHAR(50) NOT NULL,                 -- Professional's last name
    Specialty VARCHAR(100) NOT NULL,               -- Professional's area of specialty
    PhoneNumber VARCHAR(15),                        -- Professional's phone number
    Email VARCHAR(100),                             -- Professional's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing services provided
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service
    Description TEXT,                              -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,                 -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for managing appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each appointment
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthProfessionals
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProfessionalID) REFERENCES HealthProfessionals(ProfessionalID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing medical records
CREATE TABLE MedicalRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each medical record
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients
    ProfessionalID INT NOT NULL,                    -- Foreign key referencing HealthProfessionals
    RecordDate DATETIME NOT NULL,                   -- Date of the medical record
    Notes TEXT,                                     -- Notes regarding the medical record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProfessionalID) REFERENCES HealthProfessionals(ProfessionalID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
