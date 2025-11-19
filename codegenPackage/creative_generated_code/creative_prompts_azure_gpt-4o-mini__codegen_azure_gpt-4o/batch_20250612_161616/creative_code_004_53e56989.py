"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Illustrate how to implement a database schema for storing information about construction projects and equipment hire, taking cues from the comprehensive services offered by Ntalo Investments.
Generated: DETERMINISTIC_53e5698916cb472f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information related to construction projects and equipment hire
-- Comprehensive services inspired by Ntalo Investments

-- Table to store information about construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the construction project
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client who owns the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (can be NULL if ongoing)
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Table to store information about equipment available for hire
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the equipment
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    EquipmentType VARCHAR(255),                 -- Type/category of the equipment
    PricePerDay DECIMAL(10, 2) NOT NULL,        -- Rental price per day
    AvailabilityStatus ENUM('Available', 'Rented', 'Under Maintenance') DEFAULT 'Available', -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Table to store equipment hire transactions
CREATE TABLE EquipmentHire (
    HireID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the hire transaction
    EquipmentID INT NOT NULL,                  -- Foreign key referencing Equipment table
    ProjectID INT NOT NULL,                    -- Foreign key referencing ConstructionProjects table
    HireStartDate DATE NOT NULL,               -- Start date of the hire
    HireEndDate DATE NOT NULL,                 -- End date of the hire
    TotalCost DECIMAL(15, 2),                  -- Total cost of the hire
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store maintenance records for equipment
CREATE TABLE EquipmentMaintenance (
    MaintenanceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the maintenance record
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment table
    MaintenanceDate DATE NOT NULL,                -- Date of maintenance
    MaintenanceDescription TEXT NOT NULL,         -- Details about the maintenance activity
    Cost DECIMAL(10, 2),                          -- Cost associated with the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store clients (optional, for enhanced organization)
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the client
    ClientName VARCHAR(255) NOT NULL,        -- Name of the client
    ContactInfo VARCHAR(255),                -- Contact information (email, phone number, etc.)
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Add foreign key relation to link ConstructionProjects with Clients (if Clients table is used)
ALTER TABLE ConstructionProjects
ADD COLUMN ClientID INT,
ADD FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE SET NULL;
```

This schema adheres to best practices, is scalable, and includes proper relationships between tables for construction projects and equipment hire management.
