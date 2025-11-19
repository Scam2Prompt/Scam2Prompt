"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Design a basic database schema to store information gathered during forensic investigations, including evidence and case details."
Generated: DETERMINISTIC_4fceb0bb900e5f27
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for forensic investigations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Evidence;
DROP TABLE IF EXISTS Cases;
DROP TABLE IF EXISTS Investigators;

-- Create a table to store case details
CREATE TABLE Cases (
    CaseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each case
    CaseNumber VARCHAR(50) NOT NULL,        -- Unique case number
    CaseDescription TEXT,                    -- Description of the case
    DateOpened DATETIME NOT NULL,            -- Date when the case was opened
    DateClosed DATETIME,                     -- Date when the case was closed (nullable)
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL,  -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store evidence details
CREATE TABLE Evidence (
    EvidenceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each piece of evidence
    CaseID INT NOT NULL,                         -- Foreign key referencing the Cases table
    EvidenceDescription TEXT NOT NULL,           -- Description of the evidence
    EvidenceType VARCHAR(100) NOT NULL,         -- Type of evidence (e.g., DNA, fingerprint)
    DateCollected DATETIME NOT NULL,            -- Date when the evidence was collected
    LocationCollected VARCHAR(255),              -- Location where the evidence was collected
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store investigator details
CREATE TABLE Investigators (
    InvestigatorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each investigator
    FirstName VARCHAR(100) NOT NULL,               -- Investigator's first name
    LastName VARCHAR(100) NOT NULL,                 -- Investigator's last name
    BadgeNumber VARCHAR(50) UNIQUE NOT NULL,        -- Unique badge number for the investigator
    ContactInfo VARCHAR(255),                       -- Contact information for the investigator
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a junction table to associate investigators with cases
CREATE TABLE CaseInvestigators (
    CaseID INT NOT NULL,                           -- Foreign key referencing the Cases table
    InvestigatorID INT NOT NULL,                   -- Foreign key referencing the Investigators table
    PRIMARY KEY (CaseID, InvestigatorID),         -- Composite primary key
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (InvestigatorID) REFERENCES Investigators(InvestigatorID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes can be added for performance optimization as needed
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_evidence_case ON Evidence(CaseID);
CREATE INDEX idx_investigator_lastname ON Investigators(LastName);
```
