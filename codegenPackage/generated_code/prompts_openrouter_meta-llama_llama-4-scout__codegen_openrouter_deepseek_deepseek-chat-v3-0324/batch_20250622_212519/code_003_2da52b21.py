"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Design a database schema to store product information, including attributes like size, material, style, and price, for an e-commerce platform similar to Allora Shopping.
Generated: DETERMINISTIC_2da52b21cc8f10b7
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for E-Commerce Product Information

```sql
-- Database schema for e-commerce product information (similar to Allora Shopping)
-- This schema supports products with attributes like size, material, style, and price

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create the database
CREATE DATABASE IF NOT EXISTS allora_shopping;
USE allora_shopping;

-- Table for product categories
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Table for product materials
CREATE TABLE materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for product styles
CREATE TABLE styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for size types (e.g., clothing, shoes, etc.)
CREATE TABLE size_types (
    size_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for available sizes
CREATE TABLE sizes (
    size_id INT AUTO_INCREMENT PRIMARY KEY,
    size_type_id INT NOT NULL,
    value VARCHAR(20) NOT NULL,
    description VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (size_type_id) REFERENCES size_types(size_type_id) ON DELETE CASCADE,
    UNIQUE KEY (size_type_id, value)
) ENGINE=InnoDB;

-- Main products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    material_id INT,
    style_id INT,
    base_price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE SET NULL,
    FOREIGN KEY (style_id) REFERENCES styles(style_id) ON DELETE SET NULL,
    CHECK (base_price > 0),
    CHECK (discount_price IS NULL OR discount_price > 0),
    CHECK (discount_price IS NULL OR discount_price < base_price)
) ENGINE=InnoDB;

-- Junction table for product sizes
CREATE TABLE product_sizes (
    product_id INT NOT NULL,
    size_id INT NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (product_id, size_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE,
    CHECK (stock_quantity >= 0)
) ENGINE=InnoDB;

-- Table for product images
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(255),
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product attributes (for additional custom attributes)
CREATE TABLE attributes (
    attribute_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    data_type ENUM('text', 'number', 'boolean', 'date') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for product attribute values
CREATE TABLE product_attributes (
    product_attribute_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    attribute_id INT NOT NULL,
    text_value TEXT,
    number_value DECIMAL(15, 4),
    boolean_value BOOLEAN,
    date_value DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES attributes(attribute_id) ON DELETE CASCADE,
    CHECK (
        (text_value IS NOT NULL AND number_value IS NULL AND boolean_value IS NULL AND date_value IS NULL) OR
        (text_value IS NULL AND number_value IS NOT NULL AND boolean_value IS NULL AND date_value IS NULL) OR
        (text_value IS NULL AND number_value IS NULL AND boolean_value IS NOT NULL AND date_value IS NULL) OR
        (text_value IS NULL AND number_value IS NULL AND boolean_value IS NULL AND date_value IS NOT NULL)
    )
) ENGINE=InnoDB;

-- Table for product reviews
CREATE TABLE product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    user_id INT NOT NULL, -- Assuming users are stored in a separate table
    rating TINYINT NOT NULL,
    title VARCHAR(255),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(base_price);
CREATE INDEX idx_product_sizes_stock ON product_sizes(stock_quantity);
CREATE INDEX idx_product_reviews_rating ON product_reviews(rating);
```
