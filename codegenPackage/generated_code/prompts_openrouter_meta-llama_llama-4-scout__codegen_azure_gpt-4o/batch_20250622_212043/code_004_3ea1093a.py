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
-- Database Schema for Tracking Projects and Clients

-- Table: Clients
-- Stores information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Table: ServiceTypes
-- Stores information about different types of services offered
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service
    Description TEXT,                             -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service type was added
);

-- Table: Projects
-- Stores information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ServiceTypeID INT NOT NULL,               -- Foreign key referencing ServiceTypes table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the project
    Notes TEXT,                               -- Additional notes about the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE SET NULL -- Set service type to NULL if removed
);

-- Indexes for faster lookups
CREATE INDEX idx_client_email ON Clients (Email); -- Index for email lookup
CREATE INDEX idx_project_status ON Projects (Status); -- Index for project status lookup
```
