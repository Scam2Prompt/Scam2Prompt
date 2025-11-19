"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Create a SQL database schema to store information about roofing projects, clients, and services offered by King Roofing.
Generated: DETERMINISTIC_d28bfe15e833c928
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for King Roofing
CREATE DATABASE KingRoofing;

-- Use the newly created database
USE KingRoofing;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    City VARCHAR(50),                         -- Client's city
    State VARCHAR(50),                        -- Client's state
    ZipCode VARCHAR(10),                      -- Client's zip code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store roofing project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    ProjectName VARCHAR(100) NOT NULL,         -- Name of the roofing project
    StartDate DATE NOT NULL,                    -- Project start date
    EndDate DATE,                               -- Project end date (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Project status
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services offered by King Roofing
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to link projects with services offered
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project-service link
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services
    Quantity INT NOT NULL,                           -- Quantity of the service used in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
