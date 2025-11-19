"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Write a SQL query to store and retrieve project details related to Tether's construction and maintenance services in a database.
Generated: DETERMINISTIC_afbec0b2af10342c
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Tether's construction and maintenance services
CREATE DATABASE TetherConstruction;

-- Use the created database
USE TetherConstruction;

-- Create a table to store project details
CREATE TABLE ProjectDetails (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable)
    Budget DECIMAL(10, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    Description TEXT,                          -- Detailed description of the project (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Insert sample project details into the ProjectDetails table
INSERT INTO ProjectDetails (ProjectName, StartDate, EndDate, Budget, Status, Description)
VALUES 
    ('Bridge Construction', '2023-01-15', '2023-06-30', 1500000.00, 'In Progress', 'Construction of a new bridge over the river.'),
    ('Road Maintenance', '2023-03-01', NULL, 500000.00, 'Planned', 'Routine maintenance of the main road.'),
    ('Building Renovation', '2023-02-01', '2023-05-15', 750000.00, 'Completed', 'Renovation of the old building for new offices.');

-- Retrieve all project details from the ProjectDetails table
SELECT 
    ProjectID, 
    ProjectName, 
    StartDate, 
    EndDate, 
    Budget, 
    Status, 
    Description, 
    CreatedAt, 
    UpdatedAt
FROM 
    ProjectDetails;

-- Error handling can be implemented in application code that interacts with this database.
-- Ensure to handle potential SQL exceptions and validate inputs before executing queries.
```
