"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Develop a database schema in SQL to store product details like "Karma 3MT DOLAPLI ÇALIŞMA TEZGAHI," including fields for dimensions, material type, weight, and price.
Generated: DETERMINISTIC_34bf44de82231523
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for storing product details

-- Create a new database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS ProductCatalog;

-- Use the newly created database
USE ProductCatalog;

-- Create a table to store product details
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Dimensions VARCHAR(100) NOT NULL,         -- Dimensions of the product (e.g., LxWxH)
    MaterialType VARCHAR(100) NOT NULL,       -- Type of material used
    Weight DECIMAL(10, 2) NOT NULL,           -- Weight of the product in kilograms
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product in currency
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT chk_Weight CHECK (Weight >= 0), -- Ensure weight is non-negative
    CONSTRAINT chk_Price CHECK (Price >= 0)    -- Ensure price is non-negative
);

-- Example of an insert statement to add a product 
-- Uncomment the following line to insert a sample product into the table
-- INSERT INTO Products (ProductName, Dimensions, MaterialType, Weight, Price) 
-- VALUES ('Karma 3MT DOLAPLI ÇALIŞMA TEZGAHI', '150x75x75', 'Wood', 50.00, 499.99);

-- Query to select all products
-- Use this query to retrieve all product details from the database
-- SELECT * FROM Products;
```
