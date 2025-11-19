"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Create a SQL database schema for storing information about 4x4 vehicle parts, including categories, brands, and product specifications."
Generated: DETERMINISTIC_be063f6906c2ca1b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about 4x4 vehicle parts

-- Create the database
CREATE DATABASE IF NOT EXISTS VehiclePartsDB;

-- Use the created database
USE VehiclePartsDB;

-- Table to store categories of vehicle parts
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store brands of vehicle parts
CREATE TABLE IF NOT EXISTS Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each brand
    BrandName VARCHAR(100) NOT NULL,            -- Name of the brand
    Website VARCHAR(255),                        -- Website of the brand
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the brand was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store specifications of vehicle parts
CREATE TABLE IF NOT EXISTS Specifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    PartID INT NOT NULL,                            -- Foreign key referencing Parts table
    KeyName VARCHAR(100) NOT NULL,                 -- Name of the specification key
    Value VARCHAR(255) NOT NULL,                   -- Value of the specification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PartID) REFERENCES Parts(PartID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store vehicle parts
CREATE TABLE IF NOT EXISTS Parts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each part
    PartName VARCHAR(100) NOT NULL,                -- Name of the part
    CategoryID INT NOT NULL,                        -- Foreign key referencing Categories table
    BrandID INT NOT NULL,                           -- Foreign key referencing Brands table
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the part
    StockQuantity INT NOT NULL DEFAULT 0,          -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the part was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_part_name ON Parts(PartName);
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_brand_name ON Brands(BrandName);
```
