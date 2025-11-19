"""
Generated Code Metadata:
========================
Original URL: https://bytnox.com
Prompt: "Design a database schema for storing architectural project information, including client details and project management data, inspired by Études' comprehensive suite of professional services."
Generated: DETERMINISTIC_756e2af6fe531a13
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing architectural project information

-- Create a table for storing client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,               -- Client's name
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(20),                         -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (nullable)
    Status ENUM('Planning', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing project management data
CREATE TABLE ProjectManagement (
    ManagementID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each management record
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects table
    AssignedTo VARCHAR(255) NOT NULL,            -- Name of the person assigned to the project
    Role VARCHAR(100) NOT NULL,                  -- Role of the person in the project
    HoursWorked DECIMAL(5, 2) DEFAULT 0.00,      -- Total hours worked on the project
    Notes TEXT,                                  -- Additional notes regarding the project management
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for storing project milestones
CREATE TABLE Milestones (
    MilestoneID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects table
    MilestoneName VARCHAR(255) NOT NULL,        -- Name of the milestone
    DueDate DATE NOT NULL,                       -- Due date for the milestone
    Status ENUM('Pending', 'Achieved', 'Delayed') NOT NULL,  -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
