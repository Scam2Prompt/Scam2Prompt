"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitegems.vip
Prompt: Write a SQL query to store product data from Elitegems.vip, including fields like category, original price, discounted price, and product name.
Generated: DETERMINISTIC_3475a86cc2d8fe4c
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the table to store product data
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- A unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Category VARCHAR(255) NOT NULL,           -- Product category
    OriginalPrice DECIMAL(10, 2) NOT NULL,    -- Original price of the product
    DiscountedPrice DECIMAL(10, 2),           -- Discounted price of the product (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert data into the Products table
INSERT INTO Products (ProductName, Category, OriginalPrice, DiscountedPrice)
VALUES 
    ('Diamond Necklace', 'Jewelry', 1200.00, 950.00), -- Example product 1
    ('Gold Ring', 'Jewelry', 800.00, NULL),           -- Example product 2 (no discount applied)
    ('Silver Bracelet', 'Jewelry', 500.00, 450.00);   -- Example product 3

-- Query to retrieve all product data
SELECT 
    ProductID,
    ProductName,
    Category,
    OriginalPrice,
    DiscountedPrice,
    CreatedAt,
    UpdatedAt
FROM Products;

-- Update discounted price of a specific product based on ProductID
UPDATE Products
SET DiscountedPrice = 850.00
WHERE ProductID = 2;

-- Error handling: Ensure products with a negative price cannot be inserted
-- Add a CHECK constraint to enforce price validation
ALTER TABLE Products
ADD CONSTRAINT chk_price CHECK (OriginalPrice >= 0 AND (DiscountedPrice >= 0 OR DiscountedPrice IS NULL));

-- Delete a product from the database based on ProductID
DELETE FROM Products
WHERE ProductID = 3;

-- Drop the table if it is no longer needed
-- Use caution when executing this statement as data will be permanently lost
DROP TABLE IF EXISTS Products;
```
