"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Based on the information provided about Pérez Bernalte Abogados' services in criminal law, civil law, and administrative law, create a simple database schema to organize client cases by legal area.
Generated: DETERMINISTIC_8d792c79b601b30d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for organizing client cases by legal area for Pérez Bernalte Abogados

-- Create a database for the law firm
CREATE DATABASE PerezBernalteAbogados;

-- Use the created database
USE PerezBernalteAbogados;

-- Table to store legal areas
CREATE TABLE LegalAreas (
    AreaID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each legal area
    AreaName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the legal area (e.g., Criminal Law, Civil Law, Administrative Law)
    Description TEXT                         -- Description of the legal area
);

-- Table to store clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the client was added
);

-- Table to store cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key referencing the Clients table
    AreaID INT NOT NULL,                       -- Foreign key referencing the LegalAreas table
    CaseDescription TEXT NOT NULL,             -- Description of the case
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL,  -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the case was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensures client deletion cascades to cases
    FOREIGN KEY (AreaID) REFERENCES LegalAreas(AreaID) ON DELETE CASCADE  -- Ensures legal area deletion cascades to cases
);

-- Insert sample legal areas
INSERT INTO LegalAreas (AreaName, Description) VALUES
('Criminal Law', 'Legal area dealing with crimes and their punishments.'),
('Civil Law', 'Legal area dealing with disputes between individuals or organizations.'),
('Administrative Law', 'Legal area governing the activities of administrative agencies.');

-- Sample query to retrieve all cases with client information and legal area
SELECT 
    c.FirstName,
    c.LastName,
    la.AreaName,
    cs.CaseDescription,
    cs.Status,
    cs.CreatedAt
FROM 
    Cases cs
JOIN 
    Clients c ON cs.ClientID = c.ClientID
JOIN 
    LegalAreas la ON cs.AreaID = la.AreaID;
```
