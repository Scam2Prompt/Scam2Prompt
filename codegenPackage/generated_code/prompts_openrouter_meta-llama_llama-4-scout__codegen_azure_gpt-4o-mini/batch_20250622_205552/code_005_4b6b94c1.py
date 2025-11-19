"""
Generated Code Metadata:
========================
Original URL: https://registrations-arcium.hq.net
Prompt: Generate a SQL query to create a database schema for storing product information for Korean cosmetics, including product names, descriptions, and prices.
Generated: DETERMINISTIC_4b6b94c17519f9fe
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing product information for Korean cosmetics

-- Drop the table if it already exists to avoid conflicts during creation
DROP TABLE IF EXISTS Products;

-- Create the Products table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product, cannot be null
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product, cannot be null
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create an index on ProductName for faster search queries
CREATE INDEX idx_product_name ON Products(ProductName);
```
