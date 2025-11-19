"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Design a database schema for storing client information, treatment plans, and session records for a therapy center with a unique approach like Reset Terapias e Movimento."
Generated: DETERMINISTIC_a8fac8ff8fba056d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a therapy center

-- Create a database for the therapy center
CREATE DATABASE TherapyCenter;

-- Use the created database
USE TherapyCenter;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,                -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    PlanDescription TEXT NOT NULL,                  -- Description of the treatment plan
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE,                                   -- End date of the treatment plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store session records
CREATE TABLE SessionRecords (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each session
    TreatmentPlanID INT NOT NULL,                  -- Foreign key referencing TreatmentPlans
    SessionDate DATE NOT NULL,                     -- Date of the session
    Duration INT NOT NULL,                         -- Duration of the session in minutes
    Notes TEXT,                                    -- Notes from the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_treatmentplan_client ON TreatmentPlans(ClientID);
CREATE INDEX idx_session_treatmentplan ON SessionRecords(TreatmentPlanID);
```
