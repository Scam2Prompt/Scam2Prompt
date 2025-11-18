"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Create a database schema for storing polygraph test results, including fields for test type, client details, and examiner credentials, inspired by the services offered by Euro Poligraf Center.
Generated: DETERMINISTIC_981759143af875da
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing polygraph test results
-- This schema includes tables for clients, examiners, test types, and test results.

-- Table for storing client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the client
    FullName VARCHAR(100) NOT NULL,                 -- Full name of the client
    DateOfBirth DATE NOT NULL,                      -- Date of birth of the client
    PhoneNumber VARCHAR(15),                        -- Contact phone number
    Email VARCHAR(100),                             -- Contact email address
    Address TEXT,                                   -- Residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table for storing examiner credentials
CREATE TABLE Examiners (
    ExaminerID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the examiner
    FullName VARCHAR(100) NOT NULL,                 -- Full name of the examiner
    CertificationNumber VARCHAR(50) NOT NULL,       -- Certification number of the examiner
    YearsOfExperience INT NOT NULL,                 -- Number of years of experience
    Specialization VARCHAR(100),                   -- Specialization (e.g., criminal cases, corporate disputes)
    PhoneNumber VARCHAR(15),                        -- Contact phone number
    Email VARCHAR(100),                             -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table for storing test types
CREATE TABLE TestTypes (
    TestTypeID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the test type
    TestName VARCHAR(100) NOT NULL,                 -- Name of the test type (e.g., lie detection, forensic analysis)
    Description TEXT,                               -- Description of the test type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table for storing polygraph test results
CREATE TABLE PolygraphTests (
    TestID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for the polygraph test
    ClientID INT NOT NULL,                          -- Foreign key referencing the client who took the test
    ExaminerID INT NOT NULL,                        -- Foreign key referencing the examiner conducting the test
    TestTypeID INT NOT NULL,                        -- Foreign key referencing the type of test conducted
    TestDate DATE NOT NULL,                         -- Date when the test was conducted
    Result VARCHAR(50) NOT NULL,                   -- Result of the test (e.g., truthful, deceptive)
    Notes TEXT,                                    -- Additional notes or observations from the examiner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,       -- Cascade deletion for client data
    FOREIGN KEY (ExaminerID) REFERENCES Examiners(ExaminerID) ON DELETE CASCADE, -- Cascade deletion for examiner data
    FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID) ON DELETE CASCADE  -- Cascade deletion for test type data
);

-- Index for faster search on PolygraphTests table
CREATE INDEX idx_test_date ON PolygraphTests (TestDate);
```
