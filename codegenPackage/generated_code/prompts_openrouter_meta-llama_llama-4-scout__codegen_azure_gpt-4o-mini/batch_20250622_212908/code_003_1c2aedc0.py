"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Generate a SQL database schema for storing information about construction projects, including clients, services, and equipment, based on AKNAN's business model.
Generated: DETERMINISTIC_1c2aedc00d1b43b3
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for AKNAN's Construction Projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Client's name
    ContactEmail VARCHAR(100) UNIQUE NOT NULL, -- Client's contact email
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered in construction projects
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                          -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store equipment used in construction projects
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each equipment
    EquipmentName VARCHAR(100) NOT NULL,        -- Name of the equipment
    Description TEXT,                            -- Description of the equipment
    PurchaseDate DATE,                          -- Date of purchase
    Cost DECIMAL(10, 2),                        -- Cost of the equipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store construction projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                     -- Foreign key referencing Services
    EquipmentID INT,                            -- Foreign key referencing Equipment (optional)
    ProjectName VARCHAR(100) NOT NULL,         -- Name of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE SET NULL -- Optional equipment reference
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_project_status ON Projects(Status);
```
