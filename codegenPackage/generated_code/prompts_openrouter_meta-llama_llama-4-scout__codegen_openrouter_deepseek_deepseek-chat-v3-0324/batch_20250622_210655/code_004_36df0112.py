"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Design a simple database schema to store product information (e.g., product name, price, quantity) for an e-commerce platform like ShopeeWise.
Generated: DETERMINISTIC_36df0112b2bf01c8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ShopeeWise e-commerce platform

-- Create database
CREATE DATABASE IF NOT EXISTS shopee_wise;
USE shopee_wise;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    sku VARCHAR(100) UNIQUE,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (price >= 0),
    CHECK (quantity >= 0)
) ENGINE=InnoDB;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Add foreign key constraint to products table
ALTER TABLE products
ADD CONSTRAINT fk_category
FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL;

-- Create product images table
CREATE TABLE IF NOT EXISTS product_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_price ON products(price);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_category_name ON categories(name);
```
