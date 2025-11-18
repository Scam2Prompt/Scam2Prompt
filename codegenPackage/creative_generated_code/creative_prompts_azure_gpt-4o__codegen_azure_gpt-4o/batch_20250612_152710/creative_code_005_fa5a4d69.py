"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Create a database schema for tracking logistics operations across different regimes, such as industrial zones, free trade zones, and fiscal storage zones, as described by PLM.
Generated: DETERMINISTIC_fa5a4d692b89d327
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tracking Logistics Operations

-- Table to store the details of different regimes
CREATE TABLE Regimes (
    RegimeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each regime
    RegimeName VARCHAR(255) NOT NULL,        -- Name of the regime (e.g., Industrial Zone, Free Trade Zone)
    RegimeType ENUM('Industrial Zone', 'Free Trade Zone', 'Fiscal Storage Zone') NOT NULL, -- Type of regime
    Description TEXT,                        -- Detailed description of the regime
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the regime was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store logistics operations
CREATE TABLE LogisticsOperations (
    OperationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the operation
    RegimeID INT NOT NULL,                      -- Foreign key referencing Regimes table
    OperationName VARCHAR(255) NOT NULL,        -- Name of the logistics operation
    OperationType ENUM('Import', 'Export', 'Storage', 'Transfer') NOT NULL, -- Type of operation
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Current status of operation
    StartDate DATE NOT NULL,                    -- Start date of the operation
    EndDate DATE,                               -- End date of the operation (can be NULL for ongoing operations)
    Notes TEXT,                                 -- Additional notes regarding the operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the operation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (RegimeID) REFERENCES Regimes(RegimeID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Table to track the entities involved in logistics operations
CREATE TABLE Entities (
    EntityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each entity
    EntityName VARCHAR(255) NOT NULL,        -- Name of the entity (e.g., company name)
    EntityType ENUM('Manufacturer', 'Distributor', 'Retailer', 'Customs') NOT NULL, -- Type of entity
    ContactInfo TEXT,                        -- Contact details of the entity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entity was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to track relationships between logistics operations and entities
CREATE TABLE OperationEntities (
    OperationEntityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    OperationID INT NOT NULL,                         -- Foreign key referencing LogisticsOperations table
    EntityID INT NOT NULL,                            -- Foreign key referencing Entities table
    Role ENUM('Initiator', 'Handler', 'Supervisor', 'Recipient') NOT NULL, -- Role of the entity in the operation
    Notes TEXT,                                       -- Additional notes regarding the entity's involvement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (OperationID) REFERENCES LogisticsOperations(OperationID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key constraint
    FOREIGN KEY (EntityID) REFERENCES Entities(EntityID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Indexes for improving query performance
CREATE INDEX idx_regime_type ON Regimes(RegimeType);
CREATE INDEX idx_operation_type ON LogisticsOperations(OperationType);
CREATE INDEX idx_entity_type ON Entities(EntityType);

-- Error handling for ensuring transaction safety is typically handled in application logic interacting with the database.
-- Example: Using BEGIN TRANSACTION, COMMIT, and ROLLBACK for atomic operations when inserting or updating multiple tables.
```
