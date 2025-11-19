"""
Generated Code Metadata:
========================
Original URL: https://www.meje.cc
Prompt: Write SQL queries to organize MEJE's product inventory by categories such as "Kitchen Sink," "Bathroom Sink," and "Smart Toilets," and retrieve all items under "Ceramic Sink."
Generated: DETERMINISTIC_e2338e9577eb5a8c
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to organize MEJE's product inventory by categories
-- and retrieve all items under the "Ceramic Sink" category.

-- Create a table to store product inventory
CREATE TABLE ProductInventory (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into the ProductInventory table
INSERT INTO ProductInventory (ProductName, Category, Price, StockQuantity) VALUES
('Stainless Steel Kitchen Sink', 'Kitchen Sink', 199.99, 50),
('Ceramic Kitchen Sink', 'Kitchen Sink', 249.99, 30),
('Ceramic Bathroom Sink', 'Bathroom Sink', 149.99, 20),
('Smart Toilet Model X', 'Smart Toilets', 899.99, 15),
('Ceramic Sink Model Y', 'Ceramic Sink', 199.99, 25),
('Ceramic Sink Model Z', 'Ceramic Sink', 299.99, 10);

-- Query to retrieve all items under the "Ceramic Sink" category
SELECT ProductID, ProductName, Price, StockQuantity
FROM ProductInventory
WHERE Category = 'Ceramic Sink';

-- Error handling: Check if the query returns results
-- This part is typically handled in application code, but for demonstration:
IF (SELECT COUNT(*) FROM ProductInventory WHERE Category = 'Ceramic Sink') = 0 THEN
    SELECT 'No items found under the Ceramic Sink category.' AS Message;
END IF;
```
