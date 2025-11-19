"""
Generated Code Metadata:
========================
Original URL: https://azarlegal.com
Prompt: Create a sample database schema for storing client information and case details for a law firm like AZAR & Associates, focusing on corporate and real estate law.
Generated: DETERMINISTIC_e192d70186bb480f
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AZAR & Associates Law Firm
-- This schema is designed to store client information and case details
-- focusing on corporate and real estate law.

-- Create a database for the law firm
CREATE DATABASE AZAR_Associates;

-- Use the created database
USE AZAR_Associates;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store case details
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    CaseType ENUM('Corporate', 'Real Estate') NOT NULL,  -- Type of case
    CaseDescription TEXT,                      -- Description of the case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open',  -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store case notes
CREATE TABLE CaseNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each note
    CaseID INT NOT NULL,                        -- Foreign key referencing Cases table
    Note TEXT NOT NULL,                         -- Content of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each billing record
    CaseID INT NOT NULL,                        -- Foreign key referencing Cases table
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount billed
    BillingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of billing
    PaymentStatus ENUM('Paid', 'Unpaid', 'Pending') DEFAULT 'Unpaid',  -- Payment status
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional)
-- INSERT INTO Clients (FirstName, LastName, Email, Phone, Address) VALUES
-- ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, City, State, ZIP'),
-- ('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321', '456 Elm St, City, State, ZIP');

-- INSERT INTO Cases (ClientID, CaseType, CaseDescription) VALUES
-- (1, 'Corporate', 'Corporate merger and acquisition case'),
-- (2, 'Real Estate', 'Real estate property dispute case');

-- INSERT INTO CaseNotes (CaseID, Note) VALUES
-- (1, 'Initial consultation held on 2023-01-01.'),
-- (2, 'Client provided additional documents on 2023-01-05.');

-- INSERT INTO Billing (CaseID, Amount, PaymentStatus) VALUES
-- (1, 1500.00, 'Unpaid'),
-- (2, 2000.00, 'Paid');
```
