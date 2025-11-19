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
-- Includes client details and project management data

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date (if applicable)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store project team members
CREATE TABLE ProjectTeam (
    TeamMemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    ProjectID INT NOT NULL,                      -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,                  -- Full name of the team member
    Role VARCHAR(255) NOT NULL,                  -- Role of the team member in the project
    Email VARCHAR(255),                          -- Email address of the team member
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store project milestones
CREATE TABLE ProjectMilestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,                 -- Name of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Due date for the milestone
    Status ENUM('Pending', 'Completed') DEFAULT 'Pending', -- Current status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store invoices related to projects
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Amount DECIMAL(15, 2) NOT NULL,           -- Invoice amount
    IssueDate DATE NOT NULL,                  -- Date the invoice was issued
    DueDate DATE NOT NULL,                    -- Due date for payment
    Status ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending', -- Current status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store project documents
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    ProjectID INT NOT NULL,                    -- Foreign key referencing the project
    FileName VARCHAR(255) NOT NULL,            -- Name of the file
    FilePath TEXT NOT NULL,                    -- Path to the file on the server
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for file upload
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store project tasks
CREATE TABLE ProjectTasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each task
    ProjectID INT NOT NULL,                -- Foreign key referencing the project
    Name VARCHAR(255) NOT NULL,            -- Name of the task
    Description TEXT,                      -- Detailed description of the task
    AssignedTo INT,                        -- Foreign key referencing the team member
    DueDate DATE NOT NULL,                 -- Due date for the task
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AssignedTo) REFERENCES ProjectTeam(TeamMemberID) ON DELETE SET NULL -- Ensure referential integrity
);
```
