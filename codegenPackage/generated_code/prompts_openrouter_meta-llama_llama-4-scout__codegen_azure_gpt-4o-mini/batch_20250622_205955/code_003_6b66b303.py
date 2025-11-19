"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Design a database schema for a construction company's customer relationship management (CRM) system, including tables for clients, projects, and services offered, such as groundworks solutions and health and safety consulting."
Generated: DETERMINISTIC_6b66b303866727dd
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a construction company's CRM system

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,               -- Client's name
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(20),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link projects with services offered
CREATE TABLE ProjectServices (
    ProjectServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project-service link
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services
    Quantity INT NOT NULL,                            -- Quantity of the service provided
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_client ON Projects(ClientID);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
