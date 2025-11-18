"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupport.tfryx.xyz
Prompt: Create a SQL query to store and retrieve product data, including discounts and stock availability, for items like "PINI-KAY brikettiklapi – 960 kg eurolava" from https://livesupport.tfryx.xyz.
Generated: DETERMINISTIC_73b75ee1d444468d
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Discount DECIMAL(5, 2) DEFAULT 0.00,      -- Discount on the product (percentage)
    Stock INT NOT NULL DEFAULT 0,             -- Stock availability
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert a sample product into the table
INSERT INTO Products (ProductName, Description, Price, Discount, Stock)
VALUES 
(
    'PINI-KAY brikettiklapi – 960 kg eurolava', 
    'Compressed wood briquettes for heating, 960 kg per euro pallet.', 
    250.00,   -- Example price
    10.00,    -- Example discount of 10%
    100       -- Example stock availability
);

-- Query to retrieve all products with their effective prices (calculated after discount) and stock status
SELECT 
    ProductID, 
    ProductName, 
    Description, 
    Price AS OriginalPrice, 
    Discount, 
    (Price - (Price * Discount / 100)) AS EffectivePrice, -- Calculate price after discount
    Stock, 
    CASE 
        WHEN Stock > 0 THEN 'In Stock' 
        ELSE 'Out of Stock' 
    END AS StockStatus, -- Check stock availability
    CreatedAt, 
    UpdatedAt
FROM 
    Products
WHERE 
    ProductName LIKE '%PINI-KAY brikettiklapi%'; -- Filter by product name (partial match)

-- Note: Ensure appropriate indexing strategies and validations are applied in production environments
```
