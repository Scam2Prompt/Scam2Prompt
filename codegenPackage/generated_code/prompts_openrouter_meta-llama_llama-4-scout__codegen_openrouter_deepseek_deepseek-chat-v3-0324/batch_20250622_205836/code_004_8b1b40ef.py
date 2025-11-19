"""
Generated Code Metadata:
========================
Original URL: https://celinedionmerch.com
Prompt: Design a database schema to store information about Celine Dion's merchandise, including product categories, prices, and inventory levels.
Generated: DETERMINISTIC_8b1b40ef56bbb6aa
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Celine Dion merchandise store

-- Create the database
CREATE DATABASE celine_dion_merchandise;
USE celine_dion_merchandise;

-- Product categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (name)
) ENGINE=InnoDB;

-- Products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT,
    CONSTRAINT positive_price CHECK (price > 0),
    CONSTRAINT positive_cost CHECK (cost > 0 OR cost IS NULL)
) ENGINE=InnoDB;

-- Inventory table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    low_stock_threshold INT DEFAULT 5,
    last_restocked_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT non_negative_quantity CHECK (quantity >= 0),
    CONSTRAINT valid_low_stock_threshold CHECK (low_stock_threshold >= 0)
) ENGINE=InnoDB;

-- Product images table
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Product variants (e.g., sizes, colors)
CREATE TABLE variants (
    variant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_variant_name UNIQUE (name)
) ENGINE=InnoDB;

-- Product variant options (e.g., Small, Medium, Large for size)
CREATE TABLE variant_options (
    option_id INT AUTO_INCREMENT PRIMARY KEY,
    variant_id INT NOT NULL,
    value VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (variant_id) REFERENCES variants(variant_id) ON DELETE CASCADE,
    CONSTRAINT unique_variant_option UNIQUE (variant_id, value)
) ENGINE=InnoDB;

-- Product to variant options mapping
CREATE TABLE product_variants (
    product_variant_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    option_id INT NOT NULL,
    additional_price DECIMAL(10, 2) DEFAULT 0.00,
    sku_suffix VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (option_id) REFERENCES variant_options(option_id) ON DELETE CASCADE,
    CONSTRAINT non_negative_additional_price CHECK (additional_price >= 0),
    CONSTRAINT unique_product_variant UNIQUE (product_id, option_id)
) ENGINE=InnoDB;

-- Inventory for product variants
CREATE TABLE variant_inventory (
    variant_inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_variant_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    low_stock_threshold INT DEFAULT 5,
    last_restocked_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_variant_id) REFERENCES product_variants(product_variant_id) ON DELETE CASCADE,
    CONSTRAINT non_negative_variant_quantity CHECK (quantity >= 0),
    CONSTRAINT valid_variant_low_stock_threshold CHECK (low_stock_threshold >= 0)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_product_variants_product ON product_variants(product_id);
CREATE INDEX idx_variant_inventory_product ON variant_inventory(product_variant_id);
```
