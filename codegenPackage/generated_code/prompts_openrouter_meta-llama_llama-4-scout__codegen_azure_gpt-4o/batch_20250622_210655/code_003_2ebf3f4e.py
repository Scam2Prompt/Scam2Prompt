"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Design a database schema for storing architectural project data using Études' comprehensive suite of professional services."
Generated: DETERMINISTIC_2ebf3f4ebd1ff942
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing architectural project data
-- This schema is designed to support Études' comprehensive suite of professional services.

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store architectural projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store services offered by Études
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(15, 2) NOT NULL,            -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store project-service relationships
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing the project
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT NOT NULL DEFAULT 1,                -- Quantity of the service used in the project
    TotalCost DECIMAL(15, 2) NOT NULL,               -- Total cost for the service in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is removed
);

-- Table to store team members working on projects
CREATE TABLE TeamMembers (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    Name VARCHAR(255) NOT NULL,                  -- Full name of the team member
    Role VARCHAR(255) NOT NULL,                  -- Role of the team member (e.g., Architect, Engineer)
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the team member
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store project-team relationships
CREATE TABLE ProjectTeams (
    ProjectTeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                       -- Foreign key referencing the project
    TeamMemberID INT NOT NULL,                    -- Foreign key referencing the team member
    AssignedDate DATE NOT NULL,                   -- Date the team member was assigned to the project
    Role VARCHAR(255) NOT NULL,                   -- Role of the team member in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (TeamMemberID) REFERENCES TeamMembers(TeamMemberID) ON DELETE CASCADE -- Cascade delete if team member is removed
);

-- Table to store project milestones
CREATE TABLE Milestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,                 -- Name of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Due date for the milestone
    Status ENUM('Pending', 'Completed', 'Overdue') NOT NULL, -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Table to store invoices for projects
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    IssueDate DATE NOT NULL,                  -- Date the invoice was issued
    DueDate DATE NOT NULL,                    -- Due date for payment
    TotalAmount DECIMAL(15, 2) NOT NULL,      -- Total amount to be paid
    Status ENUM('Pending', 'Paid', 'Overdue') NOT NULL, -- Current status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);
```
