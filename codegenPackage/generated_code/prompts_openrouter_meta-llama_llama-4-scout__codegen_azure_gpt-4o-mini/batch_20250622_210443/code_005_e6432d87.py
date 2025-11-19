"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Design a simple database schema to store information about hydraulic, sanitary, gas, and firefighting networks, including their designs, constructions, and maintenance records, inspired by the services offered by Espinel y Cia."
Generated: DETERMINISTIC_e6432d87387fc3ee
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about hydraulic, sanitary, gas, and firefighting networks

CREATE DATABASE NetworkManagement;

USE NetworkManagement;

-- Table to store information about different types of networks
CREATE TABLE Networks (
    NetworkID INT AUTO_INCREMENT PRIMARY KEY,
    NetworkType ENUM('Hydraulic', 'Sanitary', 'Gas', 'Firefighting') NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store design information for each network
CREATE TABLE Designs (
    DesignID INT AUTO_INCREMENT PRIMARY KEY,
    NetworkID INT,
    DesignDetails TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (NetworkID) REFERENCES Networks(NetworkID) ON DELETE CASCADE
);

-- Table to store construction records for each network
CREATE TABLE Constructions (
    ConstructionID INT AUTO_INCREMENT PRIMARY KEY,
    NetworkID INT,
    ConstructionDate DATE NOT NULL,
    ContractorName VARCHAR(255),
    Cost DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (NetworkID) REFERENCES Networks(NetworkID) ON DELETE CASCADE
);

-- Table to store maintenance records for each network
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY,
    NetworkID INT,
    MaintenanceDate DATE NOT NULL,
    Description TEXT,
    PerformedBy VARCHAR(255),
    Cost DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (NetworkID) REFERENCES Networks(NetworkID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_network_type ON Networks(NetworkType);
CREATE INDEX idx_network_id ON Designs(NetworkID);
CREATE INDEX idx_construction_network ON Constructions(NetworkID);
CREATE INDEX idx_maintenance_network ON MaintenanceRecords(NetworkID);
```
