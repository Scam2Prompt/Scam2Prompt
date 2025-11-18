"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Create an SQL database schema for storing track cycling product details, including fields for product name, category (e.g., "Track Tyres," "Track Powermeters"), price, stock status, and UCI approval.
Generated: DETERMINISTIC_05de2b2c9027ec3c
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for Track Cycling Products

CREATE TABLE IF NOT EXISTS product_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product category (e.g., "Track Tyres")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE IF NOT EXISTS track_products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,         -- Name of the product
    category_id INT NOT NULL,                    -- Foreign key referencing product category
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Product price, must be non-negative
    stock_status ENUM('In Stock', 'Out of Stock', 'Pre-order') NOT NULL, -- Product stock status
    uci_approval BOOLEAN DEFAULT FALSE,          -- UCI approval status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) -- Foreign key constraint
);

-- Index for faster searches
CREATE INDEX idx_product_name ON track_products(product_name);
CREATE INDEX idx_category ON track_products(category_id);
```
