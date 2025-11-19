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
-- SQL Database Schema for Home Remodeling Projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Installations;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectScope TEXT NOT NULL,                -- Description of the project scope
    StartDate DATE NOT NULL,                   -- Scheduled start date of the project
    EndDate DATE,                              -- Scheduled end date of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store installation schedules
CREATE TABLE Installations (
    InstallationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each installation
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects
    InstallationDate DATE NOT NULL,                 -- Date of the installation
    Description TEXT,                               -- Description of the installation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the installation was scheduled
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321', '456 Oak St, Springfield');

INSERT INTO Projects (ClientID, ProjectScope, StartDate, EndDate, Status) VALUES
(1, 'Kitchen remodel with new cabinets and countertops', '2023-10-01', '2023-10-15', 'In Progress'),
(2, 'Bathroom renovation including new tiles and fixtures', '2023-11-01', NULL, 'Pending');

INSERT INTO Installations (ProjectID, InstallationDate, Description) VALUES
(1, '2023-10-05', 'Installed new cabinets'),
(1, '2023-10-10', 'Installed new countertops'),
(2, '2023-11-05', 'Scheduled for tile installation');
```
