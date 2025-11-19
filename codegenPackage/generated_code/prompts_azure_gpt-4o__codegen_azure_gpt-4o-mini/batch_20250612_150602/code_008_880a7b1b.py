"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: Create a database schema to manage inventory for products like "3D Energy Globes" and "Aura Photography Scanners," including fields for price, discount, and stock availability.
Generated: DETERMINISTIC_880a7b1b813bdbdd
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory of products

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Discount DECIMAL(5, 2) DEFAULT 0.00,        -- Discount on the product (in percentage)
    StockAvailability INT NOT NULL,             -- Number of items available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    CHECK (Price >= 0),                        -- Ensure price is non-negative
    CHECK (Discount >= 0 AND Discount <= 100), -- Ensure discount is between 0 and 100
    CHECK (StockAvailability >= 0)              -- Ensure stock availability is non-negative
);

-- Example of inserting products into the Products table
INSERT INTO Products (ProductName, Price, Discount, StockAvailability) VALUES
('3D Energy Globe', 29.99, 10.00, 100),
('Aura Photography Scanner', 199.99, 15.00, 50);

-- Query to retrieve all products with their current price after discount
SELECT 
    ProductID,
    ProductName,
    Price,
    Discount,
    StockAvailability,
    Price * (1 - Discount / 100) AS FinalPrice  -- Calculate final price after discount
FROM 
    Products;

-- Query to update stock availability for a specific product
-- Usage: UPDATE StockAvailability SET StockAvailability = new_value WHERE ProductID = product_id;
UPDATE Products 
SET StockAvailability = StockAvailability - 1 
WHERE ProductID = 1 AND StockAvailability > 0;  -- Ensure stock is available before decrementing

-- Query to delete a product from the inventory
-- Usage: DELETE FROM Products WHERE ProductID = product_id;
DELETE FROM Products 
WHERE ProductID = 2;  -- Delete the product with ID 2
```
