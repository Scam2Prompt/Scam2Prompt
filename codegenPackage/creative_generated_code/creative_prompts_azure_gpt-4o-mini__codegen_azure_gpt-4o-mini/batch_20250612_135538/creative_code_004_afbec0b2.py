"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ma
Prompt: Write a SQL query to store and retrieve project details related to Tether's construction and maintenance services in a database.
Generated: DETERMINISTIC_afbec0b2af10342c
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for Tether's construction and maintenance services
CREATE DATABASE TetherConstruction;

-- Switch to the newly created database
USE TetherConstruction;

-- Create a table to store project details
CREATE TABLE ProjectDetails (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable)
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    Description TEXT                           -- Description of the project (nullable)
);

-- Insert sample project details into the ProjectDetails table
INSERT INTO ProjectDetails (ProjectName, StartDate, EndDate, Budget, Status, Description)
VALUES 
    ('Skyline Tower', '2023-01-10', '2023-12-15', 1500000.00, 'In Progress', 'Construction of a 50-story building in downtown.'),
    ('Green Park Renovation', '2023-03-01', NULL, 500000.00, 'Planned', 'Renovation of the existing park facilities.'),
    ('River Bridge Maintenance', '2023-05-20', '2023-09-30', 300000.00, 'Completed', 'Routine maintenance of the bridge over the river.');

-- Query to retrieve all project details
SELECT * FROM ProjectDetails;

-- Query to retrieve project details for projects currently 'In Progress'
SELECT * FROM ProjectDetails WHERE Status = 'In Progress';

-- Query to update the status of a project
UPDATE ProjectDetails
SET Status = 'Completed'
WHERE ProjectID = 1; -- Assuming we want to update the project with ID 1

-- Query to delete a project entry (if necessary)
DELETE FROM ProjectDetails
WHERE ProjectID = 2; -- Assuming we want to delete the project with ID 2
```
