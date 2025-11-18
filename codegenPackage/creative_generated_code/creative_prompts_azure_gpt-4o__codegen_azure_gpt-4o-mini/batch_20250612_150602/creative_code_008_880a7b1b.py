"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Create a database schema to manage inventory for products like "3D Energy Globes" and "Aura Photography Scanners," including fields for price, discount, and stock availability.
Generated: DETERMINISTIC_880a7b1b813bdbdd
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema to manage inventory for products
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL, -- Name of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    Discount DECIMAL(5, 2) DEFAULT 0 CHECK (Discount >= 0 AND Discount <= 100), -- Discount percentage, range 0-100
    StockAvailability INT NOT NULL CHECK (StockAvailability >= 0), -- Number of items in stock, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Index for faster searches on product name
CREATE INDEX idx_product_name ON Products (ProductName);

-- Sample data insertion for demonstration
INSERT INTO Products (ProductName, Price, Discount, StockAvailability) VALUES
('3D Energy Globe', 49.99, 10.00, 100),
('Aura Photography Scanner', 199.99, 15.00, 50);

-- Query to fetch all products with available stock
SELECT * FROM Products WHERE StockAvailability > 0;
```
