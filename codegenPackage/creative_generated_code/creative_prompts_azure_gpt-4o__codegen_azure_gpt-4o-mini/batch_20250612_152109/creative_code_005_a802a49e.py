"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a database schema in SQL for managing a catalog of flip-flop products, including fields for product name, category, material type, and customization options.
Generated: DETERMINISTIC_a802a49eb2817f7a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing a catalog of flip-flop products

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS flip_flop_catalog;

-- Switch to the created database
USE flip_flop_catalog;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product category
    description TEXT,                             -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store flip-flop products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    product_name VARCHAR(100) NOT NULL,           -- Name of the product
    category_id INT,                               -- Foreign key to the product category
    material_type VARCHAR(100) NOT NULL,          -- Type of material used in the flip-flop
    customization_options TEXT,                    -- Details on customization options available
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE SET NULL -- Relationship to category
);

-- Index for optimizing product searches by name
CREATE INDEX idx_product_name ON products(product_name);
```
