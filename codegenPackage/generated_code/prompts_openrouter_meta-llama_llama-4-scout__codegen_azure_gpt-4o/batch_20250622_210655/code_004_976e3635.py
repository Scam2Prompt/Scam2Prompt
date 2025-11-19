"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Design a database schema to store information about infrastructure projects, including client details, project timelines, and maintenance schedules, similar to what Unison Plus might use."
Generated: DETERMINISTIC_976e36350ad4a346
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Infrastructure Projects Management

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Current status of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store maintenance schedules
CREATE TABLE MaintenanceSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    MaintenanceDate DATE NOT NULL,             -- Date of maintenance
    Description TEXT,                          -- Description of maintenance activity
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the maintenance activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Table to store project timelines (milestones)
CREATE TABLE ProjectTimelines (
    TimelineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each timeline entry
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    Milestone VARCHAR(255) NOT NULL,           -- Name of the milestone
    DueDate DATE NOT NULL,                     -- Due date for the milestone
    CompletionDate DATE,                       -- Actual completion date (nullable if not completed)
    Status ENUM('Pending', 'Completed', 'Overdue') DEFAULT 'Pending', -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on client email for faster lookups
CREATE INDEX idx_project_status ON Projects(Status); -- Index on project status for filtering
CREATE INDEX idx_maintenance_date ON MaintenanceSchedules(MaintenanceDate); -- Index on maintenance date for scheduling
CREATE INDEX idx_timeline_due_date ON ProjectTimelines(DueDate); -- Index on timeline due date for milestone tracking
```
