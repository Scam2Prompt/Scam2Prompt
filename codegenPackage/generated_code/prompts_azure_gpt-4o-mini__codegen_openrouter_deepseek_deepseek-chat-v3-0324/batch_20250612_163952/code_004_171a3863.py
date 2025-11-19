"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: Design a database schema for an online store that includes tables for products like wines and gift baskets, as seen on 11 Tesoros Ibéricos, ensuring it supports various product categories and pricing.
Generated: DETERMINISTIC_171a386377ce54e4
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Online Store (11 Tesoros Ibéricos)

```sql
-- Database creation
CREATE DATABASE online_store;
USE online_store;

-- Product categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    cost_price DECIMAL(10, 2),
    quantity_in_stock INT DEFAULT 0,
    min_order_quantity INT DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Product attributes table
CREATE TABLE product_attributes (
    attribute_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_filterable BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Product attribute values
CREATE TABLE product_attribute_values (
    product_id INT NOT NULL,
    attribute_id INT NOT NULL,
    value TEXT NOT NULL,
    PRIMARY KEY (product_id, attribute_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES product_attributes(attribute_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Wine-specific attributes
CREATE TABLE wines (
    product_id INT PRIMARY KEY,
    vintage YEAR,
    alcohol_content DECIMAL(5, 2),
    bottle_size_ml INT,
    region VARCHAR(100),
    grape_variety VARCHAR(100),
    aging_process VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Gift basket-specific attributes
CREATE TABLE gift_baskets (
    product_id INT PRIMARY KEY,
    basket_size VARCHAR(50),
    contains_alcohol BOOLEAN DEFAULT FALSE,
    is_customizable BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Product images
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Pricing tiers (for volume discounts)
CREATE TABLE pricing_tiers (
    tier_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    min_quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT chk_min_quantity CHECK (min_quantity > 0)
) ENGINE=InnoDB;

-- Product inventory log
CREATE TABLE inventory_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_change INT NOT NULL,
    previous_quantity INT NOT NULL,
    new_quantity INT NOT NULL,
    reason ENUM('purchase', 'return', 'adjustment', 'damage', 'other') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Product tags
CREATE TABLE tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
) ENGINE=InnoDB;

-- Product-tag mapping
CREATE TABLE product_tags (
    product_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Related products
CREATE TABLE related_products (
    product_id INT NOT NULL,
    related_product_id INT NOT NULL,
    relation_type ENUM('complementary', 'similar', 'upsell', 'cross-sell') NOT NULL,
    PRIMARY KEY (product_id, related_product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (related_product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT chk_different_products CHECK (product_id != related_product_id)
) ENGINE=InnoDB;

-- Indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_active ON products(is_active);
CREATE INDEX idx_product_attributes ON product_attribute_values(attribute_id);
CREATE INDEX idx_inventory_product ON inventory_log(product_id);
```
