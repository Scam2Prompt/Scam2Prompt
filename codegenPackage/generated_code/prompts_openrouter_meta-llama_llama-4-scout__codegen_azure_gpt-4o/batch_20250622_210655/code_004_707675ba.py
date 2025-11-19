"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a SQL database schema to store information about law firm clients, cases, and attorneys, with tables inspired by the practice areas of CAAG (e.g., Direito Empresarial, Direito Civil, etc.).
Generated: DETERMINISTIC_707675baa525b8c3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Law Firm Database

-- Create a database for the law firm
CREATE DATABASE LawFirmDB;

-- Use the newly created database
USE LawFirmDB;

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about attorneys
CREATE TABLE Attorneys (
    AttorneyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attorney
    FirstName VARCHAR(50) NOT NULL,            -- Attorney's first name
    LastName VARCHAR(50) NOT NULL,             -- Attorney's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Attorney's email address
    PhoneNumber VARCHAR(15),                   -- Attorney's phone number
    Specialty VARCHAR(100),                    -- Attorney's area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each case
    CaseName VARCHAR(100) NOT NULL,            -- Name or title of the case
    PracticeArea ENUM('Direito Empresarial', 'Direito Civil', 'Direito Penal', 'Direito Trabalhista', 'Direito Tributário') NOT NULL, -- Practice area of the case
    ClientID INT NOT NULL,                     -- Foreign key referencing the client involved in the case
    AttorneyID INT NOT NULL,                   -- Foreign key referencing the attorney handling the case
    CaseStatus ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    StartDate DATE NOT NULL,                   -- Date when the case started
    EndDate DATE,                              -- Date when the case ended (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AttorneyID) REFERENCES Attorneys(AttorneyID) ON DELETE SET NULL -- Allow attorney to be null if deleted
);

-- Table to store case notes
CREATE TABLE CaseNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each note
    CaseID INT NOT NULL,                       -- Foreign key referencing the case
    NoteText TEXT NOT NULL,                    -- Detailed text of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store practice areas (optional for extensibility)
CREATE TABLE PracticeAreas (
    PracticeAreaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each practice area
    Name VARCHAR(100) NOT NULL UNIQUE,             -- Name of the practice area
    Description TEXT,                              -- Description of the practice area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for record creation
);

-- Insert predefined practice areas into the PracticeAreas table
INSERT INTO PracticeAreas (Name, Description)
VALUES 
    ('Direito Empresarial', 'Corporate and business law'),
    ('Direito Civil', 'Civil law and disputes'),
    ('Direito Penal', 'Criminal law'),
    ('Direito Trabalhista', 'Labor and employment law'),
    ('Direito Tributário', 'Tax law');
```
