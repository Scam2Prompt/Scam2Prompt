"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Write SQL queries to organize MEJE's product inventory by categories such as "Kitchen Sink," "Bathroom Sink," and "Smart Toilets," and retrieve all items under "Ceramic Sink."
Generated: DETERMINISTIC_e2338e9577eb5a8c
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the table for storing product inventory
CREATE TABLE ProductInventory (
    ProductID INT PRIMARY KEY,             -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,     -- Name of the product
    Category VARCHAR(100) NOT NULL,        -- Category the product belongs to
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the product
    Stock INT NOT NULL                     -- Number of items in stock
);

-- Insert sample data into the ProductInventory table
INSERT INTO ProductInventory (ProductID, ProductName, Category, Price, Stock)
VALUES
(1, 'Deluxe Kitchen Sink', 'Kitchen Sink', 199.99, 50),
(2, 'Premium Bathroom Sink', 'Bathroom Sink', 149.99, 30),
(3, 'Smart Toilet X', 'Smart Toilets', 399.99, 20),
(4, 'Classic Ceramic Sink', 'Ceramic Sink', 99.99, 40),
(5, 'Modern Ceramic Sink', 'Ceramic Sink', 129.99, 15);

-- Query to organize product inventory by categories and display all products
SELECT Category, ProductName, Price, Stock
FROM ProductInventory
ORDER BY Category, ProductName;

-- Query to retrieve all items under the "Ceramic Sink" category
SELECT ProductID, ProductName, Price, Stock
FROM ProductInventory
WHERE Category = 'Ceramic Sink';
```
