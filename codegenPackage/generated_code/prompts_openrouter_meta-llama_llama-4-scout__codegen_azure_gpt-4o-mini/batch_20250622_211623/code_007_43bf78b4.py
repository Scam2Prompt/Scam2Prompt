"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: "Design a simple database schema to track maintenance and service requests for Climax Polska's material handling equipment."
Generated: DETERMINISTIC_43bf78b4f5f90907
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking maintenance and service requests for Climax Polska's material handling equipment

-- Create a table to store information about the equipment
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each piece of equipment
    EquipmentName VARCHAR(255) NOT NULL,         -- Name of the equipment
    EquipmentType VARCHAR(100) NOT NULL,         -- Type of the equipment (e.g., forklift, conveyor)
    PurchaseDate DATE NOT NULL,                   -- Date when the equipment was purchased
    LastMaintenanceDate DATE,                     -- Date of the last maintenance performed
    Status ENUM('Active', 'Inactive') DEFAULT 'Active'  -- Current status of the equipment
);

-- Create a table to store maintenance and service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service request
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment
    RequestDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when the request was made
    ServiceType VARCHAR(100) NOT NULL,           -- Type of service requested (e.g., repair, inspection)
    Description TEXT,                             -- Detailed description of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the request
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store maintenance personnel information
CREATE TABLE MaintenancePersonnel (
    PersonnelID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each maintenance personnel
    Name VARCHAR(255) NOT NULL,                   -- Name of the personnel
    ContactInfo VARCHAR(255),                      -- Contact information (phone/email)
    Specialization VARCHAR(100)                   -- Area of specialization (e.g., electrical, mechanical)
);

-- Create a table to log maintenance activities
CREATE TABLE MaintenanceLogs (
    LogID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each maintenance log
    RequestID INT NOT NULL,                        -- Foreign key referencing ServiceRequests
    PersonnelID INT NOT NULL,                      -- Foreign key referencing MaintenancePersonnel
    MaintenanceDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when maintenance was performed
    Notes TEXT,                                   -- Additional notes about the maintenance performed
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (PersonnelID) REFERENCES MaintenancePersonnel(PersonnelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_equipment_status ON Equipment(Status);
CREATE INDEX idx_service_request_status ON ServiceRequests(Status);
CREATE INDEX idx_maintenance_personnel ON MaintenancePersonnel(Name);
```
