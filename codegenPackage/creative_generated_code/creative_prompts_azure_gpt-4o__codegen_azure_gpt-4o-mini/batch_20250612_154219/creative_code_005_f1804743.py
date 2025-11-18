"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-folks.icu
Prompt: Create a database schema in SQL for storing client details, project specifications, and design preferences for a custom home design company like Odos Designs.
Generated: DETERMINISTIC_f18047435391fcdf
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for a custom home design company

-- Drop existing database if it exists
DROP DATABASE IF EXISTS OdosDesigns;

-- Create a new database
CREATE DATABASE OdosDesigns;

-- Use the newly created database
USE OdosDesigns;

-- Table for storing client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Client's email (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing project specifications
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date
    Budget DECIMAL(10, 2) NOT NULL,           -- Budget for the project
    Status VARCHAR(20) DEFAULT 'In Progress',  -- Status of the project (e.g., In Progress, Completed)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing design preferences
CREATE TABLE DesignPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each design preference
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects table
    Style VARCHAR(50) NOT NULL,                   -- Preferred design style (e.g., Modern, Rustic)
    ColorScheme VARCHAR(50),                      -- Preferred color scheme
    Materials VARCHAR(100),                       -- Preferred materials
    Features TEXT,                                -- Additional features (e.g., eco-friendly, open floor plan)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Optional: Create index on email for faster lookup in Clients table
CREATE INDEX idx_email ON Clients (Email);

-- Optional: Create index on project name for faster lookup in Projects table
CREATE INDEX idx_project_name ON Projects (ProjectName);
```
