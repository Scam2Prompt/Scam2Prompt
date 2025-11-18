"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Create a database schema to store information about Roshako's product offerings, including categories like "Special Metals," "Filler Metals," and "High Performance Alloys," and brands like Esab and Dewalt.
Generated: DETERMINISTIC_728b08d27c495265
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for Roshako's product offerings

-- First, we will create a database called `roshako_products`
CREATE DATABASE IF NOT EXISTS roshako_products;

-- Selecting the database to use
USE roshako_products;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category (e.g., Special Metals)
    description TEXT, -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store brands
CREATE TABLE IF NOT EXISTS brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each brand
    brand_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the brand (e.g., Esab, Dewalt)
    description TEXT, -- Optional description of the brand
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products, linking to categories and brands
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    category_id INT NOT NULL, -- Foreign key referencing categories
    brand_id INT NOT NULL, -- Foreign key referencing brands
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT DEFAULT 0, -- Quantity available in stock
    description TEXT, -- Optional description of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE, -- Ensure referential integrity for categories
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE -- Ensure referential integrity for brands
);

-- Indexes for performance optimization
CREATE INDEX idx_category ON products(category_id);
CREATE INDEX idx_brand ON products(brand_id);

-- Sample data insertion
INSERT INTO categories (category_name, description) VALUES
('Special Metals', 'High-grade metals for specialized applications.'),
('Filler Metals', 'Metals used to fill gaps in welding.'),
('High Performance Alloys', 'Alloys designed for high performance in extreme conditions.');

INSERT INTO brands (brand_name, description) VALUES
('Esab', 'Leading brand in welding and cutting technology.'),
('Dewalt', 'Manufacturer of power tools and hand tools.');

-- Example product insertion (optional)
INSERT INTO products (product_name, category_id, brand_id, price, stock_quantity, description) VALUES
('Special Alloy Wire', 1, 1, 150.00, 100, 'High-quality alloy wire for specialized welding.'),
('Filler Metal Rod', 2, 2, 30.00, 200, 'Durable filler metal rod for welding applications.');

-- Note: Adjust the sample data as needed based on actual product offerings.
```
