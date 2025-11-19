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
-- Step 1: Create the table to store project details related to Tether's construction and maintenance services
CREATE TABLE IF NOT EXISTS ProjectDetails (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,              -- Name of the project
    Description TEXT,                               -- Detailed description of the project
    StartDate DATE NOT NULL,                        -- The start date of the project
    EndDate DATE,                                   -- The end date of the project (nullable for ongoing projects)
    ServiceType ENUM('Construction', 'Maintenance') NOT NULL, -- Type of service related to the project
    Budget DECIMAL(15, 2) CHECK (Budget >= 0),      -- Allocated budget for the project, must be non-negative
    ClientName VARCHAR(255),                        -- Name of the client associated with the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Planned', -- Current status of the project
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Step 2: Insert sample data into the table
INSERT INTO ProjectDetails (ProjectName, Description, StartDate, EndDate, ServiceType, Budget, ClientName, Status)
VALUES
    ('Tether HQ Renovation', 'Renovation of the headquarters building.', '2023-10-01', '2024-03-01', 'Construction', 500000.00, 'Tether Inc.', 'In Progress'),
    ('Data Center Maintenance', 'Routine maintenance of the data center.', '2023-09-15', NULL, 'Maintenance', 150000.00, 'Tether Inc.', 'In Progress'),
    ('Warehouse Expansion', 'Expansion of the existing warehouse.', '2023-11-01', '2024-06-01', 'Construction', 750000.00, 'Logistics Corp.', 'Planned');

-- Step 3: Retrieve project details related to Tether's construction and maintenance services
SELECT 
    ProjectID,
    ProjectName,
    Description,
    StartDate,
    EndDate,
    ServiceType,
    Budget,
    ClientName,
    Status,
    LastUpdated
FROM 
    ProjectDetails
WHERE 
    ClientName = 'Tether Inc.'; -- Filter results for projects associated with Tether Inc.

-- Note:
-- - The table ProjectDetails is designed to accommodate projects related to construction and maintenance services.
-- - Constraints and defaults are applied for data integrity and usability.
-- - Error handling (e.g., ensuring budget is non-negative) is enforced through CHECK constraints in the table definition.
```
