"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Develop a database schema to manage packaging product inventories and export destinations, inspired by Osku's wide portfolio and global distribution.
Generated: DETERMINISTIC_3bbaa902592bb883
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing packaging product inventories
-- and export destinations.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ExportDestinations CASCADE;
DROP TABLE IF EXISTS PackagingProducts CASCADE;
DROP TABLE IF EXISTS Inventory CASCADE;

-- Create a table for export destinations
CREATE TABLE ExportDestinations (
    id SERIAL PRIMARY KEY,           -- Unique identifier for each destination
    country VARCHAR(100) NOT NULL,  -- Country name for the export destination
    city VARCHAR(100) NOT NULL,     -- City name for more specific targeting
    region VARCHAR(100),             -- Optional region or state for the destination
    postal_code VARCHAR(20),         -- Postal code for the destination
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for packaging products
CREATE TABLE PackagingProducts (
    id SERIAL PRIMARY KEY,                       -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                  -- Name of the packaging product
    dimensions VARCHAR(255) NOT NULL,            -- Dimensions of the product (e.g., LxWxH)
    weight DECIMAL(10, 2) NOT NULL,              -- Weight of the product in kilograms
    material VARCHAR(100) NOT NULL,              -- Material used for the packaging
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Create a table for inventory that links packaging products to their destinations
CREATE TABLE Inventory (
    id SERIAL PRIMARY KEY,                              -- Unique identifier for inventory record
    product_id INT NOT NULL REFERENCES PackagingProducts(id) ON DELETE CASCADE, -- Foreign key to packaging products
    destination_id INT NOT NULL REFERENCES ExportDestinations(id) ON DELETE CASCADE, -- Foreign key to export destinations
    quantity INT NOT NULL CHECK (quantity >= 0),       -- Number of items in stock (must be non-negative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- Timestamp for the last update
);

-- Create indexes to improve search performance
CREATE INDEX idx_product_name ON PackagingProducts(name);
CREATE INDEX idx_destination_country ON ExportDestinations(country);
```
