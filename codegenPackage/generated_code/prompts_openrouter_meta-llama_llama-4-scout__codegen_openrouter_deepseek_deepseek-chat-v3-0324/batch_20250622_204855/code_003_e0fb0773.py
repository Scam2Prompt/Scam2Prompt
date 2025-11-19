"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Design a database schema to store information about various sports equipment and apparel, including details like product name, price, and sport type, inspired by the content on this webpage.
Generated: DETERMINISTIC_e0fb0773f1c2551d
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for sports equipment and apparel

-- Create the database
CREATE DATABASE IF NOT EXISTS sports_equipment_db;
USE sports_equipment_db;

-- Table for sport categories
CREATE TABLE IF NOT EXISTS sports (
    sport_id INT AUTO_INCREMENT PRIMARY KEY,
    sport_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (sport_name)
) ENGINE=InnoDB;

-- Table for brands
CREATE TABLE IF NOT EXISTS brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL,
    country_of_origin VARCHAR(50),
    founded_year YEAR,
    website VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (brand_name)
) ENGINE=InnoDB;

-- Table for product categories
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    parent_category_id INT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES product_categories(category_id) ON DELETE SET NULL,
    UNIQUE KEY (category_name, parent_category_id)
) ENGINE=InnoDB;

-- Main products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    brand_id INT NOT NULL,
    category_id INT NOT NULL,
    sport_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    color VARCHAR(30),
    size VARCHAR(20),
    material VARCHAR(50),
    weight_grams INT,
    is_in_stock BOOLEAN DEFAULT TRUE,
    stock_quantity INT DEFAULT 0,
    sku VARCHAR(50) UNIQUE,
    barcode VARCHAR(50) UNIQUE,
    release_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE RESTRICT,
    FOREIGN KEY (sport_id) REFERENCES sports(sport_id) ON DELETE RESTRICT
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

-- Table for product reviews
CREATE TABLE IF NOT EXISTS product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    user_id INT NOT NULL, -- Assuming users are stored in a separate table
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for product features
CREATE TABLE IF NOT EXISTS product_features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    feature_name VARCHAR(100) NOT NULL,
    feature_description TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_products_sport ON products(sport_id);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_brand ON products(brand_id);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_stock ON products(is_in_stock);
CREATE INDEX idx_product_images ON product_images(product_id);
CREATE INDEX idx_product_reviews ON product_reviews(product_id);
```
