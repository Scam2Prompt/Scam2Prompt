"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema in SQL to manage the records of beneficiaries receiving support from the Rakhshanda Memorial's medical camps and psychological health services.
Generated: DETERMINISTIC_54d4628dca4aeffc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing records of beneficiaries receiving support
-- from Rakhshanda Memorial's medical camps and psychological health services.

-- Create a table to store beneficiary information
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FirstName VARCHAR(100) NOT NULL,             -- First name of the beneficiary
    LastName VARCHAR(100) NOT NULL,              -- Last name of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the beneficiary
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    ContactNumber VARCHAR(15),                   -- Contact number of the beneficiary
    Email VARCHAR(100),                          -- Email address of the beneficiary
    Address TEXT,                                -- Address of the beneficiary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store medical camp details
CREATE TABLE MedicalCamps (
    CampID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each medical camp
    CampName VARCHAR(255) NOT NULL,              -- Name of the medical camp
    Location VARCHAR(255) NOT NULL,              -- Location of the medical camp
    StartDate DATE NOT NULL,                     -- Start date of the medical camp
    EndDate DATE NOT NULL,                       -- End date of the medical camp
    Description TEXT,                            -- Description of the medical camp
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store psychological health service details
CREATE TABLE PsychologicalServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each psychological service
    ServiceName VARCHAR(255) NOT NULL,           -- Name of the psychological service
    Description TEXT,                            -- Description of the psychological service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to track beneficiaries attending medical camps
CREATE TABLE BeneficiaryMedicalCamps (
    ID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each record
    BeneficiaryID INT NOT NULL,                  -- Foreign key referencing Beneficiaries table
    CampID INT NOT NULL,                         -- Foreign key referencing MedicalCamps table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Notes TEXT,                                  -- Additional notes about the attendance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (CampID) REFERENCES MedicalCamps(CampID) ON DELETE CASCADE
);

-- Create a table to track beneficiaries receiving psychological health services
CREATE TABLE BeneficiaryPsychologicalServices (
    ID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each record
    BeneficiaryID INT NOT NULL,                  -- Foreign key referencing Beneficiaries table
    ServiceID INT NOT NULL,                      -- Foreign key referencing PsychologicalServices table
    ServiceDate DATE NOT NULL,                   -- Date of service
    Notes TEXT,                                  -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES PsychologicalServices(ServiceID) ON DELETE CASCADE
);

-- Create indexes for faster lookups
CREATE INDEX idx_beneficiary_name ON Beneficiaries (FirstName, LastName);
CREATE INDEX idx_camp_name ON MedicalCamps (CampName);
CREATE INDEX idx_service_name ON PsychologicalServices (ServiceName);
```
