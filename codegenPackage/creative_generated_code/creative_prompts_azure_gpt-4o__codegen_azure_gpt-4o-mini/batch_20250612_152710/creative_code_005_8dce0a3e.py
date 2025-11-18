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

-- Table to store clinic locations
CREATE TABLE ClinicLocations (
    LocationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each location
    Address VARCHAR(255) NOT NULL,              -- Address of the clinic
    City VARCHAR(100) NOT NULL,                  -- City where the clinic is located
    State VARCHAR(100) NOT NULL,                 -- State where the clinic is located
    ZipCode VARCHAR(10) NOT NULL                 -- Zip code of the clinic
);

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each patient
    FirstName VARCHAR(100) NOT NULL,             -- Patient's first name
    LastName VARCHAR(100) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                   -- Patient's date of birth
    PhoneNumber VARCHAR(15),                      -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                   -- Patient's email (should be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store services offered by the clinic
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the service (e.g., dental crowns)
    Description TEXT,                             -- Description of the service
    Price DECIMAL(10, 2) NOT NULL                 -- Price of the service
);

-- Table to store appointment scheduling
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    LocationID INT NOT NULL,                      -- Foreign key referencing ClinicLocations
    AppointmentDateTime DATETIME NOT NULL,       -- Scheduled date and time for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Relationship to Patients
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,  -- Relationship to Services
    FOREIGN KEY (LocationID) REFERENCES ClinicLocations(LocationID) ON DELETE CASCADE -- Relationship to ClinicLocations
);
```
