"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Suggest a database schema for storing product information from Dolphin Iran, including fields for product name, category (e.g., "پرده حمام" or "جا ظرفی و آبچکان"), original price, discounted price, and stock status.
Generated: DETERMINISTIC_7e1d863f141ba309
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Category VARCHAR(255) NOT NULL,           -- Category of the product (e.g., "پرده حمام", "جا ظرفی و آبچکان")
    OriginalPrice DECIMAL(10, 2) NOT NULL,    -- Original price of the product
    DiscountedPrice DECIMAL(10, 2),           -- Discounted price, if applicable (NULL indicates no discount)
    InStock BOOLEAN NOT NULL DEFAULT TRUE,    -- Stock status: true if in stock, false otherwise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Index for faster queries on Category
CREATE INDEX idx_category ON Products(Category);

-- Sample query to insert product data
INSERT INTO Products (ProductName, Category, OriginalPrice, DiscountedPrice, InStock)
VALUES ('پرده حمام مدل A', 'پرده حمام', 500000, 450000, TRUE);

-- Sample query to retrieve all products in a specific category
SELECT * FROM Products
WHERE Category = 'پرده حمام';

-- Sample query to update stock status
UPDATE Products
SET InStock = FALSE
WHERE ProductID = 1;

-- Sample query to delete a product
DELETE FROM Products
WHERE ProductID = 1;
```
