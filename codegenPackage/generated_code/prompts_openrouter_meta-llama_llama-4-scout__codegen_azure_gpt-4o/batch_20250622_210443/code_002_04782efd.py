"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Design a database schema for storing information about interior design projects, including project details, client information, and space planning, based on the services provided by Amazing Interior.
Generated: DETERMINISTIC_04782efdd28b7ed1
Batch ID: 20250622_210443
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
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store space planning details
CREATE TABLE SpacePlanning (
    SpaceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each space
    ProjectID INT NOT NULL,                  -- Foreign key referencing Projects table
    SpaceName VARCHAR(100) NOT NULL,         -- Name of the space (e.g., Living Room, Kitchen)
    Dimensions VARCHAR(50),                  -- Dimensions of the space (e.g., "12x15 ft")
    DesignStyle VARCHAR(50),                 -- Design style for the space (e.g., "Modern", "Rustic")
    Notes TEXT,                              -- Additional notes or requirements for the space
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Table to store services provided for each project
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Furniture Selection", "Lighting Design")
    Cost DECIMAL(10, 2),                      -- Cost of the service
    Notes TEXT,                               -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_space_project ON SpacePlanning(ProjectID); -- Index for space planning queries by project
CREATE INDEX idx_service_project ON Services(ProjectID); -- Index for service queries by project
```
