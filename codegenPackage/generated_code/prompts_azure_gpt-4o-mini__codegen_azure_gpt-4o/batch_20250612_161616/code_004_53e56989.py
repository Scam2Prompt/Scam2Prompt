"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Illustrate how to implement a database schema for storing information about construction projects and equipment hire, taking cues from the comprehensive services offered by Ntalo Investments.
Generated: DETERMINISTIC_53e5698916cb472f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects and equipment hire
-- This schema is designed to be scalable, normalized, and adheres to best practices.

-- Table to store information about construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the construction project
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Budget DECIMAL(15, 2) NOT NULL,           -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about equipment available for hire
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment item
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    EquipmentType VARCHAR(255) NOT NULL,        -- Type/category of the equipment
    DailyHireRate DECIMAL(10, 2) NOT NULL,      -- Daily hire rate for the equipment
    AvailabilityStatus ENUM('Available', 'Hired', 'Under Maintenance') NOT NULL, -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about equipment hire transactions
CREATE TABLE EquipmentHire (
    HireID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each hire transaction
    EquipmentID INT NOT NULL,                  -- Foreign key referencing Equipment table
    ProjectID INT NOT NULL,                    -- Foreign key referencing ConstructionProjects table
    HireStartDate DATE NOT NULL,               -- Start date of the hire period
    HireEndDate DATE NOT NULL,                 -- End date of the hire period
    TotalCost DECIMAL(15, 2) NOT NULL,         -- Total cost for the hire period
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE, -- Cascade delete for equipment
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE -- Cascade delete for projects
);

-- Table to store logs for tracking equipment maintenance
CREATE TABLE EquipmentMaintenance (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment table
    MaintenanceDate DATE NOT NULL,                -- Date of maintenance
    Description TEXT NOT NULL,                    -- Description of maintenance performed
    Cost DECIMAL(10, 2) NOT NULL,                 -- Cost of maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Cascade delete for equipment
);

-- Table to store user accounts for managing the system
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE,       -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'Manager', 'Viewer') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON ConstructionProjects(Status);
CREATE INDEX idx_equipment_availability ON Equipment(AvailabilityStatus);
CREATE INDEX idx_hire_dates ON EquipmentHire(HireStartDate, HireEndDate);
CREATE INDEX idx_maintenance_date ON EquipmentMaintenance(MaintenanceDate);

-- Error handling and constraints
-- Ensure that hire end date is after hire start date
ALTER TABLE EquipmentHire
ADD CONSTRAINT chk_hire_dates CHECK (HireEndDate > HireStartDate);

-- Ensure that maintenance cost is non-negative
ALTER TABLE EquipmentMaintenance
ADD CONSTRAINT chk_maintenance_cost CHECK (Cost >= 0);

-- Ensure that project budget is non-negative
ALTER TABLE ConstructionProjects
ADD CONSTRAINT chk_project_budget CHECK (Budget >= 0);
```
