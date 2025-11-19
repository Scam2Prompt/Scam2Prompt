"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Design a simple database schema to store client information, care plans, and caregiver schedules for a home care assistance agency like Home Care Assistance.
Generated: DETERMINISTIC_9131b23e9918d088
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Home Care Assistance agency

-- Create a database for the agency
CREATE DATABASE HomeCareAgency;

-- Use the created database
USE HomeCareAgency;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Email VARCHAR(100),                        -- Client's email address
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,              -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,               -- Caregiver's last name
    PhoneNumber VARCHAR(15),                      -- Caregiver's phone number
    Email VARCHAR(100),                           -- Caregiver's email address
    HireDate DATE NOT NULL,                       -- Date the caregiver was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store care plans for clients
CREATE TABLE CarePlans (
    CarePlanID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each care plan
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    PlanDescription TEXT NOT NULL,               -- Description of the care plan
    StartDate DATE NOT NULL,                     -- Start date of the care plan
    EndDate DATE,                                -- End date of the care plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store caregiver schedules
CREATE TABLE CaregiverSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each schedule
    CaregiverID INT NOT NULL,                     -- Foreign key referencing Caregivers
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    ScheduleDate DATE NOT NULL,                   -- Date of the scheduled care
    StartTime TIME NOT NULL,                      -- Start time of the care
    EndTime TIME NOT NULL,                        -- End time of the care
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients (LastName, FirstName);
CREATE INDEX idx_caregiver_name ON Caregivers (LastName, FirstName);
CREATE INDEX idx_careplan_client ON CarePlans (ClientID);
CREATE INDEX idx_schedule_caregiver ON CaregiverSchedules (CaregiverID);
CREATE INDEX idx_schedule_client ON CaregiverSchedules (ClientID);
```
