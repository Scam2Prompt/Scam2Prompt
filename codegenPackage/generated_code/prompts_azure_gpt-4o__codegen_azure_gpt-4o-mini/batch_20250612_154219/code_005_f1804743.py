"""
Generated Code Metadata:
========================
Original URL: https://app-folks.icu
Prompt: Create a database schema in SQL for storing client details, project specifications, and design preferences for a custom home design company like Odos Designs.
Generated: DETERMINISTIC_f18047435391fcdf
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a custom home design company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS DesignPreferences;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                         -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project specifications
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (nullable)
    Budget DECIMAL(10, 2) NOT NULL,           -- Project budget
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',  -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store design preferences
CREATE TABLE DesignPreferences (
    PreferenceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each preference
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects
    Style VARCHAR(50) NOT NULL,                   -- Preferred design style (e.g., Modern, Traditional)
    ColorScheme VARCHAR(50),                       -- Preferred color scheme
    Materials TEXT,                                -- Preferred materials (e.g., Wood, Stone)
    Features TEXT,                                 -- Special features (e.g., Open floor plan, Energy-efficient)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes can be added for performance optimization if necessary
-- Example: CREATE INDEX idx_client_email ON Clients(Email);
```
