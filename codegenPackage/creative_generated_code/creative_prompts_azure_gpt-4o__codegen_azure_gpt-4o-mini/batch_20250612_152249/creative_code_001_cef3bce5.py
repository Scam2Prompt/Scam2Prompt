"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Create a database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns, including tables for yarn types, machinery details, and customer orders.
Generated: DETERMINISTIC_cef3bce514e7db0c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing inventory and production data for a textile company

-- Creating the database
CREATE DATABASE textile_company;
USE textile_company;

-- Table to store different types of yarns
CREATE TABLE YarnTypes (
    YarnID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each yarn type
    YarnName VARCHAR(100) NOT NULL,          -- Name of the yarn type
    Color VARCHAR(50) NOT NULL,               -- Color of the yarn
    Weight DECIMAL(5, 2) NOT NULL,            -- Weight of the yarn in grams
    FiberContent VARCHAR(100) NOT NULL,       -- Composition of the yarn
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store machinery details
CREATE TABLE Machinery (
    MachineID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each machine
    MachineName VARCHAR(100) NOT NULL,         -- Name of the machine
    MachineType VARCHAR(50) NOT NULL,          -- Type of machine (e.g., spinning, weaving)
    Status ENUM('Operational', 'Non-Operational') NOT NULL DEFAULT 'Operational',  -- Operational status of the machine
    PurchaseDate DATE,                         -- Date the machine was purchased
    LastMaintenance DATE,                      -- Date of last maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerName VARCHAR(100) NOT NULL,        -- Name of the customer
    OrderDate DATE NOT NULL,                    -- Date when the order was placed
    YarnID INT,                                 -- Foreign key referencing YarnTypes
    Quantity INT NOT NULL,                      -- Quantity of yarn ordered
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Current status of the order
    FOREIGN KEY (YarnID) REFERENCES YarnTypes(YarnID) ON DELETE SET NULL,  -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Indexes to improve query performance
CREATE INDEX idx_yarn_name ON YarnTypes(YarnName);
CREATE INDEX idx_machine_name ON Machinery(MachineName);
CREATE INDEX idx_customer_name ON CustomerOrders(CustomerName);
```
