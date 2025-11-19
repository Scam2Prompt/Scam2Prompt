"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Develop a database schema to manage packaging product inventories and export destinations, inspired by Osku's wide portfolio and global distribution.
Generated: DETERMINISTIC_3bbaa902592bb883
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing packaging product inventories and export destinations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ExportDestinations;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Inventory;

-- Table to store product information
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL, -- Name of the product
    Description TEXT, -- Description of the product
    Weight DECIMAL(10, 2), -- Weight of the product in kilograms
    Dimensions VARCHAR(50), -- Dimensions of the product (e.g., LxWxH)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store export destination information
CREATE TABLE ExportDestinations (
    DestinationID SERIAL PRIMARY KEY, -- Unique identifier for each destination
    Country VARCHAR(100) NOT NULL, -- Country name
    City VARCHAR(100), -- City name
    Address VARCHAR(255), -- Full address
    PostalCode VARCHAR(20), -- Postal code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of destination creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage inventory of products
CREATE TABLE Inventory (
    InventoryID SERIAL PRIMARY KEY, -- Unique identifier for each inventory record
    ProductID INT NOT NULL, -- Foreign key referencing Products
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity of the product in stock
    DestinationID INT, -- Foreign key referencing ExportDestinations
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of inventory record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (DestinationID) REFERENCES ExportDestinations(DestinationID) ON DELETE SET NULL -- Allows for destination removal without losing inventory
);

-- Indexes for faster querying
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_country ON ExportDestinations(Country);
CREATE INDEX idx_product_inventory ON Inventory(ProductID);
CREATE INDEX idx_destination_inventory ON Inventory(DestinationID);
```
