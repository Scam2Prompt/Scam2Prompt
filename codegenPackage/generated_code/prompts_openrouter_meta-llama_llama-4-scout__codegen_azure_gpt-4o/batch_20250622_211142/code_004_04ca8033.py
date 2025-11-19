"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Create a sample database schema for storing information about NDT equipment, personnel, and projects in the marine industry."
Generated: DETERMINISTIC_04ca80339e5d4223
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about NDT equipment, personnel, and projects in the marine industry

-- Create a table for storing information about NDT equipment
CREATE TABLE NDT_Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    Name VARCHAR(100) NOT NULL,                 -- Name of the equipment
    Type VARCHAR(50) NOT NULL,                  -- Type of equipment (e.g., Ultrasonic, Radiographic)
    Manufacturer VARCHAR(100),                  -- Manufacturer of the equipment
    Model VARCHAR(50),                          -- Model of the equipment
    SerialNumber VARCHAR(50) UNIQUE,            -- Unique serial number for the equipment
    CalibrationDate DATE NOT NULL,              -- Last calibration date
    CalibrationDueDate DATE NOT NULL,           -- Next calibration due date
    Status ENUM('Active', 'Inactive', 'Under Maintenance') DEFAULT 'Active', -- Current status of the equipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing information about personnel
CREATE TABLE Personnel (
    PersonnelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each personnel
    FirstName VARCHAR(50) NOT NULL,             -- First name of the personnel
    LastName VARCHAR(50) NOT NULL,              -- Last name of the personnel
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the personnel
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    CertificationLevel ENUM('Level 1', 'Level 2', 'Level 3') NOT NULL, -- Certification level
    CertificationExpiryDate DATE NOT NULL,      -- Certification expiry date
    Role VARCHAR(50) NOT NULL,                  -- Role in the organization (e.g., Inspector, Technician)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    Name VARCHAR(100) NOT NULL,                 -- Name of the project
    Description TEXT,                           -- Detailed description of the project
    StartDate DATE NOT NULL,                    -- Project start date
    EndDate DATE,                               -- Project end date (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Planned', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for associating personnel with projects
CREATE TABLE ProjectPersonnel (
    ProjectPersonnelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    ProjectID INT NOT NULL,                            -- Foreign key referencing Projects table
    PersonnelID INT NOT NULL,                          -- Foreign key referencing Personnel table
    RoleInProject VARCHAR(50) NOT NULL,                -- Role of the personnel in the project
    AssignedDate DATE NOT NULL,                        -- Date when the personnel was assigned to the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PersonnelID) REFERENCES Personnel(PersonnelID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table for associating equipment with projects
CREATE TABLE ProjectEquipment (
    ProjectEquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    ProjectID INT NOT NULL,                            -- Foreign key referencing Projects table
    EquipmentID INT NOT NULL,                          -- Foreign key referencing NDT_Equipment table
    AssignedDate DATE NOT NULL,                        -- Date when the equipment was assigned to the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (EquipmentID) REFERENCES NDT_Equipment(EquipmentID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table for logging equipment usage
CREATE TABLE EquipmentUsageLog (
    UsageLogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    EquipmentID INT NOT NULL,                  -- Foreign key referencing NDT_Equipment table
    PersonnelID INT NOT NULL,                  -- Foreign key referencing Personnel table
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    UsageDate DATE NOT NULL,                   -- Date of equipment usage
    Notes TEXT,                                -- Additional notes about the usage
    FOREIGN KEY (EquipmentID) REFERENCES NDT_Equipment(EquipmentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PersonnelID) REFERENCES Personnel(PersonnelID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete
);
```
