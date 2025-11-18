"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Generate a database schema for managing ENL Consortium's port operations, including tables for container stacking, warehouse space allocation, and cargo handling.
Generated: DETERMINISTIC_87318434d1d2a534
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for ENL Consortium Port Operations

-- Create a new database for the ENL Consortium
CREATE DATABASE ENL_Consortium_Port_Operations;

-- Use the created database
USE ENL_Consortium_Port_Operations;

-- Table for managing container stacking
CREATE TABLE Container_Stacking (
    container_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each container
    container_number VARCHAR(50) NOT NULL,       -- Container number (e.g., CAIU1234567)
    stack_id INT NOT NULL,                        -- Identifier for the stack position
    arrival_date DATETIME NOT NULL,              -- Date and time the container arrived
    status ENUM('stacked', 'removed', 'pending') NOT NULL, -- Current status of the container
    FOREIGN KEY (stack_id) REFERENCES Stacks(stack_id) -- Foreign key referencing Stacks table
);

-- Table for managing stack positions
CREATE TABLE Stacks (
    stack_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each stack
    location VARCHAR(100) NOT NULL,               -- Location description for the stack
    max_capacity INT NOT NULL,                     -- Maximum capacity of the stack
    current_load INT DEFAULT 0,                   -- Current load in the stack
    CHECK (current_load <= max_capacity)          -- Ensure current load does not exceed capacity
);

-- Table for managing warehouse space allocation
CREATE TABLE Warehouse_Space (
    space_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for warehouse space
    location VARCHAR(100) NOT NULL,                -- Location description of the warehouse
    capacity INT NOT NULL,                          -- Total capacity of the warehouse space
    current_utilization INT DEFAULT 0,             -- Current utilization of the warehouse space
    CHECK (current_utilization <= capacity)        -- Ensure current utilization does not exceed capacity
);

-- Table for managing cargo handling operations
CREATE TABLE Cargo_Handling (
    handling_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each cargo handling operation
    container_id INT NOT NULL,                      -- Identifier for the handled container
    operation_type ENUM('load', 'unload', 'transfer') NOT NULL, -- Type of cargo handling operation
    operation_date DATETIME NOT NULL,              -- Date and time of the operation
    operator_name VARCHAR(100) NOT NULL,           -- Name of the operator handling the cargo
    FOREIGN KEY (container_id) REFERENCES Container_Stacking(container_id) -- Foreign key referencing Container_Stacking table
);

-- Table for tracking cargo status
CREATE TABLE Cargo_Status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each status entry
    container_id INT NOT NULL,                      -- Identifier for the container being tracked
    status ENUM('in transit', 'at warehouse', 'delivered', 'damaged') NOT NULL, -- Current status of the cargo
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of the status update
    FOREIGN KEY (container_id) REFERENCES Container_Stacking(container_id) -- Foreign key referencing Container_Stacking table
);

-- Indexing for performance optimization
CREATE INDEX idx_container_number ON Container_Stacking (container_number);
CREATE INDEX idx_stack_location ON Stacks (location);
CREATE INDEX idx_warehouse_location ON Warehouse_Space (location);
CREATE INDEX idx_operator_name ON Cargo_Handling (operator_name);
```
