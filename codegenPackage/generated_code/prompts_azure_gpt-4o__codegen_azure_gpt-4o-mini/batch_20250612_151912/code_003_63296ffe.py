"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Create a database schema for managing client cases in a law firm specializing in family law and criminal law, including tables for client information, case details, and modes of resolution (e.g., mediation, judicial representation) inspired by Majeli Avocat's practices.
Generated: DETERMINISTIC_63296ffeaac75f95
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client cases in a law firm specializing in family law and criminal law

-- Create a database for the law firm
CREATE DATABASE LawFirmDB;

-- Use the created database
USE LawFirmDB;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    Phone VARCHAR(15),                       -- Client's phone number
    Address VARCHAR(255),                     -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store case details
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    CaseType ENUM('Family Law', 'Criminal Law') NOT NULL, -- Type of case
    CaseDescription TEXT NOT NULL,             -- Description of the case
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL, -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store modes of resolution
CREATE TABLE Resolutions (
    ResolutionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resolution method
    CaseID INT NOT NULL,                          -- Foreign key referencing Cases table
    ResolutionType ENUM('Mediation', 'Judicial Representation', 'Negotiation', 'Arbitration') NOT NULL, -- Type of resolution
    ResolutionDetails TEXT,                       -- Details about the resolution
    ResolvedAt TIMESTAMP,                        -- Timestamp when the case was resolved
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_resolution_case ON Resolutions(CaseID);
```
