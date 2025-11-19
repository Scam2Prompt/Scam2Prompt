"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Design a database schema for storing client information, projects, and services offered by an engineering and architecture firm like TWM Associates."
Generated: DETERMINISTIC_8aa82f37c4e3a42c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information, projects, and services
-- offered by an engineering and architecture firm

-- Create a database for the firm
CREATE DATABASE TWM_Associates;

-- Use the created database
USE TWM_Associates;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactPerson VARCHAR(255),                -- Name of the contact person
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the client
    Phone VARCHAR(20),                         -- Phone number of the client
    Address VARCHAR(255),                       -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services offered by the firm
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store projects associated with clients
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to associate services with projects
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the association
    ProjectID INT NOT NULL,                            -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                            -- Foreign key referencing Services
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
