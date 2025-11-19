"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Generate a SQL query to manage product inventory for an e-commerce platform with product categories, prices, and descriptions, like the ones listed on Feresplast.
Generated: DETERMINISTIC_56fe5d98626c64c2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to manage product inventory for an e-commerce platform
CREATE TABLE ProductInventory (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Category VARCHAR(100) NOT NULL,           -- Category of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Description TEXT,                         -- Description of the product
    StockQuantity INT NOT NULL,               -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the ProductInventory table
INSERT INTO ProductInventory (ProductName, Category, Price, Description, StockQuantity)
VALUES
    ('Plastic Container', 'Storage', 19.99, 'Durable plastic container for storage.', 100),
    ('Metal Cage', 'Pet Supplies', 49.99, 'Sturdy metal cage for small pets.', 50),
    ('Wooden Shelf', 'Furniture', 89.99, 'Elegant wooden shelf for home decor.', 20),
    ('Garden Hose', 'Outdoor', 25.99, 'Flexible garden hose with adjustable nozzle.', 75);

-- Query to retrieve all products with their details
SELECT * FROM ProductInventory;

-- Query to retrieve products within a specific price range
SELECT * FROM ProductInventory
WHERE Price BETWEEN 20 AND 50;

-- Query to update the stock quantity of a specific product
UPDATE ProductInventory
SET StockQuantity = StockQuantity - 1
WHERE ProductID = 1 AND StockQuantity > 0;

-- Error handling: Ensure stock quantity does not go below zero
UPDATE ProductInventory
SET StockQuantity = GREATEST(StockQuantity - 1, 0)
WHERE ProductID = 1;

-- Query to delete a product from the inventory
DELETE FROM ProductInventory
WHERE ProductID = 4;

-- Query to retrieve products by category
SELECT * FROM ProductInventory
WHERE Category = 'Pet Supplies';

-- Query to add a new product to the inventory
INSERT INTO ProductInventory (ProductName, Category, Price, Description, StockQuantity)
VALUES ('Ceramic Bowl', 'Kitchenware', 15.99, 'Stylish ceramic bowl for serving meals.', 30);

-- Query to update product details
UPDATE ProductInventory
SET Price = 99.99, Description = 'Updated description for the wooden shelf.'
WHERE ProductID = 3;

-- Query to retrieve products with low stock (threshold: 10 units)
SELECT * FROM ProductInventory
WHERE StockQuantity < 10;

-- Query to retrieve the total number of products in each category
SELECT Category, COUNT(*) AS TotalProducts
FROM ProductInventory
GROUP BY Category;

-- Query to calculate the total value of inventory for each category
SELECT Category, SUM(Price * StockQuantity) AS TotalInventoryValue
FROM ProductInventory
GROUP BY Category;
```
