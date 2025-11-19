"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Design a database schema to store patient information, treatment plans, and therapy sessions for a center like Centro Abakadabra, including entities for patients, therapists, and services.
Generated: DETERMINISTIC_e6f2b962e0c00787
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Centro Abakadabra

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS TherapySessions;
DROP TABLE IF EXISTS TreatmentPlans;
DROP TABLE IF EXISTS Therapists;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Services;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    ContactNumber VARCHAR(15),                 -- Patient's contact number
    Email VARCHAR(100),                        -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store therapist information
CREATE TABLE Therapists (
    TherapistID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,              -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,               -- Therapist's last name
    Specialty VARCHAR(100),                       -- Therapist's area of specialty
    ContactNumber VARCHAR(15),                   -- Therapist's contact number
    Email VARCHAR(100),                          -- Therapist's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store treatment plans for patients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                          -- Foreign key referencing Patients
    TherapistID INT NOT NULL,                        -- Foreign key referencing Therapists
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE NOT NULL,                          -- End date of the treatment plan
    Notes TEXT,                                     -- Additional notes for the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,  -- Cascade delete on patient removal
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE,  -- Cascade delete on therapist removal
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete on service removal
);

-- Table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each therapy session
    TreatmentPlanID INT NOT NULL,                  -- Foreign key referencing TreatmentPlans
    SessionDate DATETIME NOT NULL,                 -- Date and time of the therapy session
    Duration INT NOT NULL,                         -- Duration of the session in minutes
    Notes TEXT,                                    -- Additional notes for the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE  -- Cascade delete on treatment plan removal
);
```
