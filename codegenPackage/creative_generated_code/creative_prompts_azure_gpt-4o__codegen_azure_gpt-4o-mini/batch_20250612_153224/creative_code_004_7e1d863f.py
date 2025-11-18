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
-- Database schema for storing product information for Dolphin Iran

CREATE TABLE Product (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,     -- Name of the product
    category VARCHAR(100) NOT NULL,          -- Product category (e.g., "پرده حمام", "جا ظرفی و آبچکان")
    original_price DECIMAL(10, 2) NOT NULL,  -- Original price of the product
    discounted_price DECIMAL(10, 2),        -- Discounted price of the product (NULL if no discount)
    stock_status BOOLEAN NOT NULL DEFAULT TRUE, -- Stock status: true if in stock, false otherwise
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of product creation
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Index on product_name for faster search queries
CREATE INDEX idx_product_name ON Product(product_name);

-- Index on category for faster filtering
CREATE INDEX idx_category ON Product(category);
```
