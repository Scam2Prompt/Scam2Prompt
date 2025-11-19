"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: "Create a SQL database schema to store information about home remodeling projects, including client details, project scope, and installation schedules, inspired by the services provided by 1Marble Classic."
Generated: DETERMINISTIC_7efab76a85425d13
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Home Remodeling Projects inspired by 1Marble Classic

-- Create a table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    ProjectScope TEXT NOT NULL,               -- Detailed description of the project scope
    Budget DECIMAL(10, 2),                    -- Estimated budget for the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table to store installation schedules
CREATE TABLE InstallationSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    InstallationDate DATE NOT NULL,            -- Date of installation
    InstallerName VARCHAR(100),                -- Name of the installer
    InstallationDetails TEXT,                  -- Details about the installation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Create indexes for faster lookups
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick client lookup
CREATE INDEX idx_project_status ON Projects(Status); -- Index on project status for filtering
CREATE INDEX idx_schedule_date ON InstallationSchedules(InstallationDate); -- Index on installation date for scheduling

-- Error handling and constraints
-- Ensure email format is valid (example constraint for demonstration purposes)
ALTER TABLE Clients ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%@%.%');

-- Ensure budget is non-negative
ALTER TABLE Projects ADD CONSTRAINT chk_budget_non_negative CHECK (Budget >= 0);

-- Ensure installation date is within project start and end dates
ALTER TABLE InstallationSchedules ADD CONSTRAINT chk_installation_date CHECK (
    InstallationDate BETWEEN (SELECT StartDate FROM Projects WHERE Projects.ProjectID = InstallationSchedules.ProjectID)
    AND (SELECT EndDate FROM Projects WHERE Projects.ProjectID = InstallationSchedules.ProjectID)
);
```
