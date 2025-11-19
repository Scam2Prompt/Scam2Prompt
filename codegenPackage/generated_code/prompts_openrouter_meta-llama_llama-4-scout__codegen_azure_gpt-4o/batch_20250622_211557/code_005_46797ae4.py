"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: "Design a database schema for an e-commerce platform like EcoSwap, including tables for devices (e.g., watches, jewelry, Apple devices), their specifications, and pricing."
Generated: DETERMINISTIC_46797ae4360ebeec
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform like EcoSwap

-- Table to store device categories
CREATE TABLE DeviceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Watches, Jewelry, Apple Devices)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store devices
CREATE TABLE Devices (
    DeviceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each device
    CategoryID INT NOT NULL,                   -- Foreign key referencing DeviceCategories
    DeviceName VARCHAR(255) NOT NULL,          -- Name of the device (e.g., Apple Watch Series 7)
    Description TEXT,                          -- Detailed description of the device
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the device
    Stock INT NOT NULL DEFAULT 0,              -- Number of items available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the device was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the device was last updated
    FOREIGN KEY (CategoryID) REFERENCES DeviceCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store device specifications
CREATE TABLE DeviceSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    DeviceID INT NOT NULL,                          -- Foreign key referencing Devices
    SpecificationKey VARCHAR(255) NOT NULL,         -- Key for the specification (e.g., Color, Weight, Battery Life)
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value for the specification (e.g., Black, 150g, 18 hours)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the specification was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the specification was last updated
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store pricing history for devices
CREATE TABLE PricingHistory (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each pricing record
    DeviceID INT NOT NULL,                          -- Foreign key referencing Devices
    OldPrice DECIMAL(10, 2) NOT NULL,               -- Previous price of the device
    NewPrice DECIMAL(10, 2) NOT NULL,               -- Updated price of the device
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price change occurred
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON DeviceCategories(CategoryName); -- Index for quick lookup of categories by name
CREATE INDEX idx_device_name ON Devices(DeviceName);              -- Index for quick lookup of devices by name
CREATE INDEX idx_specification_key ON DeviceSpecifications(SpecificationKey); -- Index for quick lookup of specifications by key
```
