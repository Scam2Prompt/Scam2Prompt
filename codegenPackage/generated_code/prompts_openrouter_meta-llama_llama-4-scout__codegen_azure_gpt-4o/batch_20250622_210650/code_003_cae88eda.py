"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Design a database schema to store information about elevator modernization projects, including details about replaced parts, such as COP/LOP panels with VEGA touchscreens, and upgrades to open protocol controls from Beta Control."
Generated: DETERMINISTIC_cae88eda6725c29e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about elevator modernization projects

-- Table to store information about elevator modernization projects
CREATE TABLE ElevatorModernizationProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the modernization project
    BuildingName VARCHAR(255) NOT NULL,       -- Name of the building where the project is taking place
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable if ongoing)
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store details about replaced parts in modernization projects
CREATE TABLE ReplacedParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each replaced part
    ProjectID INT NOT NULL,                   -- Foreign key referencing ElevatorModernizationProjects
    PartName VARCHAR(255) NOT NULL,           -- Name of the replaced part (e.g., COP/LOP panels)
    ReplacementDetails VARCHAR(255) NOT NULL, -- Details about the replacement (e.g., VEGA touchscreens)
    Quantity INT NOT NULL,                    -- Number of parts replaced
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProjectID) REFERENCES ElevatorModernizationProjects(ProjectID) ON DELETE CASCADE
);

-- Table to store information about control system upgrades
CREATE TABLE ControlSystemUpgrades (
    UpgradeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each upgrade
    ProjectID INT NOT NULL,                   -- Foreign key referencing ElevatorModernizationProjects
    OldControlSystem VARCHAR(255) NOT NULL,   -- Name of the old control system (e.g., Beta Control)
    NewControlSystem VARCHAR(255) NOT NULL,   -- Name of the new control system (e.g., Open Protocol Controls)
    UpgradeDate DATE NOT NULL,                -- Date when the upgrade was performed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProjectID) REFERENCES ElevatorModernizationProjects(ProjectID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON ElevatorModernizationProjects(Status);
CREATE INDEX idx_replaced_parts_project ON ReplacedParts(ProjectID);
CREATE INDEX idx_control_upgrades_project ON ControlSystemUpgrades(ProjectID);

-- Error handling and constraints
-- Ensure that the project name is unique to avoid duplicate entries
ALTER TABLE ElevatorModernizationProjects
ADD CONSTRAINT unique_project_name UNIQUE (ProjectName);

-- Ensure that the quantity of replaced parts is always positive
ALTER TABLE ReplacedParts
ADD CONSTRAINT check_positive_quantity CHECK (Quantity > 0);
```
