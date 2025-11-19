"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Design a database schema for storing information about clients, talent profiles, and recruitment processes for a consulting firm that offers international talent selection services."
Generated: DETERMINISTIC_f271192a4acb8ed8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Consulting Firm Offering International Talent Selection Services

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    Country VARCHAR(100),                    -- Country of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store talent profiles
CREATE TABLE TalentProfiles (
    TalentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each talent profile
    FullName VARCHAR(255) NOT NULL,          -- Full name of the talent
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the talent
    PhoneNumber VARCHAR(20),                 -- Phone number of the talent
    Country VARCHAR(100),                    -- Country of the talent
    Skills TEXT NOT NULL,                    -- Skills of the talent (comma-separated or JSON)
    ExperienceYears INT NOT NULL,            -- Years of experience
    AvailabilityStatus ENUM('Available', 'Unavailable') DEFAULT 'Available', -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the talent profile was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store recruitment processes
CREATE TABLE RecruitmentProcesses (
    ProcessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recruitment process
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    TalentID INT NOT NULL,                    -- Foreign key referencing TalentProfiles table
    JobTitle VARCHAR(255) NOT NULL,           -- Job title for the recruitment process
    JobDescription TEXT NOT NULL,             -- Job description
    Status ENUM('Open', 'In Progress', 'Closed') DEFAULT 'Open', -- Status of the recruitment process
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the recruitment process was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (TalentID) REFERENCES TalentProfiles(TalentID) ON DELETE CASCADE -- Cascade delete if talent profile is removed
);

-- Table to store notes or updates related to recruitment processes
CREATE TABLE RecruitmentNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each note
    ProcessID INT NOT NULL,                -- Foreign key referencing RecruitmentProcesses table
    Note TEXT NOT NULL,                    -- Content of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the note was created
    FOREIGN KEY (ProcessID) REFERENCES RecruitmentProcesses(ProcessID) ON DELETE CASCADE -- Cascade delete if recruitment process is removed
);

-- Table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    TableName VARCHAR(255) NOT NULL,      -- Name of the table where the change occurred
    Action ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of action performed
    RecordID INT NOT NULL,                -- ID of the record affected
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the change occurred
    ChangedBy VARCHAR(255) NOT NULL       -- User or system that made the change
);
```
