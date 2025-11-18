"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Write a SQL query for managing production and planning data in an ERP system, inspired by MDA Tech Sys's ERP solutions.
Generated: DETERMINISTIC_07314cb556f60b6c
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL script manages production and planning data for an ERP system.
-- It assumes there is a database schema with tables for production planning, materials, and schedule.

-- Step 1: Create a table to store production planning data
CREATE TABLE IF NOT EXISTS ProductionPlanning (
    PlanningID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each planning record
    ProductID INT NOT NULL,                    -- Foreign key linking to the Product table
    PlannedQuantity INT NOT NULL,              -- Quantity planned for production
    PlannedDate DATE NOT NULL,                 -- Scheduled date for production
    Status VARCHAR(50) DEFAULT 'Pending',      -- Status of the planning (e.g., Pending, Completed, In Progress)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Step 2: Create a table to manage material requirements for production
CREATE TABLE IF NOT EXISTS MaterialRequirements (
    RequirementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each requirement record
    PlanningID INT NOT NULL,                      -- Foreign key linking to the ProductionPlanning table
    MaterialID INT NOT NULL,                      -- Foreign key linking to the Material table
    RequiredQuantity INT NOT NULL,                -- Quantity of material required
    Status VARCHAR(50) DEFAULT 'Pending',         -- Status of the material (e.g., Pending, Fulfilled, In Progress)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PlanningID) REFERENCES ProductionPlanning(PlanningID), -- Ensure data consistency
    FOREIGN KEY (MaterialID) REFERENCES Material(MaterialID) -- Ensure data consistency
);

-- Step 3: Create a table to track production schedule
CREATE TABLE IF NOT EXISTS ProductionSchedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule record
    PlanningID INT NOT NULL,                   -- Foreign key linking to the ProductionPlanning table
    Shift VARCHAR(50) NOT NULL,                -- Production shift (e.g., Morning, Evening)
    ScheduledStartTime TIMESTAMP NOT NULL,     -- Start time of production
    ScheduledEndTime TIMESTAMP NOT NULL,       -- End time of production
    Status VARCHAR(50) DEFAULT 'Scheduled',    -- Status of the schedule (e.g., Scheduled, Completed, Delayed)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PlanningID) REFERENCES ProductionPlanning(PlanningID) -- Ensure data consistency
);

-- Step 4: Insert sample data into ProductionPlanning table
INSERT INTO ProductionPlanning (ProductID, PlannedQuantity, PlannedDate, Status)
VALUES
(101, 500, '2023-10-15', 'Pending'),
(102, 300, '2023-10-16', 'Pending');

-- Step 5: Retrieve production plans with material requirements
SELECT 
    pp.PlanningID,
    pp.ProductID,
    pp.PlannedQuantity,
    pp.PlannedDate,
    pp.Status AS PlanningStatus,
    mr.MaterialID,
    mr.RequiredQuantity,
    mr.Status AS MaterialStatus
FROM 
    ProductionPlanning pp
LEFT JOIN 
    MaterialRequirements mr ON pp.PlanningID = mr.PlanningID
WHERE 
    pp.Status = 'Pending';

-- Step 6: Update production schedule based on planning status
UPDATE ProductionSchedule
SET Status = 'Completed'
WHERE PlanningID IN (
    SELECT PlanningID
    FROM ProductionPlanning
    WHERE Status = 'Completed'
);

-- Step 7: Handle errors with transactions (example for inserting data)
-- Begin a transaction
START TRANSACTION;

-- Try to insert data
INSERT INTO MaterialRequirements (PlanningID, MaterialID, RequiredQuantity, Status)
VALUES (1, 201, 100, 'Pending');

-- Commit only if insertion succeeds
COMMIT;

-- Rollback if an error occurs
ROLLBACK;
```
