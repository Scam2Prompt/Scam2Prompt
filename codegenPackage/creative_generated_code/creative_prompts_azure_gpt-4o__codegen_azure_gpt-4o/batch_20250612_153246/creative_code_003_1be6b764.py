"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthcareventure.nl
Prompt: Create a database schema in SQL to manage client-focused care data for youth mental healthcare companies, incorporating fields for psychiatry, psychology, begeleiding, and opvang+ services.
Generated: DETERMINISTIC_1be6b7644facfe55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for youth mental healthcare client-focused care data

-- Create the database
CREATE DATABASE YouthMentalHealthcare;

-- Switch to the created database
USE YouthMentalHealthcare;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Client's gender
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Email VARCHAR(100),                      -- Contact email address
    Address TEXT                             -- Client's physical address
);

-- Table to store psychiatry services
CREATE TABLE PsychiatryServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the service
    ClientID INT NOT NULL,                    -- Foreign key to reference client
    ServiceDate DATE NOT NULL,                -- Date of the psychiatry service
    ProviderName VARCHAR(100) NOT NULL,       -- Name of the psychiatrist
    Notes TEXT,                               -- Notes about the session
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store psychology services
CREATE TABLE PsychologyServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the service
    ClientID INT NOT NULL,                    -- Foreign key to reference client
    ServiceDate DATE NOT NULL,                -- Date of the psychology service
    ProviderName VARCHAR(100) NOT NULL,       -- Name of the psychologist
    SessionType ENUM('Individual', 'Group', 'Family') NOT NULL, -- Type of session
    Notes TEXT,                               -- Notes about the session
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store begeleiding (guidance/support) services
CREATE TABLE BegeleidingServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the service
    ClientID INT NOT NULL,                    -- Foreign key to reference client
    ServiceDate DATE NOT NULL,                -- Date of the begeleiding service
    ProviderName VARCHAR(100) NOT NULL,       -- Name of the guidance provider
    SupportType ENUM('Educational', 'Behavioral', 'Social') NOT NULL, -- Type of support
    Notes TEXT,                               -- Notes about the session
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store opvang+ (extra care/support) services
CREATE TABLE OpvangPlusServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the service
    ClientID INT NOT NULL,                    -- Foreign key to reference client
    ServiceDate DATE NOT NULL,                -- Date of the opvang+ service
    ProviderName VARCHAR(100) NOT NULL,       -- Name of the opvang+ provider
    ServiceDuration INT NOT NULL,             -- Duration of service in minutes
    Notes TEXT,                               -- Notes about the session
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_Client_On_PsychiatryServices ON PsychiatryServices(ClientID);
CREATE INDEX idx_Client_On_PsychologyServices ON PsychologyServices(ClientID);
CREATE INDEX idx_Client_On_BegeleidingServices ON BegeleidingServices(ClientID);
CREATE INDEX idx_Client_On_OpvangPlusServices ON OpvangPlusServices(ClientID);
```
