"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Create a SQL database schema for managing client relationships and projects for a digital marketing agency like moOve, including tables for clients, projects, and services offered.
Generated: DETERMINISTIC_90b9b5e7e7fb380e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Managing Client Relationships and Projects
-- This schema is designed for a digital marketing agency.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS ProjectServices;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL UNIQUE, -- Email address for client contact
    PhoneNumber VARCHAR(20),                   -- Phone number for client contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store services offered by the agency
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the service
    Description TEXT,                           -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to manage the many-to-many relationship between projects and services
CREATE TABLE ProjectServices (
    ProjectServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each project-service relationship
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the relationship was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensures referential integrity
    UNIQUE (ProjectID, ServiceID)                   -- Prevents duplicate entries for the same project-service relationship
);

-- Indexes can be added for performance optimization as needed
-- Example: CREATE INDEX idx_client_name ON Clients(ClientName);
```
