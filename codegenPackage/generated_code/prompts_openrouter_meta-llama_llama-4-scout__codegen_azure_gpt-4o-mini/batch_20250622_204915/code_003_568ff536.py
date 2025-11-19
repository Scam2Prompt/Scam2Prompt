"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Design a database schema to store information about civil engineering projects, including project details, client information, and service offerings like waterproofing and structural repairs."
Generated: DETERMINISTIC_568ff5363d6bf527
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about civil engineering projects

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactNumber VARCHAR(15),                 -- Contact number of the client
    Email VARCHAR(255) UNIQUE,                 -- Email address of the client
    Address VARCHAR(255),                       -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable)
    Budget DECIMAL(10, 2) NOT NULL,            -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store service offerings
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL UNIQUE,   -- Name of the service (e.g., Waterproofing, Structural Repairs)
    Description TEXT,                            -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a junction table to associate projects with services
CREATE TABLE ProjectServices (
    ProjectServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project-service association
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the association was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
