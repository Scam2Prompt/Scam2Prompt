"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Design a simple database schema to store information about brick and stone restoration projects, including client details, project scope, and service types like tuckpointing and remedial wall tie replacement."
Generated: DETERMINISTIC_21e239799bb80a78
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for brick and stone restoration projects

-- Create a database for the restoration projects
CREATE DATABASE RestorationProjects;

-- Use the created database
USE RestorationProjects;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL UNIQUE,      -- Name of the service (e.g., Tuckpointing)
    Description TEXT                              -- Description of the service
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each project
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    ProjectScope TEXT NOT NULL,                    -- Description of the project scope
    ServiceTypeID INT NOT NULL,                    -- Foreign key referencing ServiceTypes
    StartDate DATE NOT NULL,                       -- Start date of the project
    EndDate DATE,                                  -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert sample service types
INSERT INTO ServiceTypes (ServiceName, Description) VALUES
('Tuckpointing', 'Repairing mortar joints in masonry'),
('Remedial Wall Tie Replacement', 'Replacing wall ties in masonry walls');

-- Note: Ensure to handle errors during insertion and other operations in application code.
```
