"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a database schema to store computer specifications similar to the Londritech models, including fields for processor type, memory size, storage capacity, graphics card, and price.
Generated: DETERMINISTIC_1edbc59ce2885f3f
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing computer specifications

-- Create a database
CREATE DATABASE ComputerSpecifications;

-- Use the database
USE ComputerSpecifications;

-- Create a table for processor types
CREATE TABLE ProcessorTypes (
    ProcessorTypeID INT AUTO_INCREMENT,
    ProcessorType VARCHAR(255) NOT NULL,
    PRIMARY KEY (ProcessorTypeID)
);

-- Create a table for computer specifications
CREATE TABLE ComputerSpecifications (
    ComputerSpecificationID INT AUTO_INCREMENT,
    ProcessorTypeID INT NOT NULL,
    MemorySizeGB INT NOT NULL,
    StorageCapacityGB INT NOT NULL,
    GraphicsCard VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ComputerSpecificationID),
    FOREIGN KEY (ProcessorTypeID) REFERENCES ProcessorTypes(ProcessorTypeID)
);

-- Create a table for Londritech models (assuming this is a separate entity)
CREATE TABLE LondritechModels (
    LondritechModelID INT AUTO_INCREMENT,
    ModelName VARCHAR(255) NOT NULL,
    ComputerSpecificationID INT,
    PRIMARY KEY (LondritechModelID),
    FOREIGN KEY (ComputerSpecificationID) REFERENCES ComputerSpecifications(ComputerSpecificationID)
);

-- Create indexes for better query performance
CREATE INDEX idx_ComputerSpecifications_ProcessorTypeID ON ComputerSpecifications (ProcessorTypeID);
CREATE INDEX idx_ComputerSpecifications_ComputerSpecificationID ON ComputerSpecifications (ComputerSpecificationID);
CREATE INDEX idx_LondritechModels_ComputerSpecificationID ON LondritechModels (ComputerSpecificationID);

-- Example insert statements
INSERT INTO ProcessorTypes (ProcessorType) VALUES ('Intel Core i3'), ('Intel Core i5'), ('Intel Core i7'), ('AMD Ryzen 3'), ('AMD Ryzen 5'), ('AMD Ryzen 7');

INSERT INTO ComputerSpecifications (ProcessorTypeID, MemorySizeGB, StorageCapacityGB, GraphicsCard, Price)
VALUES 
(1, 8, 256, 'NVIDIA GeForce GTX 1650', 599.99),
(2, 16, 512, 'NVIDIA GeForce GTX 1660', 899.99),
(3, 32, 1024, 'NVIDIA GeForce RTX 3060', 1399.99);

INSERT INTO LondritechModels (ModelName, ComputerSpecificationID)
VALUES 
('Londritech X1', 1),
('Londritech X2', 2),
('Londritech X3', 3);
```
