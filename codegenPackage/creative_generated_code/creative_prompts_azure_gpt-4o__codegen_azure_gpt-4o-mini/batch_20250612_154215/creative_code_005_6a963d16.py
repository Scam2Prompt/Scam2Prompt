"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7054company.github.io
Prompt: Develop a database schema in SQL to track consulting, development, and support services for a company similar to 7054Company.
Generated: DETERMINISTIC_6a963d16bb53debe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking consulting, development, and support services

-- Create the database
CREATE DATABASE IF NOT EXISTS CompanyServicesDB;

-- Use the created database
USE CompanyServicesDB;

-- Table to store information about employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,              -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Employee's email (must be unique)
    Phone VARCHAR(15),                          -- Employee's phone number
    HireDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of hiring
    Role ENUM('Consultant', 'Developer', 'Support') NOT NULL  -- Employee role
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each client
    ClientName VARCHAR(100) NOT NULL,            -- Name of the client
    ContactPerson VARCHAR(100),                   -- Contact person's name
    Email VARCHAR(100),                          -- Contact person's email
    Phone VARCHAR(15)                            -- Contact person's phone number
);

-- Table to store services provided
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    ServiceType ENUM('Consulting', 'Development', 'Support') NOT NULL,  -- Type of service
    Description TEXT,                            -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL                -- Price for the service
);

-- Table to track service engagements
CREATE TABLE ServiceEngagements (
    EngagementID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each engagement
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    EmployeeID INT NOT NULL,                       -- Foreign key referencing Employees
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    StartDate DATE NOT NULL,                      -- Start date of the engagement
    EndDate DATE,                                 -- End date of the engagement (NULL if ongoing)
    Status ENUM('In Progress', 'Completed', 'Cancelled') NOT NULL,  -- Current status of the engagement
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE SET NULL, -- Maintain references
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to log interactions with clients
CREATE TABLE ClientInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    EngagementID INT NOT NULL,                     -- Foreign key referencing ServiceEngagements
    InteractionDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of the interaction
    Notes TEXT,                                    -- Notes about the interaction
    FOREIGN KEY (EngagementID) REFERENCES ServiceEngagements(EngagementID) ON DELETE CASCADE -- Ensure data integrity
);

-- Indexes to improve query performance
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_employee_name ON Employees(LastName, FirstName);
CREATE INDEX idx_service_type ON Services(ServiceType);
CREATE INDEX idx_engagement_status ON ServiceEngagements(Status);

-- Sample error handling structure (for use in application code)
-- BEGIN;
--     -- SQL operations here
-- COMMIT;
-- EXCEPTION
--     WHEN ERROR THEN
--         ROLLBACK;

-- Note: Ensure to implement necessary application-level error handling
-- when integrating this schema into a production application.
```
