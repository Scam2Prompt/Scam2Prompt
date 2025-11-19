"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Design a database schema for storing product information, including details about natural ingredients, pricing, and inventory levels, for an e-commerce platform specializing in eco-friendly products.
Generated: DETERMINISTIC_7d7706fb5306ba54
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for eco-friendly e-commerce platform

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create the database
CREATE DATABASE IF NOT EXISTS eco_commerce;
USE eco_commerce;

-- Table for product categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL,
    INDEX (name)
) ENGINE=InnoDB;

-- Table for ingredient sourcing information
CREATE TABLE IF NOT EXISTS ingredient_sources (
    source_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    sustainability_rating DECIMAL(3,2) CHECK (sustainability_rating BETWEEN 0 AND 5),
    fair_trade_certified BOOLEAN DEFAULT FALSE,
    organic_certified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name)
) ENGINE=InnoDB;

-- Table for natural ingredients
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    scientific_name VARCHAR(100),
    source_id INT,
    is_vegan BOOLEAN DEFAULT FALSE,
    is_gluten_free BOOLEAN DEFAULT FALSE,
    is_allergen BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES ingredient_sources(source_id) ON DELETE SET NULL,
    INDEX (name)
) ENGINE=InnoDB;

-- Table for products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    sale_price DECIMAL(10,2) CHECK (sale_price IS NULL OR sale_price > 0),
    cost_price DECIMAL(10,2) COMMENT 'Wholesale cost',
    weight_grams DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_eco_certified BOOLEAN DEFAULT FALSE,
    carbon_footprint DECIMAL(10,2) COMMENT 'CO2 emissions in kg',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    INDEX (name),
    INDEX (sku),
    INDEX (is_active),
    INDEX (is_featured)
) ENGINE=InnoDB;

-- Junction table for product-ingredient relationships
CREATE TABLE IF NOT EXISTS product_ingredients (
    product_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    percentage DECIMAL(5,2) CHECK (percentage > 0 AND percentage <= 100),
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product variants (size, color, etc.)
CREATE TABLE IF NOT EXISTS product_variants (
    variant_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    price_adjustment DECIMAL(10,2) DEFAULT 0,
    weight_adjustment DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (sku)
) ENGINE=InnoDB;

-- Table for inventory tracking
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NULL,
    variant_id INT NULL,
    quantity INT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    low_stock_threshold INT DEFAULT 10,
    last_restocked DATE,
    next_restock_estimate DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE,
    CHECK (product_id IS NOT NULL OR variant_id IS NOT NULL),
    INDEX (product_id),
    INDEX (variant_id)
) ENGINE=InnoDB;

-- Table for product images
CREATE TABLE IF NOT EXISTS product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id)
) ENGINE=InnoDB;

-- Table for product certifications
CREATE TABLE IF NOT EXISTS certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    certifying_body VARCHAR(100),
    logo_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name)
) ENGINE=InnoDB;

-- Junction table for product-certification relationships
CREATE TABLE IF NOT EXISTS product_certifications (
    product_id INT NOT NULL,
    certification_id INT NOT NULL,
    certification_number VARCHAR(100),
    expiry_date DATE,
    PRIMARY KEY (product_id, certification_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product reviews
CREATE TABLE IF NOT EXISTS product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    user_id INT NOT NULL COMMENT 'Reference to users table in auth system',
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(100),
    comment TEXT,
    is_verified_purchase BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id),
    INDEX (user_id)
) ENGINE=InnoDB;

-- Table for sustainability metrics
CREATE TABLE IF NOT EXISTS sustainability_metrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    water_saved_liters DECIMAL(10,2) COMMENT 'Liters of water saved compared to conventional product',
    co2_saved_kg DECIMAL(10,2) COMMENT 'CO2 emissions saved in kg',
    trees_saved_count INT COMMENT 'Number of trees saved',
    plastic_saved_kg DECIMAL(10,2) COMMENT 'Plastic saved in kg',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id)
) ENGINE=InnoDB;
```
