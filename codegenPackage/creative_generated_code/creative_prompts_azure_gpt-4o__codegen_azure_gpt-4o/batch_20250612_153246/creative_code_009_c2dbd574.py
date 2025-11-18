"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://granstore.co
Prompt: Generate a SQL query to store product attributes like "Bombilla Led inteligente Tuya con Bluetooth" and "Molino Eléctrico para Café y especias" into a relational database for the GranStore inventory system.
Generated: DETERMINISTIC_c2dbd574a876913d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create table to store product attributes for the GranStore inventory system
CREATE TABLE ProductAttributes (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Category VARCHAR(100),                     -- Category of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the ProductAttributes table
INSERT INTO ProductAttributes (ProductName, Description, Category, Price, Stock)
VALUES
    ('Bombilla Led inteligente Tuya con Bluetooth', 
     'Smart LED bulb compatible with Tuya app and Bluetooth control.', 
     'Electronics', 12.99, 100),
    ('Molino Eléctrico para Café y especias', 
     'Electric grinder for coffee and spices, durable and efficient.', 
     'Appliances', 29.99, 50);

-- Query to retrieve all product attributes (example for testing data retrieval)
SELECT * FROM ProductAttributes;

-- Ensure proper error handling during querying or inserting data (example for application-side handling)
-- When executing these queries in your applications, use prepared statements to avoid SQL injection
-- and ensure transaction management for critical operations.
```
