"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azarlegal.com
Prompt: Create a sample database schema for storing client information and case details for a law firm like AZAR & Associates, focusing on corporate and real estate law.
Generated: DETERMINISTIC_e192d70186bb480f
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for AZAR & Associates law firm
-- This schema is designed to store client information and case details 
-- specifically for corporate and real estate law.

CREATE DATABASE LawFirmDB;

USE LawFirmDB;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- First name of the client
    LastName VARCHAR(50) NOT NULL,           -- Last name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address of the client
    Phone VARCHAR(15),                        -- Phone number of the client
    Address VARCHAR(255),                     -- Address of the client
    CompanyName VARCHAR(100),                 -- Company name (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store case details
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    CaseType ENUM('Corporate', 'Real Estate') NOT NULL, -- Type of case
    CaseDescription TEXT NOT NULL,             -- Description of the case
    Status ENUM('Open', 'In Progress', 'Closed') DEFAULT 'Open', -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Case creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Case update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures client deletion cascades to cases
);

-- Table to store case documents
CREATE TABLE CaseDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    CaseID INT NOT NULL,                       -- Foreign key referencing Cases table
    DocumentName VARCHAR(255) NOT NULL,       -- Name of the document
    DocumentPath VARCHAR(255) NOT NULL,       -- File path to the document
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Document upload timestamp
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensures case deletion cascades to documents
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each billing record
    CaseID INT NOT NULL,                       -- Foreign key referencing Cases table
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount billed
    BillingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of billing
    Status ENUM('Paid', 'Unpaid', 'Pending') DEFAULT 'Unpaid', -- Billing status
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensures case deletion cascades to billing records
);

-- Ensure necessary indexes for performance
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_case_client ON Cases (ClientID);
CREATE INDEX idx_document_case ON CaseDocuments (CaseID);
CREATE INDEX idx_billing_case ON Billing (CaseID);
```
