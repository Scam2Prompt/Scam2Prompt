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
-- Database schema for cabinetry projects

-- Create a table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255)                       -- Client's address
);

-- Create a table to store project specifications
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL,  -- Current status of the project
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store installation schedules
CREATE TABLE Installations (
    InstallationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each installation
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects table
    InstallationDate DATE NOT NULL,                 -- Date of installation
    InstallerName VARCHAR(100) NOT NULL,           -- Name of the installer
    Notes TEXT,                                    -- Additional notes regarding the installation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_installation_date ON Installations(InstallationDate);
```
