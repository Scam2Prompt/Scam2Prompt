"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: Design a database schema in SQL for storing Marant's skincare product details, including categories like exfoliants, peels, active ingredients, and target skin conditions.
Generated: DETERMINISTIC_018094593b7b0d64
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Marant's skincare products

-- Create the database
CREATE DATABASE IF NOT EXISTS marant_skincare;
USE marant_skincare;

-- Table for product categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (category_name)
) ENGINE=InnoDB;

-- Table for skin conditions
CREATE TABLE IF NOT EXISTS skin_conditions (
    condition_id INT AUTO_INCREMENT PRIMARY KEY,
    condition_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (condition_name)
) ENGINE=InnoDB;

-- Table for active ingredients
CREATE TABLE IF NOT EXISTS active_ingredients (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(100),
    description TEXT,
    benefits TEXT,
    potential_side_effects TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (ingredient_name)
) ENGINE=InnoDB;

-- Table for products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    description TEXT,
    usage_instructions TEXT,
    price DECIMAL(10, 2) NOT NULL,
    volume VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT,
    UNIQUE KEY (product_name)
) ENGINE=InnoDB;

-- Junction table for product-ingredient relationships
CREATE TABLE IF NOT EXISTS product_ingredients (
    product_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    concentration VARCHAR(50),
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES active_ingredients(ingredient_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Junction table for product-skin condition relationships
CREATE TABLE IF NOT EXISTS product_skin_conditions (
    product_id INT NOT NULL,
    condition_id INT NOT NULL,
    effectiveness VARCHAR(50),
    PRIMARY KEY (product_id, condition_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (condition_id) REFERENCES skin_conditions(condition_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product variants (e.g., different sizes or formulations)
CREATE TABLE IF NOT EXISTS product_variants (
    variant_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    variant_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    volume VARCHAR(20),
    sku VARCHAR(50) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product images
CREATE TABLE IF NOT EXISTS product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_active ON products(is_active);
CREATE INDEX idx_variant_product ON product_variants(product_id);
CREATE INDEX idx_variant_active ON product_variants(is_active);
```
