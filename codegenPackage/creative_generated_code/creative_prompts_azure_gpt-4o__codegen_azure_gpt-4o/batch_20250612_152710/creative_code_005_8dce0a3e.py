"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Suggest a database schema for a dental clinic management system that includes tables for patient information, services offered (e.g., dental crowns, fluoride treatments), appointment scheduling, and clinic locations.
Generated: DETERMINISTIC_8dce0a3eb10d254d
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Dental Clinic Management System

-- Table: Patients
-- Stores information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- First name of the patient
    LastName VARCHAR(50) NOT NULL,            -- Last name of the patient
    DateOfBirth DATE NOT NULL,                -- Date of birth of the patient
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Email address
    Address VARCHAR(255),                     -- Residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Services
-- Stores information about services offered at the clinic
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., Dental Crowns, Fluoride Treatments)
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationMinutes INT NOT NULL,             -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: ClinicLocations
-- Stores information about clinic locations
CREATE TABLE ClinicLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each clinic location
    Name VARCHAR(100) NOT NULL,                -- Name of the clinic location
    Address VARCHAR(255) NOT NULL,             -- Address of the clinic
    PhoneNumber VARCHAR(15),                   -- Contact phone number for the clinic
    OpeningHours VARCHAR(50),                  -- Hours of operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Appointments
-- Stores information about scheduled appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Reference to the patient (foreign key)
    ServiceID INT NOT NULL,                       -- Reference to the service (foreign key)
    LocationID INT NOT NULL,                      -- Reference to the clinic location (foreign key)
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE RESTRICT, -- Ensures referential integrity
    FOREIGN KEY (LocationID) REFERENCES ClinicLocations(LocationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Ensure all tables are created with proper indexing for optimal performance
-- This schema is designed to handle typical operations for a dental clinic management system.
```
