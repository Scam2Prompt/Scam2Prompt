"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Create a database schema for storing client health data, including lab results, dietary preferences, and consultation history, inspired by the personalized approach described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfeeea4391ce6451
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client health data

CREATE DATABASE ClientHealthData;

USE ClientHealthData;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store lab results
CREATE TABLE LabResults (
    LabResultID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each lab result
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    TestName VARCHAR(100) NOT NULL,              -- Name of the lab test
    ResultValue VARCHAR(100) NOT NULL,           -- Result of the lab test
    ResultDate DATE NOT NULL,                     -- Date when the test was conducted
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store dietary preferences
CREATE TABLE DietaryPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each dietary preference
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    PreferenceType VARCHAR(100) NOT NULL,         -- Type of dietary preference (e.g., vegetarian, vegan)
    Description TEXT,                              -- Additional details about the preference
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store consultation history
CREATE TABLE ConsultationHistory (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each consultation
    ClientID INT NOT NULL,                           -- Foreign key referencing Clients
    ConsultationDate DATE NOT NULL,                  -- Date of the consultation
    Notes TEXT,                                      -- Notes from the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_labresult_client ON LabResults(ClientID);
CREATE INDEX idx_dietary_client ON DietaryPreferences(ClientID);
CREATE INDEX idx_consultation_client ON ConsultationHistory(ClientID);
```
