"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Write a SQL query to organize furniture inventory data into categories such as "Domestic Furniture," "Office Furniture," and "School Furniture," based on the product range described by Navkar Furniture.
Generated: DETERMINISTIC_83399e4fe200819a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for furniture inventory
CREATE DATABASE FurnitureInventory;

-- Use the database
USE FurnitureInventory;

-- Create a table for furniture products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductRange VARCHAR(255) NOT NULL,
    Category VARCHAR(255) DEFAULT NULL,
    Quantity INT NOT NULL DEFAULT 0,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ProductID)
);

-- Insert sample data into the products table
INSERT INTO Products (ProductName, ProductRange, Quantity, Price)
VALUES 
('Sofa Set', 'Domestic', 10, 5000.00),
('Office Chair', 'Office', 20, 2000.00),
('School Desk', 'School', 30, 1000.00),
('Dining Table', 'Domestic', 15, 3000.00),
('Conference Table', 'Office', 5, 8000.00),
('Classroom Chair', 'School', 40, 800.00);

-- Create a stored procedure to categorize products
DELIMITER $$
CREATE PROCEDURE CategorizeProducts()
BEGIN
    -- Update categories based on product range
    UPDATE Products
    SET Category = 
        CASE 
            WHEN ProductRange = 'Domestic' THEN 'Domestic Furniture'
            WHEN ProductRange = 'Office' THEN 'Office Furniture'
            WHEN ProductRange = 'School' THEN 'School Furniture'
            ELSE 'Unknown'
        END;
END$$
DELIMITER ;

-- Call the stored procedure to categorize products
CALL CategorizeProducts();

-- Select categorized products
SELECT 
    ProductID,
    ProductName,
    ProductRange,
    Category,
    Quantity,
    Price
FROM 
    Products
ORDER BY 
    Category;
```
