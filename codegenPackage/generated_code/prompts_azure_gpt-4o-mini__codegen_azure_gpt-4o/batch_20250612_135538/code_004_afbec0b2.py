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
-- Create a table to store project details related to Tether's construction and maintenance services
CREATE TABLE IF NOT EXISTS ProjectDetails (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    Budget DECIMAL(15, 2),                   -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the ProjectDetails table
INSERT INTO ProjectDetails (ProjectName, Description, StartDate, EndDate, Status, Budget)
VALUES
    ('Tether HQ Construction', 'Construction of the new Tether headquarters.', '2023-01-15', '2023-12-15', 'In Progress', 5000000.00),
    ('Maintenance of Tether HQ', 'Regular maintenance of the Tether headquarters.', '2023-01-01', NULL, 'In Progress', 200000.00),
    ('Tether Warehouse Expansion', 'Expansion of the Tether warehouse facilities.', '2023-06-01', '2024-06-01', 'Planned', 1500000.00);

-- Retrieve all project details related to Tether's construction and maintenance services
SELECT 
    ProjectID,
    ProjectName,
    Description,
    StartDate,
    EndDate,
    Status,
    Budget,
    CreatedAt,
    UpdatedAt
FROM 
    ProjectDetails
WHERE 
    ProjectName LIKE '%Tether%' -- Filter projects related to Tether
ORDER BY 
    StartDate ASC; -- Sort projects by start date in ascending order
```
