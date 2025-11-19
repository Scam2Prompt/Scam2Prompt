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
-- SQL Schema for managing client relationships and projects for a digital marketing agency

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Client's name
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Client's email address
    Phone VARCHAR(20),                       -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Project name
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Project status
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table for storing services offered by the agency
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Service name
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for associating projects with services
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    ProjectID INT NOT NULL,                          -- Foreign key referencing the project
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT DEFAULT 1,                          -- Quantity of the service used in the project
    TotalCost DECIMAL(10, 2) GENERATED ALWAYS AS (Quantity * (SELECT Price FROM Services WHERE ServiceID = ProjectServices.ServiceID)) STORED, -- Total cost calculation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the association was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Create indexes for faster lookups
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_client ON Projects(ClientID);
CREATE INDEX idx_project_service ON ProjectServices(ProjectID, ServiceID);
```
