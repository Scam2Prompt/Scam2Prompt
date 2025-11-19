"""
Generated Code Metadata:
========================
Original URL: https://celestia.top
Prompt: "Design a database schema for an architectural solutions platform that includes client information, project details, and service types."
Generated: DETERMINISTIC_91cd7054c0924cd0
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an Architectural Solutions Platform

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS ProjectServices;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store different types of services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the service
    Description TEXT,                          -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Junction table to associate projects with services
CREATE TABLE ProjectServices (
    ProjectServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each association
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,  -- Ensure referential integrity
    UNIQUE (ProjectID, ServiceID)                    -- Prevent duplicate associations
);

-- Indexes can be added for performance optimization as needed
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_status ON Projects(Status);
```
