"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Create a SQL query to manage inventory levels for pet supplies, including products like "Tapete Higiênico Premium Chalesco", with varying quantities and prices.
Generated: DETERMINISTIC_f89e2eb32ceb38a4
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to manage inventory levels for pet supplies
CREATE TABLE PetSuppliesInventory (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity in stock, must be non-negative
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the inventory table
INSERT INTO PetSuppliesInventory (ProductName, Quantity, Price)
VALUES 
    ('Tapete Higiênico Premium Chalesco', 100, 49.99),
    ('Dog Food Premium', 50, 89.99),
    ('Cat Litter Ultra Absorbent', 200, 29.99);

-- Query to retrieve all products with their inventory levels and prices
SELECT 
    ProductID,
    ProductName,
    Quantity,
    Price,
    LastUpdated
FROM 
    PetSuppliesInventory;

-- Update the quantity of a specific product (example: reduce quantity of "Tapete Higiênico Premium Chalesco" by 10)
UPDATE PetSuppliesInventory
SET Quantity = Quantity - 10
WHERE ProductName = 'Tapete Higiênico Premium Chalesco' AND Quantity >= 10;

-- Handle cases where the quantity might drop below zero (error prevention)
-- Example: Attempting to reduce quantity of a product that doesn't have enough stock
UPDATE PetSuppliesInventory
SET Quantity = CASE 
    WHEN Quantity >= 10 THEN Quantity - 10
    ELSE Quantity -- No change if insufficient stock
END
WHERE ProductName = 'Tapete Higiênico Premium Chalesco';

-- Delete a product from the inventory (example: remove "Dog Food Premium")
DELETE FROM PetSuppliesInventory
WHERE ProductName = 'Dog Food Premium';

-- Add a new product to the inventory
INSERT INTO PetSuppliesInventory (ProductName, Quantity, Price)
VALUES ('Bird Cage Deluxe', 30, 199.99);

-- Query to check low-stock products (example: products with quantity less than 20)
SELECT 
    ProductID,
    ProductName,
    Quantity,
    Price,
    LastUpdated
FROM 
    PetSuppliesInventory
WHERE 
    Quantity < 20;

-- Ensure the table structure is optimized for production use
-- Add an index on ProductName for faster lookups
CREATE INDEX idx_ProductName ON PetSuppliesInventory (ProductName);
```
