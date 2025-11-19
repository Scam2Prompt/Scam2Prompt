"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Describe how to create a database schema for managing health records in a SUS-based healthcare system, including tables for patients, health professionals, and services.
Generated: DETERMINISTIC_79540de79ff6728e
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing health records in a SUS-based healthcare system.

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FullName VARCHAR(255) NOT NULL,           -- Full name of the patient
    DateOfBirth DATE NOT NULL,                -- Date of birth of the patient
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    CPF CHAR(11) UNIQUE NOT NULL,             -- CPF (Brazilian tax identifier) of the patient
    Address TEXT,                             -- Address of the patient
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(255),                       -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store health professional information
CREATE TABLE HealthProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each health professional
    FullName VARCHAR(255) NOT NULL,                 -- Full name of the health professional
    RegistrationNumber VARCHAR(50) UNIQUE NOT NULL, -- Professional license number (e.g., CRM)
    Specialization VARCHAR(100),                   -- Area of specialization
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Email VARCHAR(255),                            -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered to patients
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each service
    PatientID INT NOT NULL,                        -- Foreign key to the Patients table
    ProfessionalID INT NOT NULL,                   -- Foreign key to the HealthProfessionals table
    ServiceType VARCHAR(255) NOT NULL,             -- Type or description of the service provided
    ServiceDate TIMESTAMP NOT NULL,                -- Date and time of the service
    Notes TEXT,                                    -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (ProfessionalID) REFERENCES HealthProfessionals(ProfessionalID) ON DELETE CASCADE -- Cascade delete if professional is removed
);

-- Ensure the database is created with proper constraints.
-- Add indexes for performance on frequently queried columns.

CREATE INDEX idx_Patient_CPF ON Patients(CPF); -- Index for quick lookup by CPF
CREATE INDEX idx_Professional_RegNum ON HealthProfessionals(RegistrationNumber); -- Index for quick lookup by registration number
CREATE INDEX idx_Service_Date ON Services(ServiceDate); -- Index for quick lookup by service date
```
