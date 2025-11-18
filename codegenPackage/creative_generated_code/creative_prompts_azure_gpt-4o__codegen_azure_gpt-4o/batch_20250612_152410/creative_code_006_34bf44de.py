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
-- Database schema for storing product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Dimensions VARCHAR(100),                    -- Dimensions of the product (e.g., "3m x 2m x 1m")
    MaterialType VARCHAR(100),                  -- Material type (e.g., "Steel", "Wood")
    Weight DECIMAL(10, 2),                      -- Weight of the product in kilograms
    Price DECIMAL(10, 2),                       -- Price of the product in the applicable currency
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp indicating when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Indexes for faster querying
CREATE INDEX idx_ProductName ON Products(ProductName);
CREATE INDEX idx_MaterialType ON Products(MaterialType);

-- Example error handling: If table already exists, drop it before creating a new one
-- NOTE: This line is optional and can be removed in production
DROP TABLE IF EXISTS Products;

-- Example data insertion for testing
INSERT INTO Products (ProductName, Dimensions, MaterialType, Weight, Price)
VALUES
    ('Karma 3MT DOLAPLI ÇALIŞMA TEZGAHI', '3m x 2m x 1m', 'Steel', 150.50, 2500.00),
    ('Modern Wooden Desk', '1.5m x 0.75m x 0.75m', 'Wood', 45.00, 750.00);

-- Query the table to verify data
SELECT * FROM Products;
```
