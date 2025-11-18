"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Create a database schema to organize product categories such as "Garage Machines" and "Power Tools" based on the structure of Dotcom Machinery's website.
Generated: DETERMINISTIC_1e43878892e1e7bd
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for organizing product categories

CREATE DATABASE dotcom_machinery;

USE dotcom_machinery;

-- Table to store product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store products associated with categories
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,        -- Name of the product
    category_id INT NOT NULL,                   -- Foreign key to link product with category
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,      -- Quantity of product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE  -- Establishes foreign key relationship
);

-- Example category insertion for "Garage Machines" and "Power Tools"
INSERT INTO product_categories (category_name) VALUES
('Garage Machines'),
('Power Tools');

-- Example product insertion
INSERT INTO products (product_name, category_id, price, stock_quantity) VALUES
('Air Compressor', 1, 299.99, 30),
('Electric Drill', 2, 89.99, 50),
('Table Saw', 1, 499.99, 15),
('Cordless Screwdriver', 2, 59.99, 100);
```
