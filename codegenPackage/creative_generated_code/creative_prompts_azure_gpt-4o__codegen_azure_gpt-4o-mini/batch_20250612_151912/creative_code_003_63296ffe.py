"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Create a database schema for managing client cases in a law firm specializing in family law and criminal law, including tables for client information, case details, and modes of resolution (e.g., mediation, judicial representation) inspired by Majeli Avocat's practices.
Generated: DETERMINISTIC_63296ffeaac75f95
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client cases in a law firm specializing in family law and criminal law

-- Drop existing tables if they exist for a clean setup
DROP TABLE IF EXISTS ModesOfResolution;
DROP TABLE IF EXISTS Cases;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID SERIAL PRIMARY KEY,           -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,       -- Client's first name
    LastName VARCHAR(50) NOT NULL,        -- Client's last name
    DateOfBirth DATE,                      -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Client's email address
    Phone VARCHAR(15),                     -- Client's phone number
    Address VARCHAR(255),                  -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store case details
CREATE TABLE Cases (
    CaseID SERIAL PRIMARY KEY,             -- Unique identifier for each case
    ClientID INT NOT NULL,                 -- Foreign key reference to Clients table
    CaseType VARCHAR(50) NOT NULL,         -- Type of case (e.g., family law, criminal law)
    CaseDescription TEXT NOT NULL,         -- Description of the case
    StartDate DATE NOT NULL,               -- Case start date
    EndDate DATE,                          -- Case end date
    Status VARCHAR(20) NOT NULL,           -- Current status of the case (e.g., active, closed)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Handle client deletion
);

-- Table to store modes of resolution
CREATE TABLE ModesOfResolution (
    ResolutionID SERIAL PRIMARY KEY,       -- Unique identifier for each resolution mode
    CaseID INT NOT NULL,                   -- Foreign key reference to Cases table
    ResolutionType VARCHAR(50) NOT NULL,   -- Type of resolution (e.g., mediation, judicial representation)
    ResolutionDate DATE,                   -- Date the resolution took place
    Notes TEXT,                            -- Additional notes about the resolution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Handle case deletion
);

-- Optional: Indexes for optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_resolution_case ON ModesOfResolution(CaseID);
```
