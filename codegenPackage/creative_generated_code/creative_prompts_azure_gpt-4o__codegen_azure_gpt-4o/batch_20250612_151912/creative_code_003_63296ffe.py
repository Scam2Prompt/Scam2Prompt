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
-- Database Schema: Law Firm Case Management

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE,                        -- Client's date of birth
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Table: Cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each case
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    CaseType ENUM('Family', 'Criminal') NOT NULL, -- Type of case: Family or Criminal
    CaseDetails TEXT NOT NULL,               -- Detailed description of case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    OpenedDate DATE NOT NULL,                -- Date when the case was opened
    ClosedDate DATE,                         -- Date when the case was closed (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures client deletion cascades to cases
);

-- Table: Resolutions
CREATE TABLE Resolutions (
    ResolutionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resolution
    CaseID INT NOT NULL,                         -- Foreign key referencing Cases table
    ResolutionType ENUM('Mediation', 'Judicial Representation', 'Settlement') NOT NULL, -- Type of resolution
    ResolutionDetails TEXT,                      -- Detailed description of the resolution
    ResolutionDate DATE NOT NULL,                -- Date of resolution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensures case deletion cascades to resolutions
);

-- Indexes for optimization
CREATE INDEX idx_client_name ON Clients(FirstName, LastName); -- Index for faster client name searches
CREATE INDEX idx_case_status ON Cases(Status); -- Index for filtering cases by status
CREATE INDEX idx_resolution_type ON Resolutions(ResolutionType); -- Index for filtering resolutions by type
```
