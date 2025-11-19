"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Suggest a database schema for storing product information from Dolphin Iran, including fields for product name, category (e.g., "پرده حمام" or "جا ظرفی و آبچکان"), original price, discounted price, and stock status.
Generated: DETERMINISTIC_7e1d863f141ba309
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for Dolphin Iran

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,       -- Name of the product
    Category VARCHAR(100) NOT NULL,          -- Category of the product (e.g., "پرده حمام", "جا ظرفی و آبچکان")
    OriginalPrice DECIMAL(10, 2) NOT NULL,   -- Original price of the product
    DiscountedPrice DECIMAL(10, 2),          -- Discounted price of the product (nullable if no discount)
    StockStatus ENUM('In Stock', 'Out of Stock') NOT NULL, -- Stock status of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Indexes for better performance
CREATE INDEX idx_category ON Products(Category);
CREATE INDEX idx_stock_status ON Products(StockStatus);
```
