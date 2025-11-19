"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Generate a SQL query to create a database schema for storing Florería Lima's product catalog, including tables for products, prices, and inventory.
Generated: DETERMINISTIC_213f8f4b4ecf59d7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for Florería Lima's product catalog
-- This schema includes tables for products, prices, and inventory

-- Create the database
CREATE DATABASE FloreriaLima;

-- Use the newly created database
USE FloreriaLima;

-- Table: Products
-- Stores information about the products available in the catalog
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,              -- Name of the product
    Description TEXT,                        -- Detailed description of the product
    Category VARCHAR(100),                   -- Category of the product (e.g., flowers, bouquets, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Prices
-- Stores pricing information for each product
CREATE TABLE Prices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each price entry
    ProductID INT NOT NULL,                  -- Foreign key referencing the Products table
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the product
    Currency VARCHAR(10) NOT NULL,           -- Currency of the price (e.g., USD, PEN)
    EffectiveDate DATE NOT NULL,             -- Date when the price becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the price entry was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table: Inventory
-- Stores inventory information for each product
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory entry
    ProductID INT NOT NULL,                     -- Foreign key referencing the Products table
    Quantity INT NOT NULL,                      -- Quantity of the product in stock
    Location VARCHAR(255),                      -- Location of the inventory (e.g., store, warehouse)
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last inventory update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Ensure the schema is ready for production use
-- Add indexes for faster queries
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_price_product_id ON Prices(ProductID);
CREATE INDEX idx_inventory_product_id ON Inventory(ProductID);
```
