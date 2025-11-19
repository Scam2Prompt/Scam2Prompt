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
-- Database schema for organizing client cases by legal area

-- Create a table to store information about legal areas
CREATE TABLE LegalAreas (
    LegalAreaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each legal area
    Name VARCHAR(100) NOT NULL,                 -- Name of the legal area (e.g., Criminal Law, Civil Law, Administrative Law)
    Description TEXT                            -- Optional description of the legal area
);

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,            -- Client's first name
    LastName VARCHAR(100) NOT NULL,             -- Client's last name
    Email VARCHAR(255) UNIQUE,                  -- Client's email address (must be unique)
    PhoneNumber VARCHAR(20),                    -- Client's phone number
    Address TEXT                                -- Client's address
);

-- Create a table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each case
    ClientID INT NOT NULL,                      -- Foreign key referencing the client associated with the case
    LegalAreaID INT NOT NULL,                   -- Foreign key referencing the legal area of the case
    CaseTitle VARCHAR(255) NOT NULL,            -- Title or name of the case
    CaseDescription TEXT,                       -- Detailed description of the case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the case was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the case was last updated
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (LegalAreaID) REFERENCES LegalAreas(LegalAreaID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert predefined legal areas
INSERT INTO LegalAreas (Name, Description)
VALUES 
    ('Criminal Law', 'Legal services related to criminal cases and defense.'),
    ('Civil Law', 'Legal services related to civil disputes and contracts.'),
    ('Administrative Law', 'Legal services related to administrative and regulatory matters.');
```
