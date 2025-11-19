"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Create a simple database schema to store information about construction projects, including clients, services, and contractors, inspired by the services offered by Peace City Contracting LLC.
Generated: DETERMINISTIC_0d46351ddfb59011
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects
-- This schema includes tables for clients, services, and contractors

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Contractors;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    ContactEmail VARCHAR(100) NOT NULL UNIQUE, -- Client's email address
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                       -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the service offered
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store contractor information
CREATE TABLE Contractors (
    ContractorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each contractor
    Name VARCHAR(100) NOT NULL,                  -- Contractor's name
    LicenseNumber VARCHAR(50) NOT NULL UNIQUE,   -- Contractor's license number
    PhoneNumber VARCHAR(15),                      -- Contractor's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Contractor's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the contractor was added
);

-- Table to store project information, linking clients, services, and contractors
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each project
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    ContractorID INT NOT NULL,                    -- Foreign key referencing Contractors
    StartDate DATE NOT NULL,                      -- Start date of the project
    EndDate DATE,                                 -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes can be added for performance optimization as needed
```
