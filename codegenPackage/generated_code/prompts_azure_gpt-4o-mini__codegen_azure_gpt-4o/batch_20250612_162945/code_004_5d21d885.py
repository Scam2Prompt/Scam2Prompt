"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing consultancy projects and client interactions
-- This schema is designed to handle projects, clients, services, and interactions.

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    Phone VARCHAR(20),                       -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about services offered by Dusanto Consultancy Trading OU
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Planned', -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store interactions between clients and the consultancy
CREATE TABLE Interactions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    ClientID INT NOT NULL,                        -- Foreign key referencing the client
    ProjectID INT,                                -- Foreign key referencing the project (nullable for general interactions)
    InteractionDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date and time of the interaction
    Notes TEXT,                                   -- Notes about the interaction
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE SET NULL -- Allow null if project is deleted
);

-- Create a table to store the mapping between projects and services
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mapping
    ProjectID INT NOT NULL,                          -- Foreign key referencing the project
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT NOT NULL DEFAULT 1,                -- Quantity of the service provided
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_interaction_date ON Interactions(InteractionDate); -- Index for sorting/filtering interactions by date
```
