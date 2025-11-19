"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Design a database schema for storing client information and accident details for a personal injury law firm, ensuring it includes fields for various accident types and client contact methods.
Generated: DETERMINISTIC_769a9dba55fc72dc
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing client information and accident details
-- This schema is designed for a personal injury law firm

-- Create table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- First name of the client
    LastName VARCHAR(50) NOT NULL,           -- Last name of the client
    DateOfBirth DATE,                        -- Date of birth of the client
    Email VARCHAR(100),                      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client (international formats supported)
    Address TEXT,                            -- Physical address of the client
    PreferredContactMethod ENUM('Email', 'Phone', 'Postal') DEFAULT 'Email', -- Preferred contact method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for storing accident details
CREATE TABLE Accidents (
    AccidentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accident
    ClientID INT NOT NULL,                     -- Foreign key linking to the client
    AccidentDate DATE NOT NULL,                -- Date of the accident
    AccidentType ENUM('Car Accident', 'Slip and Fall', 'Workplace Injury', 'Medical Malpractice', 'Other') NOT NULL, -- Type of accident
    Description TEXT,                          -- Detailed description of the accident
    Location TEXT,                             -- Location where the accident occurred
    SeverityLevel ENUM('Low', 'Moderate', 'High') NOT NULL, -- Severity of the accident
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create table for storing client contact methods (optional, for more flexibility)
CREATE TABLE ContactMethods (
    ContactMethodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contact method
    ClientID INT NOT NULL,                          -- Foreign key linking to the client
    ContactType ENUM('Email', 'Phone', 'Postal') NOT NULL, -- Type of contact
    ContactDetail VARCHAR(100) NOT NULL,           -- Contact detail (email address, phone number, or postal address)
    IsPreferred BOOLEAN DEFAULT FALSE,            -- Indicates if this is the preferred contact method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Ensure database supports UTF-8 for proper international text handling
ALTER DATABASE my_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Indexes for optimization (optional, depending on query patterns)
CREATE INDEX idx_client_name ON Clients(LastName, FirstName);
CREATE INDEX idx_accident_client ON Accidents(ClientID);
```
