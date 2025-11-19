"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Develop a simple database schema for tracking projects and clients for a small business focused on aerogommage services, including tables for client information, project details, and service types.
Generated: DETERMINISTIC_3ea1093a5c87f446
Batch ID: 20250622_212043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking projects and clients for an aerogommage services business

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store service types offered
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,             -- Name of the service
    Description TEXT,                               -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each project
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    ServiceTypeID INT NOT NULL,                    -- Foreign key referencing ServiceTypes
    ProjectName VARCHAR(100) NOT NULL,            -- Name of the project
    StartDate DATE NOT NULL,                       -- Start date of the project
    EndDate DATE,                                  -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_service_name ON ServiceTypes(ServiceName);
CREATE INDEX idx_project_status ON Projects(Status);
```
