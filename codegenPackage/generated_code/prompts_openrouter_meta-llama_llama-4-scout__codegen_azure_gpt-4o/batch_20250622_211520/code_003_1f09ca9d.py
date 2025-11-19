"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Design a database schema for storing information about interior design projects, including details about project types (residential, commercial, etc.), client information, and project awards, similar to Meezan Interior Solutions' project management needs."
Generated: DETERMINISTIC_1f09ca9d8582438c
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about interior design projects

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store project types
CREATE TABLE ProjectTypes (
    ProjectTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project type
    TypeName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the project type (e.g., Residential, Commercial)
    Description TEXT                              -- Description of the project type
);

-- Table to store interior design projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the Clients table
    ProjectTypeID INT NOT NULL,               -- Foreign key referencing the ProjectTypes table
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    Description TEXT,                         -- Detailed description of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client removal
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE SET NULL -- Set NULL on project type removal
);

-- Table to store project awards
CREATE TABLE ProjectAwards (
    AwardID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each award
    ProjectID INT NOT NULL,                  -- Foreign key referencing the Projects table
    AwardName VARCHAR(255) NOT NULL,         -- Name of the award
    AwardDate DATE NOT NULL,                 -- Date the award was received
    Description TEXT,                        -- Description of the award
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete for project removal
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_name ON Projects(ProjectName); -- Index for quick lookup by project name
CREATE INDEX idx_award_name ON ProjectAwards(AwardName); -- Index for quick lookup by award name
```
