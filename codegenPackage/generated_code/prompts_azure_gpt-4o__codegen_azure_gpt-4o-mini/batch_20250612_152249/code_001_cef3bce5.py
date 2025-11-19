"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Create a database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns, including tables for yarn types, machinery details, and customer orders.
Generated: DETERMINISTIC_cef3bce514e7db0c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns

-- Create a table for yarn types
CREATE TABLE YarnTypes (
    YarnTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each yarn type
    YarnName VARCHAR(100) NOT NULL,             -- Name of the yarn type
    Color VARCHAR(50) NOT NULL,                  -- Color of the yarn
    Weight DECIMAL(5,2) NOT NULL,                -- Weight of the yarn in grams
    FiberContent VARCHAR(100) NOT NULL,          -- Fiber content description
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for machinery details
CREATE TABLE Machinery (
    MachineryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each machine
    MachineName VARCHAR(100) NOT NULL,           -- Name of the machine
    MachineType VARCHAR(50) NOT NULL,             -- Type of the machine (e.g., spinning, weaving)
    PurchaseDate DATE NOT NULL,                   -- Date when the machine was purchased
    Status ENUM('Operational', 'Maintenance', 'Decommissioned') NOT NULL, -- Current status of the machine
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for customer orders
CREATE TABLE CustomerOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer
    OrderDate DATE NOT NULL,                       -- Date when the order was placed
    YarnTypeID INT NOT NULL,                       -- Foreign key referencing YarnTypes
    Quantity INT NOT NULL,                         -- Quantity of yarn ordered
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL, -- Current status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (YarnTypeID) REFERENCES YarnTypes(YarnTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on YarnTypes for faster searches by YarnName
CREATE INDEX idx_yarn_name ON YarnTypes(YarnName);

-- Create an index on CustomerOrders for faster searches by OrderDate
CREATE INDEX idx_order_date ON CustomerOrders(OrderDate);
```
