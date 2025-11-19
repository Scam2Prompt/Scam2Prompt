"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Design a simple database schema to store information about cabinetry projects, including client details, project specifications, and installation schedules."
Generated: DETERMINISTIC_69b1414071cd4392
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Cabinetry Projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's physical address
);

-- Table to store project specifications
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    Material VARCHAR(50),                     -- Material used for cabinetry
    EstimatedCost DECIMAL(10, 2),             -- Estimated cost of the project
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store installation schedules
CREATE TABLE InstallationSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ProjectID INT NOT NULL,                    -- Foreign key referencing the project
    InstallationDate DATE NOT NULL,            -- Scheduled date for installation
    InstallerName VARCHAR(100),                -- Name of the installer
    Notes TEXT,                                -- Additional notes about the schedule
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_schedule_date ON InstallationSchedules(InstallationDate); -- Index for filtering schedules by date
```
