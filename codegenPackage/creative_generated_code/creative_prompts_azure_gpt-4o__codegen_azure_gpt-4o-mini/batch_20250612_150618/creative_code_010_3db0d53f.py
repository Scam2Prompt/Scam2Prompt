"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Create a database schema for storing product details, categories, and promotions for an e-commerce platform like "Mass Compras."
Generated: DETERMINISTIC_3db0d53f5a27bba2
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for E-commerce Platform "Mass Compras"

-- Drop existing tables if they exist (for redefinition)
DROP TABLE IF EXISTS Promotions;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- Table to store product categories
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,       -- Name of the category (must be unique)
    description TEXT,                        -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store product details
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,              -- Name of the product
    description TEXT,                        -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Amount of product in stock
    category_id INT REFERENCES Categories(id) ON DELETE SET NULL, -- Foreign key to Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store promotions related to products
CREATE TABLE Promotions (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each promotion
    product_id INT REFERENCES Products(id) ON DELETE CASCADE, -- Foreign key to Products table
    discount_percentage DECIMAL(5, 2) NOT NULL CHECK (discount_percentage >= 0 AND discount_percentage <= 100), -- Discount percentage (0-100)
    start_date DATE NOT NULL,                -- Start date of the promotion
    end_date DATE NOT NULL,                  -- End date of the promotion
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Indexes to improve query performance
CREATE INDEX idx_category_name ON Categories(name);
CREATE INDEX idx_product_name ON Products(name);
CREATE INDEX idx_product_category ON Products(category_id);
CREATE INDEX idx_promotion_product ON Promotions(product_id);
```
