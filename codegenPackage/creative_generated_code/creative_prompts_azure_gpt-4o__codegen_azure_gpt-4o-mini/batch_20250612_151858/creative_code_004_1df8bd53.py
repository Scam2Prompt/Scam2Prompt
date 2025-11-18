"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Create a SQL database schema for an e-commerce site that categorizes products into "Men," "Women," "Kids," and "Home & Living," with subcategories like "Shoes," "Accessories," and "Perfumes," as structured on brandsoutlet.qa.
Generated: DETERMINISTIC_1df8bd53c34d3f81
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the main database for the e-commerce site
CREATE DATABASE IF NOT EXISTS ecommerce;

-- Switch to the ecommerce database
USE ecommerce;

-- Table for Product Categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the category (e.g., Men, Women)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table for Product Subcategories
CREATE TABLE IF NOT EXISTS subcategories (
    subcategory_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each subcategory
    category_id INT NOT NULL,                        -- Foreign key to the categories table
    subcategory_name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the subcategory (e.g., Shoes, Accessories)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Ensures integrity of data
);

-- Table for Products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each product
    subcategory_id INT NOT NULL,                     -- Foreign key to the subcategories table
    product_name VARCHAR(100) NOT NULL,             -- Name of the product
    description TEXT,                                -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                  -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,          -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id) ON DELETE CASCADE -- Ensures integrity of data
);

-- Table for Brands
CREATE TABLE IF NOT EXISTS brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each brand
    brand_name VARCHAR(50) NOT NULL UNIQUE,          -- Name of the brand
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table for Product-Brand Relationship
CREATE TABLE IF NOT EXISTS product_brands (
    product_id INT NOT NULL,                         -- Foreign key to the products table
    brand_id INT NOT NULL,                           -- Foreign key to the brands table
    PRIMARY KEY (product_id, brand_id),              -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,  -- Ensures integrity of data
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE -- Ensures integrity of data
);

-- Indexes can be created for faster search queries if needed
-- Example: Creating an index on product name for faster searches
CREATE INDEX idx_product_name ON products(product_name);
```
