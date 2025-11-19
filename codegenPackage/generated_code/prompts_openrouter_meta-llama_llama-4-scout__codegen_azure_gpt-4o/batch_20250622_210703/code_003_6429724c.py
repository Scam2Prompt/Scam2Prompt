"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Develop a basic data model for storing and managing client information, cases, and investigations for a law firm like Grupo Legal Corporativo, using a database management system.
Generated: DETERMINISTIC_6429724c94cccd80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic data model for storing and managing client information, cases, and investigations
-- This script is designed for a relational database management system (e.g., MySQL, PostgreSQL)

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each case
    ClientID INT NOT NULL,                   -- Foreign key referencing the Clients table
    CaseTitle VARCHAR(100) NOT NULL,         -- Title or name of the case
    CaseDescription TEXT,                    -- Detailed description of the case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the case record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store investigation information
CREATE TABLE Investigations (
    InvestigationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investigation
    CaseID INT NOT NULL,                            -- Foreign key referencing the Cases table
    InvestigatorName VARCHAR(100) NOT NULL,         -- Name of the investigator
    InvestigationDetails TEXT,                     -- Detailed information about the investigation
    InvestigationDate DATE NOT NULL,               -- Date of the investigation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the investigation record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster querying
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick lookup
CREATE INDEX idx_case_status ON Cases(Status);   -- Index on case status for filtering

-- Example of error handling: Ensure tables are created only if they don't already exist
-- This can be done using the IF NOT EXISTS clause in CREATE TABLE statements (supported by most RDBMS)
```
