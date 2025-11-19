"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema in SQL to manage the records of beneficiaries receiving support from the Rakhshanda Memorial's medical camps and psychological health services.
Generated: DETERMINISTIC_54d4628dca4aeffc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing beneficiaries of Rakhshanda Memorial's services

-- Table to store beneficiary details
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    FullName VARCHAR(100) NOT NULL,              -- Full name of the beneficiary
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the beneficiary
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the beneficiary
    ContactNumber VARCHAR(15),                   -- Contact number (optional)
    EmailAddress VARCHAR(100),                   -- Email address (optional)
    Address TEXT,                                -- Residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store medical camp details
CREATE TABLE MedicalCamps (
    CampID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each medical camp
    CampName VARCHAR(100) NOT NULL,              -- Name of the medical camp
    Location VARCHAR(255) NOT NULL,              -- Location of the medical camp
    StartDate DATE NOT NULL,                     -- Start date of the medical camp
    EndDate DATE NOT NULL,                       -- End date of the medical camp
    OrganizerName VARCHAR(100),                  -- Name of the organizer (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store psychological health service details
CREATE TABLE PsychologicalServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each psychological service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the psychological service
    Description TEXT,                            -- Description of the service
    ServiceProvider VARCHAR(100),                -- Name of the service provider (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to manage beneficiaries attending medical camps
CREATE TABLE BeneficiaryMedicalCampRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the record
    BeneficiaryID INT NOT NULL,                  -- Foreign key to Beneficiaries table
    CampID INT NOT NULL,                         -- Foreign key to MedicalCamps table
    AttendanceDate DATE NOT NULL,                -- Date the beneficiary attended the camp
    Notes TEXT,                                  -- Additional notes about the beneficiary's participation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (CampID) REFERENCES MedicalCamps(CampID) ON DELETE CASCADE
);

-- Table to manage beneficiaries receiving psychological health services
CREATE TABLE BeneficiaryPsychologicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the record
    BeneficiaryID INT NOT NULL,                  -- Foreign key to Beneficiaries table
    ServiceID INT NOT NULL,                      -- Foreign key to PsychologicalServices table
    SessionDate DATE NOT NULL,                   -- Date the beneficiary received the service
    Notes TEXT,                                  -- Additional notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES PsychologicalServices(ServiceID) ON DELETE CASCADE
);

-- Table to store audit logs for tracking changes in the database
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the log
    TableName VARCHAR(100) NOT NULL,             -- Name of the table where the change occurred
    OperationType ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation
    ChangedRecordID INT NOT NULL,                -- ID of the record that was changed
    ChangeTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the change
    User VARCHAR(100) NOT NULL                   -- User who performed the operation
);
```
